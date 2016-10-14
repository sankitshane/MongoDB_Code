import sys
import pymongo

connection = pymongo.MongoClient('mongodb://localhost')

db = connection.test
users = db.users

doc = {
    'firstname':'Sankit',
    'latname':'Acharya'
}

print doc
print 'about to insert the document'

try:
    users.insert_one(doc)
except Exception as e:
    print 'inset failed:', e

print doc
print 'insert again'

try:
    users.insert_one(doc)
except Exception as e:
    print 'inset failed:', e 
