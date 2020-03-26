#Faisalfs10x
#!/usr/bin/env python
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time, subprocess

def main():

    url = "https://github.com/login" 

    profile = webdriver.FirefoxProfile()
    profile.set_preference("general.useragent.override", "Mozilla/5.0 (X11; Linux x86_64; rv:74.0) Gecko/20100101 sel.py")
    browser = webdriver.Firefox(profile)
    browser.get(url)
    time.sleep(1)

    with open('passwordGit.txt', 'r') as pwdgit:
        for details in pwdgit:
            username, password = details.split(':')

            username_entry= browser.find_element_by_name('login')
            username_entry.send_keys(username)

            password_entry = browser.find_element_by_name('password')
            password_entry.send_keys(password)

            login_button= browser.find_element_by_name('commit')
            login_button.submit()

    # Keep the page loaded for 5 seconds
    time.sleep(5)


    browser.find_element_by_xpath("/html/body/div[4]/div/aside[1]/div[2]/div[1]/div/h2/a").click()
    time.sleep(2)
    browser.find_element_by_id('repository_name').send_keys("selenium repo automation")
    browser.find_element_by_id('repository_description').send_keys("Hi, im using selenium to create repo in github. Do follow me on github @faisalfs10x")
    browser.find_element_by_id('repository_auto_init').click()
    time.sleep(5)
    browser.find_element_by_xpath("/html/body/div[4]/main/div/form/div[4]/button").click()
    

#    browser.delete_all_cookies()
#    browser.close()
            
if __name__ == '__main__':
    main()
