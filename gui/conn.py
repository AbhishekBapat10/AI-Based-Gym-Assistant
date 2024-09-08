import mysql.connector

dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  password ="",
  database = "ai_gym"
)
cursor = dataBase.cursor()

# sql = "INSERT INTO task (flag) VALUES (%s)"
# val = ("stop",)
#
# cursor.execute(sql, val)
# dataBase.commit()
#
if __name__ == "__main__":
  import time
  
  while True:
  
  
    connection = mysql.connector.connect(
      host = "localhost",
      user = "root",
      password = "",
      database = "ai_gym"
    )
    curr = connection.cursor()
    
    
    flag = False
    try:
      # Execute the query to fetch the latest flag
      query = "SELECT flag FROM task ORDER BY id DESC LIMIT 1"
      curr.execute(query)
      result = curr.fetchone()  # Fetch only the latest row
      
      if result:
        latest_flag = result[0]
        print("Latest flag from database:", latest_flag)
        
        # Check if the flag is 'stop'
        if latest_flag == "stop":
          print("Stop command received. Exiting loop.")
          flag = True
    
    except Exception as e:
      # Handle any errors that may occur during database operations
      print("Error:", e)
    
    if flag:
      break
    
    # Add a delay to avoid excessive resource consumption
    connection.close()
    time.sleep(1)



