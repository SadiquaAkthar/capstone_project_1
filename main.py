from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from Data import data
from Locators import locators
import time
import pytest

class Project:
    # constructor class
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.action = ActionChains(self.driver)
        self.driver.get(data.WebApp_Data().url)
    
    # Successful Employee login to OrangeHRM portal
    def TC_Login_01_successful_login(self):
        try:
            #login using valid credentials
            self.login(data.WebApp_Data().username,data.WebApp_Data().password)

            # Expected Result: Verify that the user is logged in successfully
            assert "dashboard" in self.driver.current_url.lower(), "Login failed!"

            if data.WebApp_Data().dashboard_url in self.driver.current_url:
                 print("PASS : Login success with username {a}".format(a=data.WebApp_Data().username))
                 self.logout()
            elif(data.WebApp_Data().url in self.driver.current_url):
                 print("FAIL : Login failure with username {a}".format(a=data.WebApp_Data().username))
                 self.driver.refresh()

        except NoSuchElementException as selenium_error:
            print(selenium_error)


    # Invalid Employee login to OrangeHRM portal
    def TC_Login_02_invalid_login(self):
        try:
            #login using invalid credentials
            self.login(data.WebApp_Data().username,data.WebApp_Data().invalid_password)

            # Expected Result: Verify that an error message is displayed for invalid credentials
            error_message = self.get_error_message()
            assert "invalid credentials" in error_message.lower(), "Invalid credentials error message not displayed"
            
            #  A valid error message for invalid credentials is displayed.
            if(data.WebApp_Data().url in self.driver.current_url):
                 print("PASS : Login failure with message {a}".format(a=error_message))
                 self.driver.refresh()
            elif data.WebApp_Data().dashboard_url in self.driver.current_url:
                 print("FAIL : Login success with username {a}".format(a=data.WebApp_Data().username))
                 self.logout()        
         
        except NoSuchElementException as selenium_error:
            print(selenium_error)

    # Add a new employee in the PIM module
    def TC_PIM_01_add_new_employee(self):
        try:
            #login using invalid credentials
            self.login(data.WebApp_Data().username,data.WebApp_Data().password)
            wait = WebDriverWait(self.driver, 10)
            
            # Navigate to PIM module
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "PIM"))).click()

            # Add new employee
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Add Employee"))).click()
            
            # Expected Result: Verify that a message for successful employee addition is displayed
            if data.WebApp_Data.add_emp_url in self.driver.current_url:
                success_message= self.fill_emp_details_save()
                assert "successfully saved" in success_message.lower(), "Employee addition failed"
                print("PASS  : A new employee added successfully")   
            else:
                print("FAIL  :New employee not added")                            
            
            self.logout()

        except NoSuchElementException as selenium_error:
            print(selenium_error)

    #Edit an exiting employee in the PIM module.       
    def TC_PIM_02_edit_existing_employee(self):
        try:
            #login using invalid credentials
            self.login(data.WebApp_Data().username,data.WebApp_Data().password)
            wait = WebDriverWait(self.driver, 10)
            edit_Id='//div[text()='+data.WebApp_Data.admin_Id+']'

            # Navigate to PIM module
            self.driver.find_element(By.LINK_TEXT, "PIM").click()
            
            # Edit an existing employee
            wait.until(EC.visibility_of_element_located((By.XPATH,edit_Id))).click()
            self.driver.find_element(By.NAME,"middleName").send_keys("aimy")
            self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button').click()
            
            # Expected Result: Verify that a message for successful employee details edition is displayed
            success_message = self.driver.find_element(By.XPATH,'//*[@id="oxd-toaster_1"]/div/div[1]/div[2]/p[2]').text
            assert "successfully updated" in success_message.lower(), "Employee details edition failed"
            if success_message.lower() in "successfully updated":
                print("PASS : Successfully updated")
            else:
                print("FAIL  : Not updated")

            self.logout()
        
        except NoSuchElementException as selenium_error:
            print(selenium_error)

     #Delete an exiting employee in the PIM module.       
    def TC_PIM_03_delete_existing_employee(self):

        #login
        self.login(data.WebApp_Data().username,data.WebApp_Data().password)
        
        # Navigate to PIM module
        self.driver.find_element(By.LINK_TEXT,"PIM").click()
        self.driver.find_element(By.LINK_TEXT, "Employee List").click()
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input').send_keys("0038")
        self.driver.implicitly_wait(5) 
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[1]/div/div/label/span/i').click()
        
        # Delete an existing employee with id
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[2]/div/div/button').click()
        time.sleep(3)

        try:
            self.driver.find_element(By.XPATH,'//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]').click()

        except ElementNotVisibleException as selenium_error:
            print(selenium_error)

        # Expected Result: Verify that a message for successful deletion is displayed
        success_message = self.driver.find_element(By.XPATH,'//*[@id="oxd-toaster_1"]/div/div[1]/div[2]/p[2]').text
        assert "successfully deleted" in success_message.lower(), "Employee deletion failed"

        if success_message.lower() in "successfully deleted":
            print("PASS  : Deleted successfully")
        else:
            print("FAIL  : Deletion failed")
            
        self.logout()


    def fill_emp_details_save(self):
        # Fill in employee details (modify as per your application)
        wait = WebDriverWait(self.driver, 10) 
        wait.until(EC.visibility_of_element_located((By.NAME,"firstName"))).send_keys("John")
        wait.until(EC.visibility_of_element_located((By.NAME,"lastName"))).send_keys("Doe")
        wait.until(EC.visibility_of_element_located((By.XPATH,locators.WebApp_Locators.add_emp_save_btn))).click()
        return wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="oxd-toaster_1"]/div/div[1]/div[2]/p[2]'))).text

    def get_error_message(self):
        return self.driver.find_element(by=By.XPATH, value='//p[@class="oxd-text oxd-text--p oxd-alert-content-text"]').text

    def login(self,uname,passw):
        try:
            self.driver.maximize_window()
            self.driver.get(data.WebApp_Data().url)
            self.driver.implicitly_wait(10)
            self.driver.find_element(by=By.NAME, value=locators.WebApp_Locators().username_input_box).send_keys(uname)
            self.driver.find_element(by=By.NAME, value=locators.WebApp_Locators().password_input_box).send_keys(passw)
            self.driver.find_element(by=By.XPATH, value=locators.WebApp_Locators().submit_button).click()
        
        except NoSuchElementException as selenium_error:
            print(selenium_error)

    def logout(self):
         logout_button = self.driver.find_element(by=By.XPATH, value=locators.WebApp_Locators.logout_button)
         action = ActionChains(self.driver)
         action.click(on_element=logout_button).perform()
         self.driver.find_element(by=By.LINK_TEXT, value='Logout').click()
         self.driver.refresh()


       

def test_main():
    obj1=Project()
    obj1.TC_Login_01_successful_login()
    obj1.TC_Login_02_invalid_login()
    obj1.TC_PIM_01_add_new_employee()
    obj1.TC_PIM_02_edit_existing_employee()
    obj1.TC_PIM_03_delete_existing_employee()
