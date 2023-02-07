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

#SELECT NAME,COMPANY FROM Employee ORDER BY NAME ASC|DESC;
#query = "SELECT * FROM Employee ORDER BY NAME DESC'
query = "SELECT * FROM Employee ORDER BY NAME ASC"

cursorObject.execute(query)
   
myresult = cursorObject.fetchall()
   
for x in myresult:
    print(x)
 
# disconnecting from server
dataBase.close()
