from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from unittest import TestCase  

class TestAddCard(TestCase):
    def setUp(self):    
        PATH = 'C:\Selenium\chromedriver.exe'
        self._driver = webdriver.Chrome(PATH)    
        self._driver.implicitly_wait(10)    
        valid_email = 'rcbrown94@outlook.com'
        valid_password = 'P@ssw0rd12'
        self._driver.get('http://127.0.0.1:5000/login')    
        email = self._driver.find_element(By.ID, 'email')    
        email.send_keys(valid_email)    
        password = self._driver.find_element(By.ID, 'password')    
        password.send_keys(valid_password)
        submit_btn = self._driver.find_element(By.NAME, 'login_btn')
        submit_btn.click()
        self._driver.get('http://127.0.0.1:5000/cards/add')  

    def test_1_add_card_card_number_generated(self):  
        # Expected Values
        card_status_value = 'Pending'
        
        # Get Page Variables
        card_number = self._driver.find_element(By.NAME, 'cardNumber') 
        card_status = self._driver.find_element(By.NAME, 'status') 
        card_name = self._driver.find_element(By.NAME, 'cardName') 
        
        assert card_number.get_attribute('value').isdigit() == True
        assert card_status.get_attribute('value') == card_status_value
        assert card_number.get_attribute("readonly") == "true"
        assert card_name.get_attribute("readonly") == None
        assert card_status.get_attribute("readonly") == "true"

    def test_2_add_card_card_name_length(self):  
        # Expected Values
        card_status_input = 'Pending'
        card_name_input = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
        error_message = 'Card name must be 30 characters or less'
        
        # Get Page Variables
        card_number = self._driver.find_element(By.NAME, 'cardNumber') 
        card_status = self._driver.find_element(By.NAME, 'status') 
        card_name = self._driver.find_element(By.NAME, 'cardName') 
        submit = self._driver.find_element(By.NAME, 'submit') 
        card_name.send_keys(card_name_input)
         
        assert card_number.get_attribute('value').isdigit() == True
        assert card_status.get_attribute('value') == card_status_input
        assert card_number.get_attribute("readonly") == "true"
        assert card_name.get_attribute("readonly") == None
        assert card_status.get_attribute("readonly") == "true"
        
        submit.click()
        display_message = self._driver.find_element(By.NAME, 'display-message') 
        
        assert display_message.text == error_message 
        
    def test_3_add_card_valid(self):  
        # Expected Values
        card_status_input = 'Pending'
        card_name_input = 'Rivaa Test Card'
        success_message = 'Card added'
        
        # Get Page Variables
        card_number = self._driver.find_element(By.NAME, 'cardNumber') 
        card_status = self._driver.find_element(By.NAME, 'status') 
        card_name = self._driver.find_element(By.NAME, 'cardName') 
        submit = self._driver.find_element(By.NAME, 'submit') 
        card_name.send_keys(card_name_input)
        
        assert card_number.get_attribute('value').isdigit() == True
        assert card_status.get_attribute('value') == card_status_input
        assert card_number.get_attribute("readonly") == "true"
        assert card_name.get_attribute("readonly") == None
        assert card_status.get_attribute("readonly") == "true"
                
        submit.click()
        display_message = self._driver.find_element(By.NAME, 'display-message') 
        
        assert display_message.text == success_message      

    def tearDown(self):    
        self._driver.quit()   