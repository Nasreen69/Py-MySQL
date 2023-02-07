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

# creating table
Employee_JD = """CREATE TABLE Employee(
				NAME     VARCHAR(20) NOT NULL,
				COMPANY  VARCHAR(50),
				SALARY   INT        NOT NULL,
				SKILLS   VARCHAR(5),
				AGE      INT
				)"""

# table created
cursorObject.execute(Employee_JD)

# disconnecting from server
dataBase.close()
