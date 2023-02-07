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

sql = "INSERT INTO Employee(NAME, COMPANY, SALARY, SKILLS, AGE)\
VALUES (%s, %s, %s, %s, %s)"
val = ("Nashu", "Oracle", "110000", "AIML", "26")

cursorObject.execute(sql, val)
dataBase.commit()

# disconnecting from server
dataBase.close()
