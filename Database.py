import sqlite3


class Function:
    def __init__(self):
        self.base = sqlite3.connect("users.db")
        self.cursor = self.base.cursor()
        self.ls = ["Pythonda dasturlash", 'Arxitektura va dizayn', 'Grafika dizayni', 'Kompyuter savodxonligi',
                   'android dasturlash', "Veb dasturlash", "Mobil robototexnika"]

    def tables(self):
        for i in range(1, 8):
            print(self.ls[i - 1])
            self.cursor.execute(
                f"""CREATE TABLE IF NOT EXISTS "{self.ls[i - 1]}" (fullname TEXT, birthday TEXT, timetable TEXT, phone TEXT)""")

    def signup(self, lst: list) -> str:
        lst2 = [lst[1], lst[2], lst[3], lst[4]]
        self.cursor.execute(f"""INSERT INTO "{lst[0]}" VALUES (?, ?, ?, ?)""", lst2)
        self.base.commit()
        return f"Tabriklaymiz {lst[1]}!!! Siz ro'yxatdan o'ttingiz, batafsil ma'lumot uchun +998953001199 raqamiga qo'ng'iroq qiling!"

    def search(self) -> list:
        data = ""
        send_lst = []
        for i in range(1, 8):
            item = self.cursor.execute(f"""SELECT * FROM '{self.ls[i - 1]}'""")
            data += f"{self.ls[i - 1].upper()}\n"
            for j in item.fetchall():
                data += f"{j}\n"
            send_lst.append(data)
            data = ""
        return send_lst


if __name__ == '__main__':
    f = Function()
    f.tables()
    print(f.search())
