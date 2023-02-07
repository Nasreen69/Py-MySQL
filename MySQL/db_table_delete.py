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

#DELETE FROM TABLE_NAME WHERE ATTRIBUTE_NAME = ATTRIBUTE_VALUE
#run cmd - mysql> SELECT * FROM employee;
query = "DELETE FROM Employee WHERE NAME = 'Nashu'"

cursorObject.execute(query)
   
dataBase.commit()
 
# disconnecting from server
dataBase.close()
