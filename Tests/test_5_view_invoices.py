from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from unittest import TestCase  

class TestViewInvoices(TestCase):
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

    def test_1_view_invoice(self):  
        # Expected Values
        invoice_reference = 'RIV001'
        invoice_date = '2022-01-02'
        net_amount = '£80.00'
        vat_amount = '£20.00'
        gross_amount = '£100.00'
        payment_due = '2022-01-16'
        invoice_count = 4
        
        # Get Page Variables
        invoice_table = self._driver.find_element(By.ID, 'invoice-table') 
        invoice_rows = invoice_table.find_elements(By.TAG_NAME, 'tr')
        first_data_row_columns = invoice_rows[1].find_elements(By.TAG_NAME, 'td')
        
        assert first_data_row_columns[0].text == invoice_reference
        assert first_data_row_columns[1].text == invoice_date
        assert first_data_row_columns[2].text == net_amount
        assert first_data_row_columns[3].text == vat_amount
        assert first_data_row_columns[4].text == gross_amount
        assert first_data_row_columns[5].text == payment_due
        # Plus one for table header row
        assert len(invoice_rows) == invoice_count + 1

    def tearDown(self):    
        self._driver.quit()   