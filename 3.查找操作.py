import pymongo

# 创建mongodb的数据库连接对象
conn = pymongo.MongoClient('localhost', 27017)

# 创建数据库对象
db = conn.stu

# 创建集合对象
myset = db.class0

'''
find()
功能 ： 查找数据库内容
参数 ： 同mongo shell find()
返回值： 返回一个结果游标

find_one()
功能：查询第一条符合条件的文档
参数： 同find（）
返回值： 返回一个字典
'''
'''在pymongo中所有操作符的用法同mongo shell相同，只是操作时加引号，以字符串的方式写入python代码'''

'''
cursor对象的属性:
next()
limit()
skip()
count()
sort()
'''
cursor = myset.find({'$or':
                         [{'sex': 'w'},
                          {'age': {'$lt': 19}}
                          ]}, {'_id': 0})

for i in cursor:
    print(i)

# res = myset.find_one({'name':'fang'},{'_id':0})
# print(res)
# 关闭连接
conn.close()
