import bottle
import pymongo

@bottle.route('/')

def index():
    connection = pymongo.MongoClient('localhost',27017)
    db = connection.test
    name = db.names
    items = name.find_one()

    return '<b>Hello %s!</b>' % items['name']

bottle.run(host='localhost',port = 8082)
