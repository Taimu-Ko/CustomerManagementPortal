from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from unittest import TestCase  

class TestAdminUsers(TestCase):
    def setUp(self):    
        self._driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))     
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
        self._driver.get('http://127.0.0.1:5000/admin')  

    def test_1_view_users(self):  
        # Expected Values
        first_name = 'River'
        surname = 'Brown'
        email = 'rcbrown94@outlook.com'
        is_active = 'Active'
        is_admin = 'Admin User'
        user_count = 4
        
        # Get Page Variables
        user_table = self._driver.find_element(By.ID, 'user-table') 
        user_rows = user_table.find_elements(By.TAG_NAME, 'tr')
        first_data_row_columns = user_rows[1].find_elements(By.TAG_NAME, 'td')
        
        assert first_data_row_columns[0].text == first_name
        assert first_data_row_columns[1].text == surname
        assert first_data_row_columns[2].text == email
        assert first_data_row_columns[4].text == is_active
        assert first_data_row_columns[5].text == is_admin
        # Plus one for table header row
        assert len(user_rows) == user_count + 1

    def test_2_lock_user_with_confirm_no(self): 
        # Expected Values
        first_name = 'Kitsune'
        surname = 'Grimm'
        email = 'kitsunegrimm1@gmail.com'
        is_active = 'Active'
        is_admin = 'Normal User'
        user_count = 4
        
        # Get Page Variables
        user_table = self._driver.find_element(By.ID, 'user-table') 
        user_rows = user_table.find_elements(By.TAG_NAME, 'tr')
        unlock_lock_user_icon = user_rows[2].find_element(By.ID, 'unlock-lock-user')
        unlock_lock_user_icon.click()
        self._driver.switch_to.alert.dismiss()
        
        # Refresh Page
        self._driver.get('http://127.0.0.1:5000/admin') 
        user_table = self._driver.find_element(By.ID, 'user-table') 
        user_rows = user_table.find_elements(By.TAG_NAME, 'tr')
        second_data_row_columns = user_rows[2].find_elements(By.TAG_NAME, 'td') 
        
        assert second_data_row_columns[0].text == first_name
        assert second_data_row_columns[1].text == surname
        assert second_data_row_columns[2].text == email
        assert second_data_row_columns[4].text == is_active
        assert second_data_row_columns[5].text == is_admin
        # Plus one for table header row
        assert len(user_rows) == user_count + 1
        
    def test_3_lock_user_with_confirm_yes(self): 
        # Expected Values
        first_name = 'Kitsune'
        surname = 'Grimm'
        email = 'kitsunegrimm1@gmail.com'
        is_active = 'Locked'
        is_admin = 'Normal User'
        user_count = 4
        
        # Get Page Variables
        user_table = self._driver.find_element(By.ID, 'user-table') 
        user_rows = user_table.find_elements(By.TAG_NAME, 'tr')
        unlock_lock_user_icon = user_rows[2].find_element(By.ID, 'unlock-lock-user')
        unlock_lock_user_icon.click()
        self._driver.switch_to.alert.accept()
        
        # Refresh Page
        self._driver.get('http://127.0.0.1:5000/admin') 
        user_table = self._driver.find_element(By.ID, 'user-table') 
        user_rows = user_table.find_elements(By.TAG_NAME, 'tr')
        second_data_row_columns = user_rows[2].find_elements(By.TAG_NAME, 'td') 
        
        assert second_data_row_columns[0].text == first_name
        assert second_data_row_columns[1].text == surname
        assert second_data_row_columns[2].text == email
        assert second_data_row_columns[4].text == is_active
        assert second_data_row_columns[5].text == is_admin
        # Plus one for table header row
        assert len(user_rows) == user_count + 1
        
    def test_4_unlock_user_with_confirm_no(self): 
        # Expected Values
        first_name = 'Kitsune'
        surname = 'Grimm'
        email = 'kitsunegrimm1@gmail.com'
        is_active = 'Locked'
        is_admin = 'Normal User'
        user_count = 4
        
        # Get Page Variables
        user_table = self._driver.find_element(By.ID, 'user-table') 
        user_rows = user_table.find_elements(By.TAG_NAME, 'tr')
        unlock_lock_user_icon = user_rows[2].find_element(By.ID, 'unlock-lock-user')
        unlock_lock_user_icon.click()
        self._driver.switch_to.alert.dismiss()
        
        # Refresh Page
        self._driver.get('http://127.0.0.1:5000/admin') 
        user_table = self._driver.find_element(By.ID, 'user-table') 
        user_rows = user_table.find_elements(By.TAG_NAME, 'tr')
        second_data_row_columns = user_rows[2].find_elements(By.TAG_NAME, 'td') 
        
        assert second_data_row_columns[0].text == first_name
        assert second_data_row_columns[1].text == surname
        assert second_data_row_columns[2].text == email
        assert second_data_row_columns[4].text == is_active
        assert second_data_row_columns[5].text == is_admin
        # Plus one for table header row
        assert len(user_rows) == user_count + 1

    def test_5_unlock_user_with_confirm_yes(self): 
        # Expected Values
        first_name = 'Kitsune'
        surname = 'Grimm'
        email = 'kitsunegrimm1@gmail.com'
        is_active = 'Active'
        is_admin = 'Normal User'
        user_count = 4
        
        # Get Page Variables
        user_table = self._driver.find_element(By.ID, 'user-table') 
        user_rows = user_table.find_elements(By.TAG_NAME, 'tr')
        unlock_lock_user_icon = user_rows[2].find_element(By.ID, 'unlock-lock-user')
        unlock_lock_user_icon.click()
        self._driver.switch_to.alert.accept()
        
        # Refresh Page
        self._driver.get('http://127.0.0.1:5000/admin') 
        user_table = self._driver.find_element(By.ID, 'user-table') 
        user_rows = user_table.find_elements(By.TAG_NAME, 'tr')
        second_data_row_columns = user_rows[2].find_elements(By.TAG_NAME, 'td') 
        
        assert second_data_row_columns[0].text == first_name
        assert second_data_row_columns[1].text == surname
        assert second_data_row_columns[2].text == email
        assert second_data_row_columns[4].text == is_active
        assert second_data_row_columns[5].text == is_admin
        # Plus one for table header row
        assert len(user_rows) == user_count + 1

    def test_6_delete_user_with_confirm_no(self): 
        # Expected Values
        user_count = 4
        
        # Get Page Variables
        user_table = self._driver.find_element(By.ID, 'user-table') 
        user_rows = user_table.find_elements(By.TAG_NAME, 'tr')
        delete_user_icon = user_rows[4].find_element(By.ID, 'delete-user')
        delete_user_icon.click()
        self._driver.switch_to.alert.dismiss()
        
        # Refresh values
        self._driver.get('http://127.0.0.1:5000/admin') 
        user_table = self._driver.find_element(By.ID, 'user-table') 
        user_rows = user_table.find_elements(By.TAG_NAME, 'tr')
            
        # Plus one for table header row
        assert len(user_rows) == user_count + 1
    
    def test_6_delete_user_with_confirm_yes(self): 
        # Expected Values
        user_count = 3
        success_message = 'User deleted'
        
        # Get Page Variables
        user_table = self._driver.find_element(By.ID, 'user-table') 
        user_rows = user_table.find_elements(By.TAG_NAME, 'tr')
        delete_user_icon = user_rows[4].find_element(By.ID, 'delete-user')
        delete_user_icon.click()
        self._driver.switch_to.alert.accept()
        
        display_message = self._driver.find_element(By.NAME, 'display-message') 
        assert display_message.text == success_message 
        
        # Refresh values
        self._driver.get('http://127.0.0.1:5000/admin') 
        user_table = self._driver.find_element(By.ID, 'user-table') 
        user_rows = user_table.find_elements(By.TAG_NAME, 'tr')
            
        # Plus one for table header row
        assert len(user_rows) == user_count + 1

    def tearDown(self):    
        self._driver.quit()   