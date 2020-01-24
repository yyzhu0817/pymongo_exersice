import pymongo

# 创建mongodb的数据库连接对象
conn = pymongo.MongoClient('localhost', 27017)

# 创建数据库对象
db = conn.grade

# 创建集合对象
myset = db.class1

# 插入
'''
insert()
insert_many()
insert_one()
save(): 与insert()区别，如果id已经存在，覆盖原有的数据
'''
# myset.insert( # 插入一条数据
#     {"name": "yyzhu",
#      "king": 'fuck'}
# )

myset.insert(  # 插入多条数据
    [
        {"name": "fang",
         "king": "shit"},
        {"name": "zhu",
         "king": "hahha"}
    ]
)

myset.save(
    {"_id": 1,
     "name": "a",
     "king": "ddd"}
)

# myset.insert_many(  # 插入多条数据
#     [
#         {"name": "lvtian",
#          "king": "华师"},
#         {"name": "a",
#          "king": "bbb"}
#     ]
# )

# myset.insert_one( # 插入一个
#     {"name": "yige",
#      "king": "shit"},
#     {"name": "yige2",
#      "king": "shit2"}
# )

# 关闭连接
conn.close()
