import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from getpass4 import getpass

github_homepage = webdriver.Chrome()
github_homepage.get('https://www.github.com')
github_homepage.find_element(By.LINK_TEXT, 'Sign in').click()
time.sleep(3)
username = github_homepage.find_element(By.NAME, 'login')
username.click()
my_username = getpass("Username: ")
username.send_keys(my_username)
password = github_homepage.find_element(By.NAME, 'password')
password.click()
my_password = getpass("Password: ")
password.send_keys(my_password)

sign_in_btn = github_homepage.find_element(By.NAME, 'commit')
sign_in_btn.click()

time.sleep(120)

# button id global-create-menu-button
# a href /new

# input #react-aria-2 repo-name
# input # react-aria-3 description
# input # react-aria-8 add readme
# button submit