import pymongo

conn = pymongo.MongoClient('localhost', 27017)
db = conn.grade
myset = db.class1

'''
聚合操作
aggregate([])
参数：和mongo shell一样
返回值：返回和find()函数相同的游标对象

'''

p = [
    {'$group': {'_id': '$king', 'count': {'$sum': 1}}},
    # {'$match': {'count': {'$gt': 1}}},
]
cur = myset.aggregate(p)

for i in cur:
    print(i)

conn.close()
