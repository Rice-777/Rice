import pymssql
import threading


class ConnectSqlServer:
    def __init__(self, host, port, user, pwd, db):
        self.host = host
        self.user = user
        self.port = port
        self.pwd = pwd
        self.db = db

    def GetConnect(self):
        self.conn = pymssql.connect(host=self.host, port=self.port, user=self.user, password=self.pwd,
                                    database=self.db, charset='utf8', as_dict=False, autocommit=True)
        cur = self.conn.cursor()
        return cur

    def judge_connect(self):
        t = threading.Thread(target=self.GetConnect)
        t.setDaemon(True)
        t.start()
        t.join(3)
        if str(t)[-21:-14] == "started":
            return False
        if str(t)[-21:-14] == "tarted ":
            return False
        if str(t)[-21:-14] == "stopped" or "topped " or " stoppe":
            return True

    def ExecQuery(self, sql):
        cur = self.GetConnect()
        cur.execute(sql)
        result = cur.fetchall()
        self.conn.close()
        return result

    def ExecNoneQuery(self, sql):
        cur = self.GetConnect()
        cur.execute(sql)
        self.conn.close()


if __name__ == '__main__':
    connect = ConnectSqlServer(host='127.0.0.1', port=1433, user='sa', pwd='777', db='Rice')
    print(connect.judge_connect())
