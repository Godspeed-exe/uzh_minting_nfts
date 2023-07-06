from dotenv import load_dotenv
import mysql.connector
import random
import os



def connect_to_db():
    global mydb 
    mydb = mysql.connector.connect(
        host=mysql_host,
        user=mysql_user,
        password=mysql_password,
        database=mysql_database,
        auth_plugin="mysql_native_password"
    )



load_dotenv()
mysql_host = os.getenv('mysql_host')
mysql_user = os.getenv('mysql_user')
mysql_password = os.getenv('mysql_password')
mysql_database = os.getenv('mysql_database')

connect_to_db()
mycursor = mydb.cursor(dictionary=True)
types = ["artist", "astrologer", "blacksmith", "citizen", "herbalist", "hunter", "jeweler"]

number_of_assets = 100

for i in range (1, number_of_assets+1):

    attack = random.randint(1,70)
    speed = random.randint(1,50)
    defense = random.randint(1,80)
    health = random.randint(1,100)
    this_type = random.choice(types)

    sql = "INSERT INTO assets (type, attack, speed, defense, health) VALUES (%s, %s, %s, %s, %s)"
    values = (this_type, attack, speed, defense, health)
    mycursor.execute(sql, values)
    mydb.commit()
    print(f"Inserted asset with ID {i}")