from asyncio.windows_events import NULL
import mysql.connector
import sqlite3
import random
print('===========================\n','Authorize connection access')
a_pass = input(' Enter password: ')
mydb = mysql.connector.connect(host="localhost", 
user="root", 
password = a_pass, 
auth_plugin = a_pass, 
database="netflix")
print('===========================\n')
print(mydb)

# TODO: Clarisse 
# select query based on filter 
# create a new record 
# delete records 
# update records 

mycursor = mydb.cursor(buffered=True)
#create DB 
#UNCOMMENT: create the DB 
# mycursor.execute("CREATE SCHEMA Netflix;")
#UNCOMMENT: show the database that exist in my local mySQL 
mycursor.execute("SHOW DATABASES")
for x in mycursor: 
    print("Show DB: ", x)
#UNCOMMENT: if you need to create the table 

#====DROP TABLES=====================================================================================
#drop user 
#drop records 
# drop_records = '''DROP TABLE records;'''
# mycursor.execute(drop_records)
#drop user
# drop_user = '''DROP TABLE user;'''
# mycursor.execute(drop_user)
#drop user_list 
# drop_user_list = '''DROP TABLE user_list;'''
# mycursor.execute(drop_user_list)
#drop_country 
# drop_country = '''DROP TABLE country;'''
# mycursor.execute(drop_country)
#drop_shows 
# drop_shows = '''DROP TABLE shows;'''
# mycursor.execute(drop_shows)
# #drop imdb
# drop_imdb = '''DROP TABLE imdb;'''
# mycursor.execute(drop_imdb)
#===============================================================================================

#====CREATING THE TABLES========================================================================
#imdb 
# imdb_query = '''
#         CREATE TABLE imdb(
#            imdb_id INTEGER NOT NULL PRIMARY KEY,
#            score FLOAT 
#         );
#         '''
# mycursor.execute(imdb_query)
# print('imdb Table Created')

# # #shows
# shows_query = '''
#         CREATE TABLE shows(
#            show_ID INTEGER NOT NULL PRIMARY KEY,
#            title VARCHAR(200),
#            description VARCHAR(200), 
#            rating DOUBLE, 
#            im_id INTEGER,
#            FOREIGN KEY (im_id) REFERENCES imdb(imdb_id), 
#            release_year INTEGER,
#            film_location VARCHAR(200), 
#            view_type VARCHAR(20),
#            duration VARCHAR(200)
#         );
#         '''
# mycursor.execute(shows_query)
# print('Shows Table Created')

# #country 
# country_query = '''
#         CREATE TABLE country(
#            country_ID INTEGER NOT NULL PRIMARY KEY,
#            s_ID INTEGER,
#            FOREIGN KEY (s_ID) REFERENCES shows(show_ID), 
#            country_Name VARCHAR(200)
#         );
#         '''
# mycursor.execute(country_query)
# print('Country Table Created')

# # #user_list 
# user_list_query = '''
#     CREATE TABLE user_list(
#         u_listID INTEGER NOT NULL PRIMARY KEY, 
#         s_ID INTEGER, 
#         FOREIGN KEY (s_ID) REFERENCES shows(show_ID)
#     )
# '''
# mycursor.execute(user_list_query)
# print('User_List Table Created')

# # #create the user table 
# user_query = '''
#         CREATE TABLE user(
#             user_ID INTEGER NOT NULL PRIMARY KEY,
#             c_ID INTEGER NOT NULL,
#             FOREIGN KEY (c_ID) REFERENCES country(country_ID), 
#             name VARCHAR(200),
#             ul_ID INTEGER NOT NULL, 
#             FOREIGN KEY(ul_ID) REFERENCES user_list(u_listID),
#             username VARCHAR(20),
#             password VARCHAR(20)
#         );
#         '''
# mycursor.execute(user_query)
# print('User Table Created')

# #Records 
# records_query = '''
#         CREATE TABLE records(
#            login_ID INTEGER NOT NULL PRIMARY KEY,
#            date DATE, 
#            time TIME, 
#            u_ID INTEGER, 
#            FOREIGN KEY (u_id) REFERENCES user(user_id)
#         );
#         '''
# mycursor.execute(records_query)
# print('Records Table Created')
#====================================================================================


#===FUNCTIONS========================================================================
countries = [{1:'United States', 2: 'South Korea', 3: 'United Kingdom'}]
shows = [{4:'The Office', 5: 'Squid Game', 6: 'The Great British Bake Off'}]
u_nameTest = ['bob', 'harry', 'dwight']
user_infoTest = [{'builder':'123', 'potter':'boywholived', 'schrute':'office'}]

#temporary data insert 
def insert_data(): 
    temp_user_data = "INSERT INTO user(user_ID, c_ID, name, ul_ID, username, password) VALUES (%s, %s, %s,%s, %s, %s)" 
    user_vals = [
            (10,1,'bob',14, 'builder', '123'),
            (11,2,'harry',15, 'potter', 'boywholived'),
            (12,3,'dwight',16,'schrute', 'office')]
    temp_uList = "INSERT INTO user_list(u_listID, s_ID) VALUES (%s, %s)" 
    ulist_vals = [
            (14,4),
            (15,5),
            (16,6)]
    temp_country_data = "INSERT INTO country (country_ID,s_ID,country_Name) VALUES (%s, %s, %s)" 
    countries_vals = [
            (1,4,'United States'),
            (2,5,'South Korea'),
            (3,6,'United Kingdom')]
    temp_show_data = "INSERT INTO shows (show_ID,title,description, rating, im_id, release_year, film_location, view_type, duration) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)" 
    show_vals = [
            (4,'Bridgerton','When debutantes are presented at court.', 5.0, 8, 2020, 'London, United Kingdom', 'TV Show', '2 Seasons' ),
            (5,'Squid Game','revolves around 456 heavily debt-ridden people from different age groups and strata of society, who participate in six rounds of various children games to win a humongous sum of money.', 5.0, 9, 2021, 'Daejeon, Korea', 'TV Show', '1 Season'),
            (6,'The Great British Bake Off','search for the best amateur baker by testing skills on cakes, breads, pastries and desserts, crowning a winner after 10 weeks of competition.', 5.0, 10, 2010, 'Down Hall Hotel, United Kingdom', 'TV Show', '11 Seasons')]
    temp_imdb = "INSERT INTO imdb (imdb_id,score) VALUES (%s, %s)" 
    imdb_vals = [
            (8,8.0),
            (9,8.0),
            (10,7.0)]
    mycursor.executemany(temp_imdb,imdb_vals) 
    mycursor.executemany(temp_show_data, show_vals)
    mycursor.executemany(temp_country_data, countries_vals)
    mycursor.executemany(temp_uList, ulist_vals)
    mycursor.executemany(temp_user_data, user_vals)
    mydb.commit()
    print(mycursor.rowcount, "was inserted")

#TODO: loops num of times provided and generates random users 
#def genData(num): 
    #generate a random ID within range of countries 
    #generate a random showsid within shows range 
    #u_id = generate_userID 
    #countryiD  = #generate a random ID within range of countries 
    #name = #generate a random user 
    #username = generate random user name 
    #password = generate random password 
    #newUser 
    #newUser(country, name, username, password )
    #

# function to return the attribute values 
def attributeInformation(query): 
    mycursor.execute(query)
    results = mycursor.fetchall()
    return results

# function to return a single attribute values from table
def single_attribute(query):
    mycursor.execute(query)
    results = mycursor.fetchall()
    results = [i[0] for i in results]
    return results

# get_choice: function checks if user input is correct given a list of choices 
def get_choice(lst):
        choice = input("Enter choice number: ")
        while choice.isdigit() == False:
            print("Incorrect option. Try again")
            choice = input("Enter choice number: ")

        while int(choice) not in lst:
            print("Incorrect option. Try again")
            choice = input("Enter choice number: ")
        return int(choice)
# loginOptions: prompt user to login or create a new account
def loginOptions(): 
    print('Welcome to Netflix But Better')
    print("1 Login\n" \
    "2 New User")
    return get_choice([1,2,3])

# validUser(): validate user 
def validUser(user, password): 
    validUserInfo = False
    query = ''' 
    SELECT username, password 
    FROM user 
    WHERE username = '{u}' and password = '{p}';'''.format(u = user, p = password)
    mycursor.execute(query)
    userInfo = attributeInformation(query)
    print(userInfo)
    print('length: ', len(userInfo))
    if(len(userInfo) != 0): 
          validUserInfo = True
          print('valid user')
    else: 
          print('invalid user credentials')
    return validUserInfo

#return all userIds
def allUserIDs():
    query = '''
    SELECT DISTINCT user_ID  
    FROM user;'''
    #Diagnostic 
    #print("ids in ride: ")
    userIDs = single_attribute(query)
    #show riderIds
    for i in range(len(userIDs)):
        print(i,userIDs[i])
        userIDs[i]
    return userIDs 

def allUlIDs():
    query = '''
    SELECT DISTINCT user_ID  
    FROM user;'''
    ulIDs = single_attribute(query)
    #show riderIds
    for i in range(len(ulIDs)):
        print(i,ulIDs[i])
        ulIDs[i]
    return ulIDs 

def returnCountryID(country): 
    #TODO: handle if it is not a country listed 
    query = '''
    SELECT DISTINCT country_ID 
    FROM country 
    WHERE country_Name = '{c}';''' .format(c = country)
    mycursor.execute(query)
    countryID = single_attribute(query)
    #diagnostic 
    # print(countryID)
    u_countryID = -1
    for i in range(len(countryID)): 
         u_countryID = countryID[i]
        #  print(u_countryID)
    return int(u_countryID)

# generate_userID : generates a new user ID 
def generate_userID(): 
    a = 1 
    b = 1000
    genUserId = random.randint(a,b)
    print('generated user id: ', genUserId)
    l_userIds = allUserIDs()
    #check if the rideID already exists 
    for i in range(len(l_userIds)): 
        if(generate_userID == l_userIds[i]): 
            print('genID matches userID: ', 'generateRideId: ', generate_userID, 'rideId: ', l_userIds[i])
            print('Regenerating a new user_ID: ')
            generate_userID
    #genRideId has no matches 
    return genUserId  

#generates a new ul_ID              
def generate_ul_ID(): 
    a = 1 
    b = 1000
    genUlId = random.randint(a,b)
    print('generated user_list id: ', genUlId)
    l_ulIds = allUlIDs()
    #check if the rideID already exists 
    for i in range(len(l_ulIds)): 
        if(generate_ul_ID == l_ulIds[i]): 
            print('genID matches ulID: ', 'generateUlId: ', generate_ul_ID, 'ul_Id: ', l_ulIds[i])
            print('Regenerating a new ul_ID: ')
            generate_ul_ID
    #genRideId has no matches 
    return genUlId 


# newUser: creates a new user  
def newUser(country, name, user, password): 
    #generate a new user_ID 
    u_id = generate_userID()
    print ('generated new user ID: ', u_id)
    ul_id = generate_ul_ID()
    print('generated new ul ID: ', ul_id)
    #insert ul_id 
    insert_ul_Id(ul_id, None)
    #insert a new user
    query = "INSERT INTO user(user_ID, c_ID, name, ul_ID, username, password) VALUES (%s, %s, %s, %s, %s, %s)"
    new_user_vals = [(u_id, country, name, ul_id, user, password)]
    mycursor.executemany(query, new_user_vals)
    mydb.commit()
    print(mycursor.rowcount, "was inserted")

def insert_ul_Id(u_list_id, s_ID): 
    query = "INSERT INTO user_list(u_listID,s_ID) VALUES (%s, %s)"
    new_ul_vals = [(u_list_id, s_ID)]
    mycursor.executemany(query, new_ul_vals)
    mydb.commit()
    print(mycursor.rowcount, "was inserted")


def menu(): 
    user_choice = loginOptions() 
    if(user_choice == 1): 
        isValidUser = False
        while(isValidUser == False):
            print('Login')
            username = input('Username: ') 
            password = input('Password: ')
            #search if username and password exists
            isValidUser = validUser(username, password) 
            print('isValid: ', isValidUser)
        #welcome user 
        #filter by country
    else: 
        print('Welcome New User')
        name = input('Enter a name: ')
        country = input('What country are you from? ')
        #find the country ID 
        country_id = returnCountryID(country)
        print('country_id: ', country_id)
        username = input('Enter a Username: ')
        password = input('Enter a password: ')
        #creates new user 
        newUser(country_id, name, username, password)


#Populate with test data if there is not data, then display menu

checkCountryEmpty = "SELECT CASE WHEN EXISTS(SELECT * FROM country WHERE 1) THEN 'TRUE' ELSE 'FALSE' END"
# print(mycursor.execute(checkCountryEmpty))
# print(mycursor.execute('SELECT * FROM imdb'))
if(mycursor.execute(checkCountryEmpty)):
    print('loading main menu')
    menu()   
else: 
    #TODO: I don't know why this is not working given the conditiond 
    print('inserting data')
    # insert_data()
    menu()

#TODO: 
    #insert: create record 

    #delete 

    #update 

    #filter by country, show, ... 


#close 
mydb.close()