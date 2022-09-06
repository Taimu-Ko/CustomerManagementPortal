from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from unittest import TestCase  

class TestSignup(TestCase):
    def setUp(self):    
        PATH = 'C:\Selenium\chromedriver.exe'
        self._driver = webdriver.Chrome(PATH)    
        self._driver.implicitly_wait(10)  
        self._driver.get('http://127.0.0.1:5000/signup')    

    def test_1_signup_mismatch_passwords(self):  
        #Set up Variables
        valid_first_name = 'Kitsune'
        valid_surname = 'King'
        valid_email = 'kitsunegrimm94@gmail.com'
        valid_password = 'P@ssw0rd12'
        invalid_password = 'P@ssw0rd13'
        success_message = 'Passwords must match'
                
        first_name = self._driver.find_element(By.NAME, 'firstName')   
        first_name.send_keys(valid_first_name)
        surname = self._driver.find_element(By.NAME, 'surname')   
        surname.send_keys(valid_surname)
        email = self._driver.find_element(By.ID, 'email')    
        email.send_keys(valid_email)    
        password = self._driver.find_element(By.ID, 'password')    
        password.send_keys(valid_password)
        confirm_password = self._driver.find_element(By.NAME, 'confirmPassword')   
        confirm_password.send_keys(invalid_password)
        submit_btn = self._driver.find_element(By.NAME, 'signup')
        submit_btn.click()
        
        display_message = self._driver.find_element(By.NAME, 'display-message')  
        assert display_message.text == success_message
        
    def test_2_signup_password_length(self):  
        #Set up Variables
        valid_first_name = 'Kitsune'
        valid_surname = 'King'
        valid_email = 'kitsunegrimm94@gmail.com'
        invalid_password = 'P@ssw0r'
        success_message = 'Password must be at least 8 characters and contain at least one uppercase, one number and one special character'
                
        first_name = self._driver.find_element(By.NAME, 'firstName')   
        first_name.send_keys(valid_first_name)
        surname = self._driver.find_element(By.NAME, 'surname')   
        surname.send_keys(valid_surname)
        email = self._driver.find_element(By.ID, 'email')    
        email.send_keys(valid_email)    
        password = self._driver.find_element(By.ID, 'password')    
        password.send_keys(invalid_password)
        confirm_password = self._driver.find_element(By.NAME, 'confirmPassword')   
        confirm_password.send_keys(invalid_password)
        submit_btn = self._driver.find_element(By.NAME, 'signup')
        submit_btn.click()
        
        display_message = self._driver.find_element(By.NAME, 'display-message')  
        assert display_message.text == success_message
    
    def test_3_signup_password_no_special(self):  
        #Set up Variables
        valid_first_name = 'Kitsune'
        valid_surname = 'King'
        valid_email = 'kitsunegrimm94@gmail.com'
        invalid_password = 'Passw0rd'
        success_message = 'Password must be at least 8 characters and contain at least one uppercase, one number and one special character'
                
        first_name = self._driver.find_element(By.NAME, 'firstName')   
        first_name.send_keys(valid_first_name)
        surname = self._driver.find_element(By.NAME, 'surname')   
        surname.send_keys(valid_surname)
        email = self._driver.find_element(By.ID, 'email')    
        email.send_keys(valid_email)    
        password = self._driver.find_element(By.ID, 'password')    
        password.send_keys(invalid_password)
        confirm_password = self._driver.find_element(By.NAME, 'confirmPassword')   
        confirm_password.send_keys(invalid_password)
        submit_btn = self._driver.find_element(By.NAME, 'signup')
        submit_btn.click()
        
        display_message = self._driver.find_element(By.NAME, 'display-message')  
        assert display_message.text == success_message
    
    def test_4_signup_password_no_capital(self):  
        #Set up Variables
        valid_first_name = 'Kitsune'
        valid_surname = 'King'
        valid_email = 'kitsunegrimm94@gmail.com'
        invalid_password = 'p@ssw0rd'
        success_message = 'Password must be at least 8 characters and contain at least one uppercase, one number and one special character'
                
        first_name = self._driver.find_element(By.NAME, 'firstName')   
        first_name.send_keys(valid_first_name)
        surname = self._driver.find_element(By.NAME, 'surname')   
        surname.send_keys(valid_surname)
        email = self._driver.find_element(By.ID, 'email')    
        email.send_keys(valid_email)    
        password = self._driver.find_element(By.ID, 'password')    
        password.send_keys(invalid_password)
        confirm_password = self._driver.find_element(By.NAME, 'confirmPassword')   
        confirm_password.send_keys(invalid_password)
        submit_btn = self._driver.find_element(By.NAME, 'signup')
        submit_btn.click()
        
        display_message = self._driver.find_element(By.NAME, 'display-message')  
        assert display_message.text == success_message
    
    def test_5_signup_password_no_number(self):  
        #Set up Variables
        valid_first_name = 'Kitsune'
        valid_surname = 'King'
        valid_email = 'kitsunegrimm94@gmail.com'
        invalid_password = 'P@ssword'
        success_message = 'Password must be at least 8 characters and contain at least one uppercase, one number and one special character'
                
        first_name = self._driver.find_element(By.NAME, 'firstName')   
        first_name.send_keys(valid_first_name)
        surname = self._driver.find_element(By.NAME, 'surname')   
        surname.send_keys(valid_surname)
        email = self._driver.find_element(By.ID, 'email')    
        email.send_keys(valid_email)    
        password = self._driver.find_element(By.ID, 'password')    
        password.send_keys(invalid_password)
        confirm_password = self._driver.find_element(By.NAME, 'confirmPassword')   
        confirm_password.send_keys(invalid_password)
        submit_btn = self._driver.find_element(By.NAME, 'signup')
        submit_btn.click()
        
        display_message = self._driver.find_element(By.NAME, 'display-message')  
        assert display_message.text == success_message
        
    def test_6_signup_first_name_empty(self):  
        #Set up Variables
        valid_surname = 'King'
        valid_email = 'kitsunegrimm94@gmail.com'
        valid_password = 'P@ssw0rd12'
        success_message = 'First Name cannot be empty'
                
        surname = self._driver.find_element(By.NAME, 'surname')   
        surname.send_keys(valid_surname)
        email = self._driver.find_element(By.ID, 'email')    
        email.send_keys(valid_email)    
        password = self._driver.find_element(By.ID, 'password')    
        password.send_keys(valid_password)
        confirm_password = self._driver.find_element(By.NAME, 'confirmPassword')   
        confirm_password.send_keys(valid_password)
        submit_btn = self._driver.find_element(By.NAME, 'signup')
        submit_btn.click()
        
        display_message = self._driver.find_element(By.NAME, 'display-message')  
        assert display_message.text == success_message
        
    def test_7_signup_surname_empty(self):  
        #Set up Variables
        valid_first_name = 'Kitsune'
        valid_email = 'kitsunegrimm94@gmail.com'
        valid_password = 'P@ssw0rd12'
        success_message = 'Surname cannot be empty'
                
        first_name = self._driver.find_element(By.NAME, 'firstName')   
        first_name.send_keys(valid_first_name)
        email = self._driver.find_element(By.ID, 'email')    
        email.send_keys(valid_email)    
        password = self._driver.find_element(By.ID, 'password')    
        password.send_keys(valid_password)
        confirm_password = self._driver.find_element(By.NAME, 'confirmPassword')   
        confirm_password.send_keys(valid_password)
        submit_btn = self._driver.find_element(By.NAME, 'signup')
        submit_btn.click()
        
        display_message = self._driver.find_element(By.NAME, 'display-message')  
        assert display_message.text == success_message
         
    def test_8_signup_user_exists(self):  
        #Set up Variables
        valid_first_name = 'Kitsune'
        valid_surname = 'King'
        valid_email = 'rcbrown94@outlook.com'
        valid_password = 'P@ssw0rd12'
        success_message = 'This email is already registered to an account'
                
        first_name = self._driver.find_element(By.NAME, 'firstName')   
        first_name.send_keys(valid_first_name)
        surname = self._driver.find_element(By.NAME, 'surname')   
        surname.send_keys(valid_surname)
        email = self._driver.find_element(By.ID, 'email')    
        email.send_keys(valid_email)    
        password = self._driver.find_element(By.ID, 'password')    
        password.send_keys(valid_password)
        confirm_password = self._driver.find_element(By.NAME, 'confirmPassword')   
        confirm_password.send_keys(valid_password)
        submit_btn = self._driver.find_element(By.NAME, 'signup')
        submit_btn.click()
        
        display_message = self._driver.find_element(By.NAME, 'display-message')  
        assert display_message.text == success_message
            
    def test_9_signup_valid(self):  
        #Set up Variables
        valid_first_name = 'Kitsune'
        valid_surname = 'King'
        valid_email = 'kitsunegrimm94@gmail.com'
        valid_password = 'P@ssw0rd12'
        success_message = 'User account added'
                
        first_name = self._driver.find_element(By.NAME, 'firstName')   
        first_name.send_keys(valid_first_name)
        surname = self._driver.find_element(By.NAME, 'surname')   
        surname.send_keys(valid_surname)
        email = self._driver.find_element(By.ID, 'email')    
        email.send_keys(valid_email)    
        password = self._driver.find_element(By.ID, 'password')    
        password.send_keys(valid_password)
        confirm_password = self._driver.find_element(By.NAME, 'confirmPassword')   
        confirm_password.send_keys(valid_password)
        submit_btn = self._driver.find_element(By.NAME, 'signup')
        submit_btn.click()
        
        display_message = self._driver.find_element(By.NAME, 'display-message')  
        assert display_message.text == success_message
           
    def tearDown(self):    
        self._driver.quit()   