import sys
import pymongo

connection = pymongo.MongoClient('mongodb://localhost')

db = connection.school
student = db.students


def find_and_delete():
    res = student.find()

    low_score = 0
    for doc in res:
        for i in doc:
            if i == 'scores':
                for j in i:
                    if j == 'homework':
                        if(low_score == 0):
                            low_score = j.score
                        else:
                            if(low_score > j.scores):
                                low_score = j.scores
        for i in doc:
            if i == 'scores':
                for j in i:
                    if j == 'homework':
                        if j.score == low_score and j.type =='homework':
                            doc.scores.remove(i)

    for doc in res:
        print doc

if __name__ == '__main__':
    find_and_delete()
