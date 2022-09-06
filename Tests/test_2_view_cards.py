from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from unittest import TestCase  

class TestViewCards(TestCase):
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

    def test_1_view_card(self):  
        # Expected Values
        card_number = '6123456789012345678'
        card_name = 'Rivaa Card 1'
        card_status = 'Current'
        expiry_date = '2026-01-01'
        card_count = 4
        
        # Get Page Variables
        card_table = self._driver.find_element(By.ID, 'card-table') 
        card_rows = card_table.find_elements(By.TAG_NAME, 'tr')
        first_data_row_columns = card_rows[1].find_elements(By.TAG_NAME, 'td')
        
        assert first_data_row_columns[0].text == card_number
        assert first_data_row_columns[1].text == card_name
        assert first_data_row_columns[2].text == card_status
        assert first_data_row_columns[3].text == expiry_date
        # Plus one for table header row
        assert len(card_rows) == card_count + 1

    def test_2_delete_card(self):  
        # Expected Values
        card_number = '6123456789012345678'
        card_name = 'Rivaa Card 1'
        card_status = 'Current'
        expiry_date = '2026-01-01'
        card_count = 3
        success_message = 'Card deleted'
        
        # Action
        card_table = self._driver.find_element(By.ID, 'card-table') 
        card_rows = card_table.find_elements(By.TAG_NAME, 'tr')
        first_data_row_columns = card_rows[1].find_elements(By.TAG_NAME, 'td')  
        delete_icon = card_rows[4].find_element(By.ID, 'delete-card')
        delete_icon.click()
        display_message = self._driver.find_element(By.NAME, 'display-message') 
        assert display_message.text == success_message  
        
        # Refresh Page
        self._driver.get('http://127.0.0.1:5000/cards') 
        card_table_after = self._driver.find_element(By.ID, 'card-table') 
        card_rows_after = card_table_after.find_elements(By.TAG_NAME, 'tr')
        first_data_row_columns_after = card_rows_after[1].find_elements(By.TAG_NAME, 'td')  
        
        assert first_data_row_columns_after[0].text == card_number
        assert first_data_row_columns_after[1].text == card_name
        assert first_data_row_columns_after[2].text == card_status
        assert first_data_row_columns_after[3].text == expiry_date
        # Plus one for table header row
        assert len(card_rows_after) == card_count + 1

    def tearDown(self):    
        self._driver.quit()   