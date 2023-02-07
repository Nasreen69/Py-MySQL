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

val = [("Yaqoob", "VISA",  "980000",  "SQL", "22"), 
       ("Raheem", "Google","320000",  "Pysql", "50"),
       ("Reshma", "Amazon","310000",  "Git",   "45"),
       ("Nazneen", "HDFC", "240000",  "GCP",   "24")]

cursorObject.executemany(sql, val)
dataBase.commit()

# disconnecting from server
dataBase.close()

