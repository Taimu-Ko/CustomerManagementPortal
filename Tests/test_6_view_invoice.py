from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from unittest import TestCase  

class TestViewInvoice(TestCase):
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
        self._driver.get('http://127.0.0.1:5000/invoices')   
        invoice_table = self._driver.find_element(By.ID, 'invoice-table') 
        invoice_rows = invoice_table.find_elements(By.TAG_NAME, 'tr')
        first_data_row_columns = invoice_rows[1].find_elements(By.TAG_NAME, 'td')
        view_invoice_icon = first_data_row_columns[6].find_element(By.ID, 'view-invoice')
        view_invoice_icon.click()

    def test_1_view_invoice_values_match(self):  
        # Expected Values
        invoice_reference_value = 'RIV001'
        invoice_date_value = '2022-01-02'
        invoice_gross_amount_value = '£100.00'
        payment_date_value = '2022-01-16'
        invoice_product_count = 2
        
        # Get Page Variables
        invoice_reference = self._driver.find_element(By.NAME, 'invoiceReference') 
        invoice_date = self._driver.find_element(By.NAME, 'invoiceDate') 
        invoice_gross_amount = self._driver.find_element(By.NAME, 'grossAmount') 
        payment_date = self._driver.find_element(By.NAME, 'paymentDate') 
        
        assert invoice_reference.get_attribute('value') == invoice_reference_value
        assert invoice_date.get_attribute('value') == invoice_date_value
        assert invoice_gross_amount.get_attribute('value') == invoice_gross_amount_value
        assert payment_date.get_attribute('value') == payment_date_value
        
        assert invoice_reference.get_attribute("readonly") == "true"
        assert invoice_date.get_attribute("readonly") == "true"
        assert invoice_gross_amount.get_attribute("readonly") == "true"
        assert payment_date.get_attribute("readonly") == "true"
        
        line_item_table = self._driver.find_element(By.ID, 'invoice-line-item-table') 
        line_item_rows = line_item_table.find_elements(By.TAG_NAME, 'tr')

        # Plus one for table header row
        assert len(line_item_rows) == invoice_product_count + 1

    def tearDown(self):    
        self._driver.quit()   