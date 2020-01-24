import pymongo

# 创建mongodb的数据库连接对象
conn = pymongo.MongoClient('localhost',27017)

# 创建数据库对象
db = conn.grade

# 创建集合对象
myset = db.class1

# 数据操作
print(dir(myset), end='\n')

# 关闭连接
conn.close()

