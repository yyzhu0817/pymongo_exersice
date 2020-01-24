import pymongo

'''
修改操作
update(query,update,upsert=False,multi=False) #multi=True表示修改所有符合条件的文档
update_many()
update_one()

'''
# 创建mongodb的数据库连接对象
conn = pymongo.MongoClient('localhost', 27017)

# 创建数据库对象
db = conn.stu

# 创建集合对象
myset = db.class0

# 修改操作
# myset.update({'name':'鲁迅'},{'$unset':{'book':''}}) # 删除域

# 将所有男的年纪修改为22
# myset.update({'sex': 'm'}, {'$set': {'age': 22}}, multi=True)

# 如果匹配文档不存在则插入
myset.update({'name': '赵怀芳'}, {'$set':{'age': 21}}, upsert=True)

# 关闭连接
conn.close()
