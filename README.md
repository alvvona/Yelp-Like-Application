# Yelp-Like-Application

README  |  CMPT 354  |  Assignment 7
Author: MeiQi Shen (301475575)


Introduction:
	This python program is a terminal-based Yelp-like application that allows users to interact with a SQL Server database. Users can log in, search for businesses, search for other users, make friends, and review businesses. The structure of this application is heirarical menus that jump into the various menus. Users can enter submenus from the main menu as well as exit out of a submenu back to the main menu. 


Prerequisites:
	To run the application, ensure the following are installed:
	- Python
	- pypyodbc (run 'pip install pypyodbc' in terminal)
	- SQL Server
	- Access to the SQL Server


How to Run
1. Execute the .py file in a Python environment (vscode works)
2. The .py file app will prompt you to log in by entering a valid user ID
3. The main menu will show up, providing 4 functions and a logout option
	- the 4 functions are search_business, search_user, make_friend, review_business
4. Choose the logout option when you are finished with using the app


Functions/Features
1. Search Business
	- (option 1) Users can set filters such as minimum stars, city, and business name
	- (option 2) Users can set the ordering of results by name, city, or number of stars
	- (option 3) Results are displayed with business details
	- (option 4) Exit to main menu
2. Search Users
	- (option 1) Users can set filters such as name, minimum review count, and minimum average stars
	- (option 2) Results are displayed with user details and ordered by name
	- (option 3) Exit to main menu
3. Make Friend
	- (option 1) Users can set filters such as name, minimum review count, and minimum average stars
	- (option 2) Results are displayed with business details
	- (option 3) Users can add a friend by entering the user ID of the user they wish to befriend
	- (option 4) Exit to main menu
4. Review Business
	- (option 1) Users can search up the business ID they wish to review
	- (option 2) Users can provide a star rating for their review of the business they selected
	- (option 3) Reviews are recorded in the database
	- (option 4) Exit to main menu
5. Logout
	- Choosing this will log the user out, user will have to log back in to have access to the main menu
