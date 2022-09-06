from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from unittest import TestCase  

class TestViewCard(TestCase):
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
        self._driver.get('http://127.0.0.1:5000/cards')   
        card_table = self._driver.find_element(By.ID, 'card-table') 
        card_rows = card_table.find_elements(By.TAG_NAME, 'tr')
        first_data_row_columns = card_rows[1].find_elements(By.TAG_NAME, 'td')
        view_card_icon = first_data_row_columns[5].find_element(By.ID, 'view-card')
        view_card_icon.click()

    def test_1_view_card_values_match(self):  
        # Expected Values
        card_number_value = '6123456789012345678'
        card_name_value = 'Rivaa Card 1'
        card_status_value = 'Current'
        expiry_date_value = '2026-01-01'
        
        # Get Page Variables
        card_number = self._driver.find_element(By.NAME, 'cardNumber') 
        card_status = self._driver.find_element(By.NAME, 'status') 
        card_name = self._driver.find_element(By.NAME, 'cardName') 
        expiry_date = self._driver.find_element(By.NAME, 'expiryDate') 
        
        assert card_number.get_attribute('value') == card_number_value
        assert card_status.get_attribute('value') == card_status_value
        assert card_name.get_attribute('value') == card_name_value
        assert expiry_date.get_attribute('value') == expiry_date_value
        
        assert card_number.get_attribute("readonly") == "true"
        assert card_name.get_attribute("readonly") == "true"
        assert card_status.get_attribute("readonly") == "true"
        assert expiry_date.get_attribute("readonly") == "true"

    def test_2_view_card_make_editable(self):  
        # Expected Values
        card_number_value = '6123456789012345678'
        card_name_value = 'Rivaa Card 1'
        card_status_value = 'Current'
        expiry_date_value = '2026-01-01'
        
        # Get Page Variables
        card_number = self._driver.find_element(By.NAME, 'cardNumber') 
        card_status = self._driver.find_element(By.NAME, 'status') 
        card_name = self._driver.find_element(By.NAME, 'cardName') 
        expiry_date = self._driver.find_element(By.NAME, 'expiryDate') 
        
        assert card_number.get_attribute('value') == card_number_value
        assert card_status.get_attribute('value') == card_status_value
        assert card_name.get_attribute('value') == card_name_value
        assert expiry_date.get_attribute('value') == expiry_date_value
        
        assert card_number.get_attribute("readonly") == "true"
        assert card_name.get_attribute("readonly") == "true"
        assert card_status.get_attribute("readonly") == "true"
        assert expiry_date.get_attribute("readonly") == "true"
        
        edit_button = self._driver.find_element(By.NAME, 'edit')
        edit_button.click()
        
        # Refresh Values
        card_number2 = self._driver.find_element(By.NAME, 'cardNumber') 
        card_status2 = self._driver.find_element(By.NAME, 'status') 
        card_name2 = self._driver.find_element(By.NAME, 'cardName') 
        expiry_date2 = self._driver.find_element(By.NAME, 'expiryDate') 
        
        assert card_number2.get_attribute("readonly") == "true"
        assert card_name2.get_attribute("readonly") == None
        assert card_status2.get_attribute("readonly") == "true"
        assert expiry_date2.get_attribute("readonly") == "true"
        
    def test_3_view_card_make_changes(self):  
        # Expected Values
        card_number_value = '6123456789012345678'
        card_name_value = 'Rivaa Card 1'
        card_status_value = 'Current'
        expiry_date_value = '2026-01-01'
        new_card_name = "Rivaa Edit 1"
        success_message = 'Successfully updated card details'
        
        # Get Page Variables
        card_number = self._driver.find_element(By.NAME, 'cardNumber') 
        card_status = self._driver.find_element(By.NAME, 'status') 
        card_name = self._driver.find_element(By.NAME, 'cardName') 
        expiry_date = self._driver.find_element(By.NAME, 'expiryDate') 
        
        assert card_number.get_attribute('value') == card_number_value
        assert card_status.get_attribute('value') == card_status_value
        assert card_name.get_attribute('value') == card_name_value
        assert expiry_date.get_attribute('value') == expiry_date_value
        
        assert card_number.get_attribute("readonly") == "true"
        assert card_name.get_attribute("readonly") == "true"
        assert card_status.get_attribute("readonly") == "true"
        assert expiry_date.get_attribute("readonly") == "true"
        
        edit_button = self._driver.find_element(By.NAME, 'edit')
        edit_button.click()
        
        # Refresh Values
        card_number2 = self._driver.find_element(By.NAME, 'cardNumber') 
        card_status2 = self._driver.find_element(By.NAME, 'status') 
        card_name2 = self._driver.find_element(By.NAME, 'cardName') 
        expiry_date2 = self._driver.find_element(By.NAME, 'expiryDate') 
        submit = self._driver.find_element(By.NAME, 'submit') 
        
        assert card_number2.get_attribute("readonly") == "true"
        assert card_name2.get_attribute("readonly") == None
        assert card_status2.get_attribute("readonly") == "true"
        assert expiry_date2.get_attribute("readonly") == "true"
        
        card_name2.send_keys(new_card_name)
        submit.click()
        
        display_message = self._driver.find_element(By.NAME, 'display-message') 
        
        assert display_message.text == success_message  
       
    def tearDown(self):    
        self._driver.quit()   