#Run Commands

##1. Run the mysql container
'docker run --name mysql -d -e MYSQL\_ROOT\_PASSWORD='$3cureUS' -v ~/cs4501/db:/var/lib/mysql  mysql:5.7.14'

##2. Docker Compose
'docker-compose up'

##3. Getting into the container
'docker ps'
###copy docker container id
'docker exec -it INSERT_CONTAINER_ID /bin/bash'



#Extra Commands
##Update mysql database
'manage.py makemigrations jbay'
