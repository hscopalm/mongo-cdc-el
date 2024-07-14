# mongo-cdc-el
A simple, python based method for extracting and loading a mongodb database into an s3 destination

## Setup
1. Connect to raspberry PI
    `ssh harrison@192.168.0.110`
2. Login
3. `docker-compose up`
4. In a new shell, `mongosh "mongodb://192.168.0.110:27017"`