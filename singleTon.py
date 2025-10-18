class DBConnection:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
            return cls.__instance
        return cls.__instance

    def connect_db(self):
        print("Connecting to DB")


db = DBConnection()
db2 = DBConnection()

print(db == db2)
db.connect_db()
db2.connect_db()
