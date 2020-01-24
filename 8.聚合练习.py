import pymongo

conn = pymongo.MongoClient('localhost', 27017)
db = conn.grade
myset = db.class0

'''
聚合操作
aggregate([])
参数：和mongo shell一样
返回值：返回和find()函数相同的游标对象

'''
from random import randint

cur = myset.find()
for i in cur:
    myset.update(
        {'_id': i['_id']},
        {'$set': {'score': {
            'chinese': randint(60, 100),
            'math': randint(60, 100),
            'english': randint(60, 100)
        }}}
    )
# 按照性别分组统计每组人数
p1 = [
    {'$group': {'_id': '$gender', 'number': {'$sum': 1}}},
]

# 统计每名男生的语文成绩
p2 = [
    {'$match': {'gender': 'm'}},
    {'$project': {'_id': 0, 'name': 1, 'score.chinese': 1}},
]

# 将女生按照英语成绩降序排列
p3 = [
    {'$match': {'gender': 'w'}},
    {'$sort': {'score.english': -1}}
]

cursor = myset.aggregate(p3)
for i in cursor:
    print(i)

conn.close()
