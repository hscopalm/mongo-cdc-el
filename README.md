# mongo-cdc-el
A simple, python based method for extracting and loading a mongodb database into an s3 destination

## Prerequisites
1. Docker and Docker-compose
2. Pull the `mongo:latest` image
3. A host for the mongodb server, as well as a potentially remote machine to process the stream

## Setup
1. Connect to raspberry PI
    `ssh harrison@192.168.0.110`
2. Login
3. `docker-compose up`
4. In a new shell, `mongosh "mongodb://192.168.0.110:27017"`


Sample dummy data
```
application_db> db.customers.find().limit(1)
[
  {
    _id: ObjectId('66a5d976e088e0ce4e5fe102'),
    name: 'Andrea Byrd',
    email: 'martinezbruce@example.org',
    address: '836 Stevens Spurs Apt. 693\nLake Scott, PW 06976'
  }
]
application_db> db.orders.find().limit(1)
[
  {
    _id: ObjectId('66a5d976e088e0ce4e5fe103'),
    customer_id: ObjectId('66a5d976e088e0ce4e5fe102'),
    product: 'side',
    quantity: 9,
    price: 85.70763509916955
  }
]
application_db> db.returns.find().limit(1)
[
  {
    _id: ObjectId('66a5d976e088e0ce4e5fe104'),
    order_id: ObjectId('66a5d976e088e0ce4e5fe103'),
    reason: 'Not satisfied',
    status: 'Pending'
  }
]
```