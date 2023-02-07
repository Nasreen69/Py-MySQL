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

#UPDATE tablename SET ="new value" WHERE ="old value";
#run cmd - mysql> SELECT * FROM employee;
query = "UPDATE Employee SET AGE = 22 WHERE Name ='Nashu'"

cursorObject.execute(query)
   
dataBase.commit()
 
# disconnecting from server
dataBase.close()
