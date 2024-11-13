from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from LogInPOM import LoginPage 

# Defining 9 test cases 
test_cases = [
    {"username": "standard_user", "password": "secret_sauce", "description": "Valid username and password"},  # Case 1 Positive
    #{"username": "performance_glitch_user", "password": "secret_sauce", "description": "Valid username and password"},  
    {"username": "wrong_user", "password": "wrong_password", "description": "Invalid username and password"},  # Case 2 Negative 
    {"username": "standard_user", "password": "wrong_password", "description": "Valid username, invalid password"},  # Case 3 Negative 
    {"username": "wrong_user", "password": "wrong_password", "description": "Invalid username and password"},  # Case 4 Negative 
    {"username": "", "password": "secret_sauce", "description": "Empty username, valid password"},  # Case 5 Negative 
    {"username": "", "password": "wrong_password", "description": "Empty username, invalid password"},  # Case 6 Negative 
    {"username": "standard_user", "password": "", "description": "Valid username, empty password"},  # Case 7 Negative 
    {"username": "wrong_user", "password": "", "description": "Invalid username, empty password"},  # Case 8 Negative 
    {"username": "", "password": "", "description": "Empty username and password"}  # Case 9 Negative 
]


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# Iterate over each test case from the pervious defined ones
for case in test_cases:
    
    login_page = LoginPage(driver) 
    driver.get("https://www.saucedemo.com/")
    
    login_page.login(case["username"], case["password"])
    
    time.sleep(1)  ##load between different Log Ins


driver.quit()
