from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from unittest import TestCase  

class TestLogin(TestCase):
    def setUp(self):    
        PATH = 'C:\Selenium\chromedriver.exe'
        self._driver = webdriver.Chrome(PATH)    
        self._driver.implicitly_wait(10)    

    def test_1_login(self):  
        #Set up Variables
        valid_email = 'rcbrown94@outlook.com'
        valid_password = 'P@ssw0rd12'
        success_message = 'Logged in successfully'
             
        self._driver.get('http://127.0.0.1:5000/login')    
        email = self._driver.find_element(By.ID, 'email')    
        email.send_keys(valid_email)    
        password = self._driver.find_element(By.ID, 'password')    
        password.send_keys(valid_password)
        submit_btn = self._driver.find_element(By.NAME, 'login_btn')
        submit_btn.click()
        
        display_message = self._driver.find_element(By.NAME, 'display-message')  

        assert display_message.text == success_message
        
    def test_2_invalid_login(self):  
        #Set up Variables
        invalid_email = '1234@mail.com'
        invalid_password = '1234'
        error_message = 'Your username or password is incorrect.'
             
        self._driver.get('http://127.0.0.1:5000/login')    
        email = self._driver.find_element(By.NAME, 'email')    
        email.send_keys(invalid_email)    
        password = self._driver.find_element(By.NAME, 'password')    
        password.send_keys(invalid_password)
        submit_btn = self._driver.find_element(By.NAME, 'login_btn')
        submit_btn.click()
        
        display_message = self._driver.find_element(By.NAME, 'display-message')  

        assert display_message.text == error_message
        
    def test_3_lock_user(self):  
        #Set up Variables
        invalid_email = 'lockme@admin.com'
        invalid_password = '1234'
        locked_error_message = 'Your account has been locked due to multiple failed login attempts. Please contact your administrator.'
             
        # 1st Failed Attempt
        self._driver.get('http://127.0.0.1:5000/login')    
        email = self._driver.find_element(By.NAME, 'email')    
        email.send_keys(invalid_email)    
        password = self._driver.find_element(By.NAME, 'password')    
        password.send_keys(invalid_password)
        submit_btn = self._driver.find_element(By.NAME, 'login_btn')
        submit_btn.click()   
        display_message = self._driver.find_element(By.NAME, 'display-message')  
        close_display_message = self._driver.find_element(By.NAME, 'close-display-message')
        close_display_message.click()
        
        # 2nd Failed Attempt   
        email = self._driver.find_element(By.NAME, 'email')    
        email.send_keys(invalid_email)    
        password = self._driver.find_element(By.NAME, 'password')    
        password.send_keys(invalid_password)
        submit_btn = self._driver.find_element(By.NAME, 'login_btn')
        submit_btn.click()   
        display_message = self._driver.find_element(By.NAME, 'display-message')  
        close_display_message = self._driver.find_element(By.NAME, 'close-display-message')
        close_display_message.click()
        
        # 3rd Failed Attempt       
        email = self._driver.find_element(By.NAME, 'email')    
        email.send_keys(invalid_email)    
        password = self._driver.find_element(By.NAME, 'password')    
        password.send_keys(invalid_password)
        submit_btn = self._driver.find_element(By.NAME, 'login_btn')
        submit_btn.click()   
        display_message = self._driver.find_element(By.NAME, 'display-message')  
        close_display_message = self._driver.find_element(By.NAME, 'close-display-message')
        close_display_message.click()

        # Lock User  
        email = self._driver.find_element(By.NAME, 'email')    
        email.send_keys(invalid_email)    
        password = self._driver.find_element(By.NAME, 'password')    
        password.send_keys(invalid_password)
        submit_btn = self._driver.find_element(By.NAME, 'login_btn')
        submit_btn.click()   
        display_message = self._driver.find_element(By.NAME, 'display-message')  
        assert display_message.text == locked_error_message
   
    def test_4_inactive_user_login(self):  
        #Set up Variables
        valid_email = 'inactive@admin.com'
        valid_password = 'P@ssw0rd12'
        lock_message = 'Unable to log in. Your account is locked.'
             
        self._driver.get('http://127.0.0.1:5000/login')    
        email = self._driver.find_element(By.ID, 'email')    
        email.send_keys(valid_email)    
        password = self._driver.find_element(By.ID, 'password')    
        password.send_keys(valid_password)
        submit_btn = self._driver.find_element(By.NAME, 'login_btn')
        submit_btn.click()
        display_message = self._driver.find_element(By.NAME, 'display-message')  

        assert display_message.text == lock_message
   
    def tearDown(self):    
        self._driver.quit()   