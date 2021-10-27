# MOX-proto

## This repo contains all of the code need

# Build system

docker-compose up --build -d
docker-compose up -d

# Connect to the Unreal Engine gRPC client generator

docker-compose exec gen_ue bash

cd pipelines
./gen_ue.sh


docker-compose exec gen_client bash

cd pipelines
./gen_py.sh
