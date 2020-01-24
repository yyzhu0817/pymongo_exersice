import pymongo

'''
删除操作
remove(query,multi = True)
multi默认是true表示删除所有query过滤文档
设置为False表示只删除第一个
'''
# 创建mongodb的数据库连接对象
conn = pymongo.MongoClient('localhost', 27017)

# 创建数据库对象
db = conn.stu

# 创建集合对象
myset = db.class0

# 删除操作
# myset.remove({'name':'赵怀芳'})
myset.remove({'name': {'$exists': False}})

# 复合操作
myset.find_one_and_delete({'name':'鲁迅'}) #查找并删除


# 关闭连接
conn.close()
