import store_other_mysql

# question, response, time, measurement
# respiration belt, blood pressure, pulse, gsr


# every time this program runs, automatically create 4 table each with a unique ID you can refer to
# e.g. Respiration0, BP0, Pulse0, GSR0 table will be created at first
# the next time this program runs, we'll have Respiration1, BP1, Pulse1, GSR1 table created in MySQL


# you want to first find an available id, if found -> create the new table for you -> save this id number for your program
# ALWAYS refer to "Respiration0" when using find_available_id(), it will find the id available for you and create the 4 table for you
store_other_mysql.find_available_id('Respiration0')
# current_table_id REQUIRED. This tells us the id of the table we're currently at
current_table_id = store_other_mysql.get_table_number()
print(current_table_id)
print("\n")

# here is how you would insert respiration data
store_other_mysql.Respiration_insert('Respiration'+str(current_table_id), 'age', 'yes', 0.5, 6.8)

# here is how you would insert blood pressure data
store_other_mysql.BP_insert('BP'+str(current_table_id), 'age', 'yes', 1.5, 9.3)

# here is how you would insert pulse data
store_other_mysql.Pulse_insert('Pulse'+str(current_table_id), 'age', 'yes', 2.0, 8.9)

# here is how you would insert gsr data
store_other_mysql.GSR_insert('GSR'+str(current_table_id), 'age', 'yes', 4.0, 5.3)


# here is how you would see the current attributes of Respiration table
store_other_mysql.desc_table('Respiration'+str(current_table_id))
print("\n")

# here is how you would see all the contents in Respiration
store_other_mysql.show_table('Respiration'+str(current_table_id))
print("\n")

# here is how you would see all the contents in BP
store_other_mysql.show_table('BP'+str(current_table_id))
print("\n")

# here is how you would see all the contents in Pulse
store_other_mysql.show_table('Pulse'+str(current_table_id))
print("\n")

# here is how you would see all the contents in GSR
store_other_mysql.show_table('GSR'+str(current_table_id))
print("\n")


# here is how you would see all the tables created so far in Questions database
print("Existing tables in Questions database:")
store_other_mysql.show_all_tables()