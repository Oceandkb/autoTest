import pymysql

db_info = {
    "host": "192.168.1.69",
    "user": "faqrobot",
    "password": "N5AFzUgI3uDml4zk",
    "database": "v5_test",
    "port": 3306,
}


class ConnectDb(object):

    def __init__(self, db_info):
        # 初始化，连上数据库
        self.db = pymysql.connect(**db_info,
                                  cursorclass=pymysql.cursors.DictCursor)
        # 创建游标
        self.cur = self.db.cursor()

    def select_sql(self, sql):
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result

    def execute_sql(self, sql):
        self.cur.execute(sql)
        self.db.commit()

    def close(self):
        self.cur.close()
        self.db.close()


if __name__ == '__main__':
    db = ConnectDb(db_info)
    user_sql = 'SELECT * from public_user WHERE name="mirrorTest";'
    r = db.select_sql(user_sql)
    print(r)
