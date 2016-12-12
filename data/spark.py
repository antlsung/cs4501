from pyspark import SparkContext
import itertools

def logic(x):
	print(x)
	y = []
	for row in x:
		temp = []
		for a in range(0,row):
			temp.append(a)
		y.append(temp)
	return y

sc = SparkContext("spark://spark-master:7077", "PopularItems")

data = sc.textFile("/tmp/data/access.log", 2)     # each worker loads a piece of the data file

pairs = data.map(lambda line: line.split("\t"))   # tell each worker to split each line of it's partition
print ("HERE PAIRS>>>>>>>>>>>>>>>>>>>>>>>")
output = pairs.collect()                          # bring the data back to the master node so we can print it out
for pair1, pair2 in output:
    print ("pair part 1: %s part2: %s" % (pair1, pair2))
print ("PAIRS DONE")

groups = pairs.groupByKey()
# groups_distinct = groups[].distinct()
print ("HERE GROUPS>>>>>>>>>>>>>>>>>>>>>>>")
output = groups.collect()                          # bring the data back to the master node so we can print it out
for pair1, pair2 in output:
	print ("group part 1: %s part2: %s" % (pair1, pair2))
	for c in pair2:
		print("id clicked on: %s" % (c))
print ("GROUPS DONE")

pages = groups.map(lambda pair: (pair[0], set(pair[1])))
print ("HERE MAPS>>>>>>>>>>>>>>>>>>>>>>>")
output = pages.collect()                          # bring the data back to the master node so we can print it out
for pair1, pair2 in output:
	print ("group part 1: %s part2: %s" % (pair1, pair2))
	for c in pair2:
		print("id clicked on: %s" % (c))
print ("MAPS DONE")

permutations = pages.map(lambda pair: (pair[0],list(itertools.combinations(pair[1], 2))))
print ("HERE PERMUTATIONS>>>>>>>>>>>>>>>>>>>>>>>")
output = permutations.collect()                          # bring the data back to the master node so we can print it out
x=[]
for pair1, pair2 in output:
	print ("pair part 1: %s part2: %s" % (pair1, pair2))
	x.append(len(pair2))
print ("PERMUTATIONS DONE")

print ("SIZEEEEEEEEEEEEEEEEEEEEEEEEEEE")
# x = len(list(itertools.combinations(pair[1], 2)))
print(x)
arr = logic(x)
print(arr)
print ("HERE WORK>>>>>>>>>>>>>>>>>>>>>>>")
arr2 = [0,1,2]
blah = permutations.map(lambda output: (output[0],output[1][0]))
total = blah.collect()
for b1, b2 in total:
	print ("B part 1: %s part2: %s" % (b1, b2))

# flat = permutations.flatMap(lambda pair: (pair[0],list(itertools.combinations(pair[1], 2))) )
# print ("HERE FLAT>>>>>>>>>>>>>>>>>>>>>>>")
# output = flat.collect()                          # bring the data back to the master node so we can print it out
# for pair1 in output:
# 	print ("pair part 1: %s part2: %s" % (pair1, pair2))
# print ("PERMUTATIONS DONE")
#





count = pages.reduceByKey(lambda x,y: x+y)        # shuffle the data so that each key is only on one worker
                                                  # and then reduce all the values by adding them together

output = count.collect()                          # bring the data back to the master node so we can print it out
for shoe_id, count in output:
    print ("Shoe ID: %s Count: %d" % (shoe_id, count))
print ("Popular items done")

sc.stop()



#pair[1] -> pair[0]
