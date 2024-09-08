

import mysql.connector
from datetime import date
todays_date = date.today()
print(todays_date)
print(type(str(todays_date)))
flag = False

dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  password ="",
  database = "ai_gym"
)

curr = dataBase.cursor()
# query = "insert into deadlift (date, sets, reps) values (%s, %s, %s)"
# values = (todays_date, 2, 8)
# curr.execute(query, values)
# dataBase.commit()
######
# query = "select sets, reps from bicep where date = '2024-04-11'"
# curr.execute(query)
# results = curr.fetchall()
# print(results)
#####
# query = "select DATE(date) from bicep"
# curr.execute(query)
# results = curr.fetchone()
# print(results)
# if todays_date in results:
#   print(True)
  
# def fetch():
#   dataBase = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "",
#     database = "ai_gym"
#   )
#   cursor = dataBase.cursor()
#   query = "select sets from bicep order by bicep_id  desc limit 1"
#   cursor.execute(query)
#   results = cursor.fetchall()
#   print(results)
#   data = results[0][0]
#   print(data)
#   return data
# fetch()

def add(new_sets):
  dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "ai_gym"
  )
  cursor = dataBase.cursor()
  query = "insert into deadlift (date, sets, reps) values (%s, %s, %s)"
  values = (todays_date, new_sets, 15)
  cursor.execute(query, values)
  dataBase.commit()
  cursor.close()
  dataBase.close()

query = "select * from deadlift order by deadlift_id desc limit 1"
curr.execute(query)
results = curr.fetchall()
print(results)
print(results[0][1])
database_date = results[0][1]
if todays_date == database_date:
  print(True)
  new_sets = (results[0][2]) + 1
  print(new_sets)
  add(new_sets)
else:
  print(False)
  new_sets = 1
  add(new_sets)
  
  
