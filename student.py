from mysql import connector

class studentdatamanagement:
    def __init__(self):
        self.connection = connector.connect(
            host="localhost",
            user="root",
            password="Rithumary@1234",
            database="students"
        )

        print("Connected successfully....")
    def get_object(self,id=None):
        try:
            self.cursor=self.connection.cursor()
            query="select * from students_data where id=%s"
            values=(id,)
            self.cursor.execute(query,values)
            records=self.cursor.fetchall()
            return records
        except Exception as e:
            return e
    def post(self, **kwargs):
        try:
            self.cursor = self.connection.cursor()

            query = """
                INSERT INTO students_data
                (name, department, place, age, phone_number)
                VALUES (%s, %s, %s, %s, %s)
            """

            values = [v for v in kwargs.values()]

            self.cursor.execute(query, values)
            self.connection.commit()

            print("student data added successfully..")

        except Exception as e:
            print("Error:", e)
    def get(self):
        try:
            self.cursor=self.connection.cursor()
            query="select * from students_data"
            self.cursor.execute(query)
            records=self.cursor.fetchall()
            print("\n........students details...........")
            for data in records:
                print(data)
        except Exception as e:
            print("Error:",e)
    def retrieve(self,id=None):
        try:
            self.cursor=self.connection.cursor()
            query="select * from students_data where id=%s"
            values=(id,)
            self.cursor.execute(query,values)
            records=self.cursor.fetchone()
            print("\nThe required student data.....")
            print(records)
        except Exception as e:
            print(e)
    def put(self,id=None,**kwargs):
        try:
            records=self.get_object(id=id)
            if records!=None:
                self.cursor=self.connection.cursor()
                placeholder=""
                for k in kwargs.keys():
                    placeholder+=k+"=%s, "
                placeholder=placeholder.rstrip(", ")
                query=f"update students_data set {placeholder} where id=%s"
                values = [v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query, values)
                records = self.cursor.fetchone()
                print("\nThe data is updated successfully.....")
            else:
                print("student details not updated")
        except Exception as e:
            print(e)
    def delete(self,id=None):
        try:
            self.cursor=self.connection.cursor()
            query="delete from students_data where id=%s"
            values=(id,)
            self.cursor.execute(query,values)
            self.connection.commit()
            print("\nThe particular student data is deleted successfully....")
        except Exception as e:
            print(e)

students_data=studentdatamanagement()
# students_data.post(
#     name="Rithu",
#     department="CSE",
#     place="Thrissur",
#     age=21,
#     phone_number="835783467"
# )
#
# students_data.post(
#     name="Anjana",
#     department="CSE",
#     place="Thrissur",
#     age=21,
#     phone_number="86758867"
# )
#
#
#
# students_data.post(
#     name="Sana",
#     department="AIML",
#     place="Aluva",
#     age=21,
#     phone_number="9765583467"
# )

students_data.get()

students_data.retrieve(2)

students_data.put(id=1,age=22)
students_data.get()

students_data.delete(3)
students_data.get()
