# Deployment Steps

## Launch EC2 Instance

- Created AWS EC2 instance
- Connected using SSH

## Install Docker

sudo yum install docker -y
sudo systemctl start docker

## Deploy Application

git clone <repo>
cd InfraPulse
docker-compose up -d

## Verify Container

docker ps

## Verify Application

curl http://localhost:5000

