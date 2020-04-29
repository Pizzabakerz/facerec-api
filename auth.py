import sqlite3


class auth:
    def __init__(self):
        self.con = sqlite3.connect('data.db')
        self.cur = self.con.cursor()
    def authentication(self, username,password,operation):
        response = False
        if operation == "signup":
            self.cur.execute("INSERT INTO users VALUES('{}','{}')".format(username,password))
            self.con.commit()
            self.con.close()
            response = True
        elif operation == "login":            
            self.cur.execute("SELECT * FROM users WHERE username = '{}' AND password = '{}' ".format(username,password))
            data = self.cur.fetchone()
            self.con.commit()
            self.con.close()
            if data != None:
                response = True
        return response

