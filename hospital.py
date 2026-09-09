from mysql import connector

# CONNECTING PYTHON TO MYSQL......

class hospital_management:
    def __init__(self):
        self.connection = connector.connect(
            host="localhost",
            user="root",
            password="Rithumary@1234",
            database="hospital"
        )
        print("Connected successfully....")

#CHECKING THE EXSISTENCE OF PARTICULAR DATA USING GET_OBJECT METHOD.................................................................

    def get_object(self,id=None):
        try:
            self.cursor=self.connection.cursor()
            query="select * from doctors_data where id=%s"
            values=(id,)
            self.cursor.execute(query,values)
            records=self.cursor.fetchone()
            return records
        except Exception as e:
            return None

#INSERTING DOCTORS_DATA USING POST OPERATION.....

    def post(self,**kwargs):
        try:
            self.cursor=self.connection.cursor()
            query="""
            insert into doctors_data
            (id,name,department,mobile_number,place)
            values(%s,%s,%s,%s,%s)
            """
            values=[v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.connection.commit()
            print("doctors data inserted succesfully......")
        except Exception as e:
            print("Error:",e)

#DISPLAYING ALL DATA................

    def get(self):
        try:
            self.cursor=self.connection.cursor()
            query="select * from doctors_data"
            self.cursor.execute(query)
            records=self.cursor.fetchall()
            if records:
                print("...........Display all doctors data..........")
                for data in records:
                    print(data)
            else:
                print("No doctors data found.....")
        except Exception as e:
            print("Error:",e)

#DISPLAY ONE DATA AT A TIME USING RETRIEVE OPERATION...........

    def retrieve(self,id=None):
        try:
            self.cursor=self.connection.cursor()
            query="select * from doctors_data where id=%s"
            values=(id,)
            self.cursor.execute(query,values)
            records=self.cursor.fetchone()
            if records:
                print("\n......Enquired doctors details.....")
                print(records)
            else:
                print("That doctors data is not found...")
        except Exception as e:
            print("Error:",e)

#DELETING DATA USING DELETE OPERATION.....................................................

    def delete(self,id=None):
        try:
            self.cursor=self.connection.cursor()
            query="select * from doctors_data where id=%s"
            values=(id,)
            self.cursor.execute(query,values)
            records=self.cursor.fetchone()
            if records:
                print("......The specific doctors data is removed succesfully.....")
                query="delete from doctors_data where id=%s"
                self.cursor.execute(query,values)
                self.connection.commit()
                records=self.cursor.fetchone()
            else:
                print("That doctors data is not found.....")
        except Exception as e:
            print("Error:",e)

#UPDATING THE DATA USING PUT OPERATION..................................................................................

    def put(self,id=None,**kwargs):
        try:
            records=self.get_object(id=id)
            if records!=None:
                self.cursor=self.connection.cursor()
                placeholder=""
                for k in kwargs.keys():
                    placeholder+=k+"=%s ,"
                    placeholder=placeholder.rstrip(", ")
                    query=f"update doctors_data set {placeholder} where id=%s"
                    values=[v for v in kwargs.values()]
                    values.append(id)
                    self.cursor.execute(query,values)
                    self.connection.commit()
                    records=self.cursor.fetchall()
                    print("Updation of doctors data is succesfull........")
            else:
                print("That doctors data is not found......")
        except Exception as e:
            print("Error:",e)







obj=hospital_management()

# obj.post(id=30,name="Giju Baby",department="Cardiology",mobile_number=814293756,place="Kunnamkulam")
# obj.post(id=31,name="Rahul Raj",department="Orthopedics",mobile_number=8765432109,place="Kochi")
# obj.post(id=32,name="Meera Joseph",department="Pediatrics",mobile_number=7654321098,place="Ernakulam")
# obj.post(id=33,name="Arjun Kumar",department="Dermatology",mobile_number=9988776655,place="Calicut")
# obj.post(id=34,name="Sneha Maria",department="Gynecology",mobile_number=8899776655,place="Kottayam")
# obj.post(id=35,name="Vishnu Prasad",department="Cardiology",mobile_number=7788665544,place="Palakkad")
# obj.post(id=46,name="Amal George",department="ENT",mobile_number=9090909090,place="Alappuzha")
# obj.post(id=47,name="Diya Mathew",department="General Medicine",mobile_number=8123456789,place="Chalakudy")

obj.get()

obj.retrieve(40)

obj.delete(41)
obj.get()

obj.put(id=37,place="Kannur")
obj.get()






