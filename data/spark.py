from pyspark import SparkContext

sc = SparkContext("spark://spark-master:7077", "PopularItems")

data = sc.textFile("/tmp/data/access.log", 2)     # each worker loads a piece of the data file

pairs = data.map(lambda line: line.split("\t"))   # tell each worker to split each line of it's partition
print ("HERE PAIRS>>>>>>>>>>>>>>>>>>>>>>>")
output = pairs.collect()                          # bring the data back to the master node so we can print it out
for pair1, pair2 in output:
    print ("pair part 1: %s part2: %s" % (pair1, pair2))
print ("PAIRS DONE")

groups = pairs.groupByKey()
print ("HERE  GROUPS>>>>>>>>>>>>>>>>>>>>>>>")
output = groups.collect()                          # bring the data back to the master node so we can print it out
for pair1, pair2 in output:
	print ("group part 1: %s part2: %s" % (pair1, pair2))
	for c in pair2:
		print("id clicked on: %s" % (c))
print ("GROUPS DONE")

pages = groups.flatMap()
print ("HERE  MAPS>>>>>>>>>>>>>>>>>>>>>>>")
output = pages.collect()                          # bring the data back to the master node so we can print it out
for pair1, pair2 in output:
	print ("maps part 1: %s part2: %s" % (pair1, pair2))
print ("MAPS DONE")


pages = pairs.map(lambda pair: (pair[1], 1))      # re-layout the data to ignore the user id
print ("HERE  MAPS>>>>>>>>>>>>>>>>>>>>>>>")
output = pages.collect()                          # bring the data back to the master node so we can print it out
for pair1, pair2 in output:
	print ("maps part 1: %s part2: %s" % (pair1, pair2))
print ("MAPS DONE")

count = pages.reduceByKey(lambda x,y: x+y)        # shuffle the data so that each key is only on one worker
                                                  # and then reduce all the values by adding them together

output = count.collect()                          # bring the data back to the master node so we can print it out
for shoe_id, count in output:
    print ("Shoe ID: %s Count: %d" % (shoe_id, count))
print ("Popular items done")

sc.stop()



#pair[1] -> pair[0]
