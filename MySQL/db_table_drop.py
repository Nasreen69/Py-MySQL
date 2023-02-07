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

#DROP TABLE tablename;
#DROP TABLE IF EXISTS tablename;
#run cmd - mysql> show tables;
query = "DROP TABLE student;"

cursorObject.execute(query)
   
dataBase.commit()
 
# disconnecting from server
dataBase.close()
