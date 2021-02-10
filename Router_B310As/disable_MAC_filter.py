#Faisalfs10x
#!/usr/bin/env python
import time, subprocess
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

def main():

    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options, executable_path=r'C:\Program Files\geckodriver-v0.29.0-win64\geckodriver.exe')

    url = "http://192.168.0.1/html/home.html" 
    driver.get(url)
    time.sleep(1)
    print("Running") 

    username = "admin"
    password = "pwd"

    # login
    driver.find_element_by_id('logout_span').click()
    driver.find_element_by_id('username').clear()
    driver.find_element_by_id('username').send_keys(username)
    driver.find_element_by_id('password').send_keys(password)
   
    driver.find_element_by_id('pop_login').click()
    time.sleep(2)
    # go to mac filter endpoint
    driver.get("http://192.168.0.1/html/wlanmacfilter.html") 
    # click dropdown 
    dropdown = driver.find_element_by_id('ssid_select_service').click()
    # choose Deny
    driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/span[2]/select/option[1]").click()
    driver.find_element_by_id('apply').click() 
    time.sleep(2)
    driver.find_element_by_id('pop_confirm').click()
    time.sleep(2)
    
    driver.quit()  
    print("MAC filter disable!")  

#    browser.delete_all_cookies()
#    browser.close()
            
if __name__ == '__main__':
    main()
