#Faisalfs10x
#!/usr/bin/env python
import time, subprocess
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

def main():

    url = "http://192.168.0.1/html/home.html" 
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(1)

    options = Options()
    options.headless = False

    username = "router_admin"
    password = "your_pwd"

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
    driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div[2]/div[2]/div[2]/div[1]/div/span[2]/select/option[3]").click()
    driver.find_element_by_id('ssid_input_WifiMacFilterMac0').send_keys("MAC_ADDRESS_HERE")
    driver.find_element_by_id('apply').click() 
    driver.find_element_by_id('pop_confirm').click()
    time.sleep(2)
    
    driver.quit()    

#    browser.delete_all_cookies()
#    browser.close()
            
if __name__ == '__main__':
    main()
