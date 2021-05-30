docker stop {container_name}
docker rm {container_name}
docker run --net=container:mooongo_py -d --name {container_name} {dockerhub_login}/{container_name}