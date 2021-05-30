docker stop {container_name}
docker rm {container_name}
docker run -p 8080:8080 -d --name {container_name} {dockerhub_login}/{container_name}


docker stop mooongo_mongo
docker rm mooongo_mongo
docker run --net=container:mooongo_py -d --name mooongo_mongo {dockerhub_login}/mooongo_mongo