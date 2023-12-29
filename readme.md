## build docker
docker build -t django-docker

## run docker
docker run -p 8080:8000 django-docker

## access django
localhost:8080