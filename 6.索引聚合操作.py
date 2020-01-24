import pymongo

conn = pymongo.MongoClient('localhost', 27017)
db = conn.stu
myset = db.class0

# 索引操作
'''
ensure_index() :创建索引
list_indexes() ：查看索引
drop_index() ：删除索引
drop_indexes() ：删除所有索引
'''
# index = myset.ensure_index('name')
index = myset.ensure_index([('age', -1)]) # 对age 创建逆向索引
print(f'index名称:{index}')
# 获取当前的索引
for i in myset.list_indexes():
    print(i)

# 删除所有索引
myset.drop_indexes()

# 创建唯一索引
myset.ensure_index('name',name='mynameIndex',unique=True)

conn.close()