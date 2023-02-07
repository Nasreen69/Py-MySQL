# importing required libraries
import mysql.connector as c

dataBase = c.connect(
                        host ="localhost",
                        user ="root",
                        passwd ="N@sreen61",
                        database = "NASHU"
                    )

if dataBase.is_connected():
         print("Successfully Connected...")


dataBase.close()
