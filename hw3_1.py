import sys
import pymongo

connection = pymongo.MongoClient('mongodb://localhost')

db = connection.school
student = db.students


def find_and_delete():
    res = student.find({},{'scores':1})
    low = 0
    for doc in res:
        for i in doc["scores"]:
            if i["type"] == 'homework':
                if low == 0:
                    low = i['score']
                elif low > i['score']:
                    low = i['score']
        for i in doc['scores']:
            if i['score'] == low:
                doc['scores'].remove(i)
        print doc
        low = 0


        student.update_one({'_id':doc['_id']},{'$set':{'scores':doc['scores']}})

if __name__ == '__main__':
    find_and_delete()
