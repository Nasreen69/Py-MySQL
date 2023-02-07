# importing required libraries
import mysql.connector

dataBase = mysql.connector.connect(
                                    host ="localhost",
                                    user ="root",
                                    passwd ="N@sreen61",
                                    database = "pymysql"
                                    )

# preparing a cursor object
cursorObject = dataBase.cursor()

query = "SELECT * FROM Employee where AGE <= 28"
cursorObject.execute(query)
   
myresult = cursorObject.fetchall()
   
for x in myresult:
    print(x)
 
# disconnecting from server
dataBase.close()
