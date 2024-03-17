###### THIS ONE WORKS FOR CSIL WINDOWS
###### VSCODE CONNECT TO SQL SERVER
###### DATABASE CYPRESS.CSIL.SFU.CA


import time
import datetime
import pypyodbc










# MAIN MENU FUNCTION
def main_menu():
    print("\n")
    print("Main Menu (Logged In User)")
    print("------------------------------")
    print("1. Search Business")
    print("2. Search Users")
    print("3. Make Friend")
    print("4. Review Business")
    print("5. Logout")
    print("------------------------------")
    choice = input("Enter your choice (1-5): ")
    print("\n")
    time.sleep(0.75)
    return choice










# LOGIN FUNCTION
def login():
    connection = pypyodbc.connect(r'Driver={SQL Server}; Server=cypress.csil.sfu.ca; Database=msa316354; uid=s_msa316; pwd=rHrqY67LG3j3YPNj')
    cursor = connection.cursor() 
    
    print('LOG IN')
    user_id = input("Enter your user ID: ")
    # check user id validity
    cursor.execute("SELECT user_id, name FROM user_yelp")
    result = cursor.fetchone()
        
    while result:      
        db_user_id = str(result[0]).strip()
        if user_id == db_user_id: 
            cursor.close()
            connection.close()
            user_name = str(result[1]).strip()
            print('\n')
            print(f"Welcome, {user_name} (ID: {user_id})! You are now logged in!")
            time.sleep(0.75)
            return user_id
        else:
            result = cursor.fetchone()

    cursor.close()
    connection.close()
    print("\nInvalid user ID. Please try again.\n")
    time.sleep(0.75)
    return None










# SEARCH BUSINESS FUNCTION
def search_business():
    minimumstars = float(0)
    city = None
    name = None
    ordering = None


    # SET FILTER
    def set_filters():
        print('SET FILTER')
        minimumstars = input("Enter minumum number of stars (leave blank for any): ")
        if minimumstars == '':
            minimumstars = float(0)
        elif minimumstars in ['1', '2', '3', '4', '5']:
            minimumstars = float(minimumstars)
        else:
            print('Invalid choice for the minimum stars. Enter a number between 1-5.')
            time.sleep(0.75)
            set_filters()
        city = input("Enter city (leave blank for any): ").strip().title()
        name = input("Enter business name or part of the name (leave blank for any): ").strip().title()
        time.sleep(0.5)
        print("Saving your filters...")
        print("\n")
        time.sleep(0.75)

        if city == '':
            city = None
        if name == '':
            name = None
        #search_business_menu()
        return minimumstars, city, name
    

    # SET ORDERING
    def set_ordering():
        print("SET ORDERING")
        print('Ordering Options:')
        print('1. By Name')
        print('2. By City')
        print('3. By Number of stars')
        print("------------------------------------------------------------")
        ordering = input("Enter your order choice (1-3) (leave blank for default): ")
        time.sleep(0.5)
        print("Saving your ordering...")
        print("\n")
        time.sleep(0.75)

        if ordering == '1':
            return 'name'
        elif ordering == '2':
            return 'city'
        elif ordering == '3':
            return 'stars'
        elif ordering == '':
            return None
        else:
            print("Invalid choice. Enter a number between 1-3.")
            time.sleep(0.75)
            set_ordering()

    
    # DISPLAY SEARCH RESULTS
    def search_results(minimumstars, city, name, ordering):
        connection = pypyodbc.connect(r'Driver={SQL Server}; Server=cypress.csil.sfu.ca; Database=msa316354; uid=s_msa316; pwd=rHrqY67LG3j3YPNj')
        cursor = connection.cursor() 
        SQLquery = f"SELECT business_id, name, address, city, stars FROM business WHERE stars >= '{minimumstars}'"

        if name:
            SQLquery += f" AND name = '{name}'"
        if city:
            SQLquery += f" AND city = '{city}'"
        if ordering:
            SQLquery += f" ORDER BY {ordering}"
        elif ordering == None:
            SQLquery += f" ORDER BY business_id"
        cursor.execute(SQLquery)
        results = cursor.fetchall()

        if results:
            print("\nSEARCH RESULTS:")
            for row in results:
                business_id, bus_name, address, bus_city, bus_stars = row
                print("-------------------------")
                print(f"ID: {business_id} \nName: {bus_name} \nAddress: {address} \nCity: {bus_city} \nStars: {bus_stars}")
            print("-------------------------")
            print('\n')
            time.sleep(0.75)
        else:
            print("No businesses found that matches your filters and ordering.")
            print("\n")
            time.sleep(0.75)
        cursor.close()
        connection.close()
        

    # MENU
    def search_business_menu():
        print("\n'Search Business' Menu")
        print("------------------------------------------------------------")
        print('1. Set Filters')
        print("      Current Filters: ")
        print(f"      Minimum stars = [ {minimumstars} ], City = [ {city} ], Name = [ {name} ]")
        print('2. Set Ordering')
        print(f"      Current Ordering: [{ordering}]")
        print('3. Display Search Results')
        print('4. Exit to Main Menu')
        print("------------------------------------------------------------")
        searchbus_choice = input("Enter Your Choice (1-4): ")
        print("\n")
        time.sleep(0.75)
        return searchbus_choice

    
    # MAIN
    while True:
        searchbus_choice = search_business_menu()
        if searchbus_choice == '1':
            minimumstars, city, name = set_filters()
        elif searchbus_choice == '2':
            ordering = set_ordering()
        elif searchbus_choice == '3':
            search_results(minimumstars, city, name, ordering)
        elif searchbus_choice == '4':
            break
        else:
            print("Invalid choice. Enter a number between 1-4.")
            print("\n")
            time.sleep(0.75)

    









# SEARCH USERS FUNCTION
def search_users():
    user_name = None
    min_reviewcount = int(0)
    min_avgstars = float(0)


    # SET FILTER
    def set_filter():
        print('SET FILTER')
        user_name = input("Enter user's name or part of the name (leave blank for any): ").strip().title()
        min_reviewcount = int(input("Enter minimum review count: "))
        min_avgstars = float(input("Enter minumum average stars: "))
        time.sleep(0.5)
        print("Saving your filters...")
        print("\n")
        time.sleep(0.75)

        if user_name == '':
            user_name = None
        if min_reviewcount == '':
            min_reviewcount = int(0)
        if min_avgstars == '':
            min_avgstars = float(0)
        return user_name, min_reviewcount, min_avgstars
    

    # DISPLAY SEARCH RESULTS
    def search_results(user_name, min_reviewcount, min_avgstars): 
        connection = pypyodbc.connect(r'Driver={SQL Server}; Server=cypress.csil.sfu.ca; Database=msa316354; uid=s_msa316; pwd=rHrqY67LG3j3YPNj')
        cursor = connection.cursor() 
        SQLquery = f"SELECT user_id, name, review_count, useful, funny, cool, average_stars, yelping_since " \
                f"FROM user_yelp " \
                f"WHERE review_count >= {min_reviewcount} AND average_stars >= {min_avgstars}"
        
        if user_name:
            SQLquery += f" AND name LIKE '%{user_name}%'"
        SQLquery += f"ORDER by name"
        cursor.execute(SQLquery)
        results = cursor.fetchall()

        if results:
            print("\nSEARCH RESULTS:")
            for row in results:
                user_id, username, reviewcount, useful, funny, cool, avgstars, yelpingsince = row
                print("-------------------------")
                print(f"ID: {user_id} \nName: {username} \nReview Count: {reviewcount} \nUseful: {useful} \nFunny: {funny} "
                      f"\nCool: {cool} \nAverage Stars: {avgstars} \nDate Registered At Yelp = {yelpingsince}")
            print("-------------------------")
            print('\n')
            time.sleep(0.75)
            cursor.close()
            connection.close()
            return results
        else:
            print("No users found that matches your filters.")
            print('\n')
            time.sleep(0.75)
            cursor.close()
            connection.close()
            return None


    # MENU
    def search_user_menu():
        print("\n'Search Users' Menu")
        print("------------------------------------------------------------")
        print('1. Set Filters')
        print("      Current Filters: ")
        print(f"      Name = [ {user_name} ], Minimum Review Count = [ {min_reviewcount} ], Minimum Average Stars = [ {min_avgstars} ]")
        print('2. Display Search Results')
        print('3. Exit to Main Menu')
        print("------------------------------------------------------------")
        searchuser_choice = input("Enter Your Choice (1-3): ")
        print("\n")
        time.sleep(0.75)
        return searchuser_choice

    
    # MAIN
    while True:
        searchuser_choice = search_user_menu()
        if searchuser_choice == '1':
            user_name, min_reviewcount, min_avgstars = set_filter()
        elif searchuser_choice == '2':
            search_results(user_name, min_reviewcount, min_avgstars)
        elif searchuser_choice == '3':
            break
        else:
            print("Invalid choice. Enter a number between 1-3.")
            print("\n")
            time.sleep(0.75)
        
    

        






# MAKE FRIEND FUNCTION
def make_friend(current_userid):
    search_res = None

    def search_userfriend():
        print('SEARCH USERS TO ADD FRIEND')
        user_name = input("Enter user's name or part of the name (leave blank for any): ").strip().title()
        min_reviewcount = int(input("Enter minimum review count: "))
        min_avgstars = float(input("Enter minumum average stars: "))
        time.sleep(0.5)
        print("Saving your search filters...")
        print("\n")
        time.sleep(0.75)

        if user_name == '':
            user_name = None
        if min_reviewcount == '':
            min_reviewcount = int(0)
        if min_avgstars == '':
            min_avgstars = float(0)
        return user_name, min_reviewcount, min_avgstars


    # DISPLAY SEARCH RESULTS
    def search_friendresults(name, min_reviewcount, min_avgstars): 
        connection = pypyodbc.connect(r'Driver={SQL Server}; Server=cypress.csil.sfu.ca; Database=msa316354; uid=s_msa316; pwd=rHrqY67LG3j3YPNj')
        cursor = connection.cursor() 
        SQLquery = f"SELECT user_id, name, review_count, useful, funny, cool, average_stars, yelping_since " \
                f"FROM user_yelp " \
                f"WHERE review_count >= {min_reviewcount} AND average_stars >= {min_avgstars}"
        
        if user_name:
            SQLquery += f" AND name LIKE '%{name}%'"
        SQLquery += f"ORDER by name"
        cursor.execute(SQLquery)
        results = cursor.fetchall()

        if results:
            print("\nSEARCH RESULTS:")
            for row in results:
                user_id, username, reviewcount, useful, funny, cool, avgstars, yelpingsince = row
                print("-------------------------")
                print(f"ID: {user_id} \nName: {username} \nReview Count: {reviewcount} \nUseful: {useful} \nFunny: {funny} "
                      f"\nCool: {cool} \nAverage Stars: {avgstars} \nDate Registered At Yelp = {yelpingsince}")
            print("-------------------------")
            print('\n')
            time.sleep(0.75)
            cursor.close()
            connection.close()
            return results
        else:
            print("No users found that matches your filters.")
            print('\n')
            time.sleep(0.75)
            cursor.close()
            connection.close()
            return None
        

    # ADD FRIEND
    def add_friend(current_userid, search_res):
        if search_res:
            friend_userid = input("Enter the user ID of the user you would like to add as a friend: ")
            if any(friend_userid == res[0] for res in search_res):
                connection = pypyodbc.connect(r'Driver={SQL Server}; Server=cypress.csil.sfu.ca; Database=msa316354; uid=s_msa316; pwd=rHrqY67LG3j3YPNj')
                cursor = connection.cursor() 
                SQLquery1 = f"select * from friendship WHERE friendship.user_id ='{current_userid}' and friendship.friend = '{friend_userid}'"
                cursor.execute(SQLquery1)
                res = cursor.fetchone()
                if res:
                    time.sleep(0.5)
                    print(f"You are already friends with (user ID: {friend_userid})")
                    print('\n')
                    time.sleep(0.75)
                    cursor.close()
                    connection.close()
                else:
                    SQLquery2 = f"INSERT INTO friendship(user_id, friend) VALUES(?, ?)"
                    vals = (current_userid, friend_userid)
                    cursor.execute(SQLquery2, vals)
                    connection.commit()
                    time.sleep(0.5)
                    print("Adding Friend...")
                    time.sleep(0.5)
                    print(f"Friendship added with (user ID: {friend_userid})!")
                    print('\n')
                    time.sleep(0.75)
                    cursor.close()
                    connection.close()
            else:
                time.sleep(0.5)
                print("Invalid user ID. Enter a user ID from your user search results.")
                print('\n')
                time.sleep(0.75)
        else:
            print("Search for users and display results (to see available users to add) before adding a friend.")
            print('\n')
            time.sleep(0.75)


    # MENU
    def make_friend_menu():
        print("\n'Make Friend' Menu")
        print("------------------------------------------------------------")
        print("1. Search Users")
        print("2. Display Search Results")
        print("3. Add Friend")
        print("4. Exit to Main Menu")
        print("------------------------------------------------------------")
        makefriend_choice = input("Enter your choice (1-4): ")
        print("\n")
        time.sleep(0.75)
        return makefriend_choice
    

    # MAIN
    while True:
        makefriend_choice = make_friend_menu()
        if makefriend_choice == '1':
            user_name, min_reviewcount, min_avgstars = search_userfriend()
        elif makefriend_choice == '2':
            search_res = search_friendresults(user_name, min_reviewcount, min_avgstars)
        elif makefriend_choice == '3':
            add_friend(current_userid, search_res)
        elif makefriend_choice == '4':
            break
        else:
            print("Invalid choice. Enter a number between 1-4.")
            print("\n")
            time.sleep(0.75)

            








# REVIEW BUSINESS FUNCTION
def review_business(user_id):
    business_id = None
    business_name = None
    stars = None

    def enter_businessid():
        print('ENTER BUSINESS ID')
        businessid = input("Enter the business ID for the business you want to review: ").strip()
        # check if business exists
        connection = pypyodbc.connect(r'Driver={SQL Server}; Server=cypress.csil.sfu.ca; Database=msa316354; uid=s_msa316; pwd=rHrqY67LG3j3YPNj')
        cursor = connection.cursor() 
        SQLquery = f"SELECT * FROM business WHERE business_id = '{businessid}'"
        cursor.execute(SQLquery)
        res = cursor.fetchone()
        businessname = res[1]
        time.sleep(0.5)
        if res:
            print("Business found.")
            print('\n')
            cursor.close()
            connection.close()
            return businessid, businessname
        else:
            print(f"Business with (ID: {businessid} does not exist. Enter a business ID that exists.")
            print("\n")
            time.sleep(0.75)
            cursor.close()
            connection.close()
            enter_businessid()

    
    def review_bus():
        print('ENTER REVIEW')
        stars = int(input("Enter the number of stars (1-5) to rate this business: "))
        if 1 <= stars <= 5:
            print("\n")
            time.sleep(0.75)
            return stars
        else:
            print("Invalid choice for star rating. Enter a number between 1-5.")
            print("\n")
            time.sleep(0.75)
            review_bus()


    def record_review(business_id, business_name, stars):
        print("RECORDING REVIEW")
        if business_id and stars:
            connection = pypyodbc.connect(r'Driver={SQL Server}; Server=cypress.csil.sfu.ca; Database=msa316354; uid=s_msa316; pwd=rHrqY67LG3j3YPNj')
            cursor = connection.cursor() 
            dt = datetime.datetime.now()
            date = dt.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
            # generate review id
            curr_dt = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
            concat_userid = user_id[:11]
            userid_date = f"{concat_userid}{curr_dt}"
            review_id = userid_date[:22]
            SQLquery = f"INSERT INTO review (review_id, user_id, business_id, stars, date) " \
                       f"VALUES (?, ?, ?, ?, ?)"
            vals = (review_id, user_id, business_id, stars, date)
            cursor.execute(SQLquery, vals)
            connection.commit()
            print(f'Your review for ({business_name}) has been recorded. You rated it ({stars}) stars.')
            print("\n")
            time.sleep(0.75)
            cursor.close()
            connection.close()
        else:
            time.sleep(0.5)
            print('Enter business ID and review business before recording the review for the business.')
            print("\n")
            time.sleep(0.75)


    # MENU
    def review_business_menu():
        print("\n'Review Business' Menu")
        print("------------------------------------------------------------")
        print("1. Search Business ID")
        print("2. Review Business")
        print("3. Record Review")
        print("4. Exit to Main Menu")
        print("------------------------------------------------------------")
        makefriend_choice = input("Enter your choice (1-4): ")
        print("\n")
        time.sleep(0.75)
        return makefriend_choice
    

    # MAIN
    while True:
        reviewbusiness_choice = review_business_menu()
        if reviewbusiness_choice == '1':
            business_id, business_name = enter_businessid()
        elif reviewbusiness_choice == '2':
            stars = review_bus()
        elif reviewbusiness_choice == '3':
            record_review(business_id, business_name, stars)
        elif reviewbusiness_choice == '4':
            break
        else:
            print("Invalid choice. Enter a number between 1-4.")
            print("\n")
            time.sleep(0.75)











# LOGOUT FUNCTION
def logout():
    current_user = None
    print('Logging you out...')
    time.sleep(0.75)
    print('Goodbye!\n')
    time.sleep(0.75)










# main program
def main():
    current_userid = None

    while True:
        if current_userid is None:
            current_userid = login()
        else:
            choice = main_menu()

            if choice == '1':
                search_business()
            elif choice == '2':
                search_users()
            elif choice == '3':
                make_friend(current_userid)
            elif choice == '4':
                review_business(current_userid)
            elif choice == '5':
                logout()
                current_userid = None
            else:
                print('\n')
                print("Invalid choice. Enter a number between 1-5.")
                time.sleep(0.75)
if __name__ == "__main__":
    main()
