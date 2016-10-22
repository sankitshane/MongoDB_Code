import pymongo
import sys

connection = pymongo.MongoClient('mongodb://localhost')

db = connection.students
grade = db.grades

def remove_vals():
    query = {'type':'homework'}
    sort_query = {'student_id':1,'score':1}

    try:
        val = grade.find(query).sort([('student_id',pymongo.ASCENDING),('score', pymongo.ASCENDING)])

    except Exception as e:
        print 'Unexpected error', type(e), e

    for i in range(val.count()):
        results = grade.delete_many({'_id':val[i]['_id']})


if __name__ == '__main__':
    remove_vals()
