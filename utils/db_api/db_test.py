import sqlite3

# #Define the connection
# connection = sqlite3.connect("art_user.db")


# #Cursor
# cursor = connection.cursor()

# # Create Tables

# command1 = """CREATE TABLE IF NOT EXISTS users_art(user_id INTEGER PRIMARY KEY, username TEXT)"""

# cursor.execute(command1)


# # Adding Elements
# cursor.execute("INSERT INTO users_art VALUES (20050921, '@ai_junior1')")
# cursor.execute("INSERT INTO users_art VALUES (20055920, '@ai_junior3')")
# cursor.execute("INSERT INTO users_art VALUES (20052156, '@ai_junior2')")


# # get  results

# cursor.execute("SELECT user_id FROM users_art")

# results = cursor.fetchall()
# print(results)

def send_ex(command):
	connection = sqlite3.connect("art_user.db")
	cursor = connection.cursor()
	cursor.execute(command)
	res = cursor.fetchall()
	connection.commit()
	cursor.close()
	connection.close()
	return res


# send_ex("CREATE TABLE IF NOT EXISTS users_art(user_id INTEGER PRIMARY KEY, username TEXT)")

# print(send_ex("INSERT INTO users_art (user_id, username) VALUES (22222, '@ai_junior')"))
# send_ex("DELETE FROM users_art WHERE user_id = 22222")
# print("success")

