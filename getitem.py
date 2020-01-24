class DataBase:

    def __init__(self, id, address):
        '''初始化方法'''
        self.id = id
        self.address = address

    def __getitem__(self, key):
        return self.__dict__.get(key, "100")


data = DataBase(1, "192.168.2.11")
print(data["hi"])
print(data["id"])
