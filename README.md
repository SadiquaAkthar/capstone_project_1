# capstone_project_1
Introduction
This Python program utilizes the Selenium WebDriver library to automate testing scenarios for an OrangeHRM web application. The tests cover various functionalities, including successful and invalid employee logins, adding a new employee in the PIM module, editing an existing employee's details, and deleting an existing employee.

Prerequisites
Python installed on your system
Selenium library installed (pip install selenium)
Web browser driver (Chrome driver in this case) compatible with your browser installed and available in the system's PATH.
Usage
Clone the repository or download the script.
Install the required libraries by running pip install selenium.
Download the appropriate web driver (e.g., ChromeDriver) and ensure it's in the system's PATH.
Open the script and modify the data and locators files based on your application's specifics.
Run the script by executing the test_main() function in the script.
Structure
Project Class: Initializes a Selenium WebDriver and contains methods for different test cases.
Test Cases:
TC_Login_01_successful_login: Tests a successful employee login.
TC_Login_02_invalid_login: Tests an invalid employee login.
TC_PIM_01_add_new_employee: Adds a new employee in the PIM module.
TC_PIM_02_edit_existing_employee: Edits an existing employee's details in the PIM module.
TC_PIM_03_delete_existing_employee: Deletes an existing employee in the PIM module.

Run the tests using the command: 
------------------------------------------------------------
python -m pytest main.py

Note
Make sure to update the data and locators files according to your application's structure.
Adjust the web driver and browser choice in the webdriver.Chrome() initialization if needed.
Customize the test cases as per your application's behavior.
