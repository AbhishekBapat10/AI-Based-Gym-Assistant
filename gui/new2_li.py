
import mysql.connector




dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  password ="",
  database = "ai_gym"
)
li = []
curr = dataBase.cursor()
query = "select sets, reps, accuracy from bicep;"
curr.execute(query)
results = curr.fetchall()
li.append(data[0] for data in results)
print(li)