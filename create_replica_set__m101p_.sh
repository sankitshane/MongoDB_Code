#!/usr/bin/env bash

mkdir  /data/rs1 /data/rs2 /data/rs3
mongod --replSet m101 --logpath "1.log" --dbpath /data/rs1 --port 27017 --oplogSize 64 --fork --smallfiles
mongod --replSet m101 --logpath "2.log" --dbpath /data/rs2 --port 27018 --oplogSize 64 --smallfiles --fork
mongod --replSet m101 --logpath "3.log" --dbpath /data/rs3 --port 27019 --oplogSize 64 --smallfiles --fork

use start mongod in windows and not --fork

start mongod --replSet m101 --logpath "1.log" --dbpath C:\Users\SCHOOL\data\r1 --port 27017 --smallfiles --oplogSize 64
start mongod --replSet m101 --logpath "2.log" --dbpath C:\Users\SCHOOL\data\r2 --port 27018 --smallfiles --oplogSize 64
start mongod --replSet m101 --logpath "3.log" --dbpath C:\Users\SCHOOL\data\r3 --port 27019 --smallfiles --oplogSize 64
