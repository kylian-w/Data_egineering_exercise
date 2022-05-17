from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
import time
import pandas as pd
import os
import wget
import instaloader
from datetime import datetime
from itertools import dropwhile, takewhile
import csv
from bs4 import BeautifulSoup as bs

file_path = 'C:/Users/kylia/OneDrive/Bureau/test_DI/sel/chromedriver.exe'
driver = webdriver.Chrome(file_path)
#driver = webdriver.Chrome() if your chromedriver.exe inside root
driver.get("http://www.instagram.com")


#open credential file
with open('insta_cred.txt') as file:
    Login1 = file.readline().split('"')[1]
    PASSWORD = file.readline().split('"')[1]

#insert creds
wait = WebDriverWait(driver, 30)
un_field = wait.until(EC.visibility_of_element_located((By.NAME, 'username')))
un_field.send_keys(Login1)
pass_field = wait.until(EC.visibility_of_element_located((By.NAME, 'password')))
pass_field.send_keys(PASSWORD)
pass_field.send_keys(Keys.RETURN)


#click on the not now buttons popping up
wait2=WebDriverWait(driver, 10)
not_now1 = wait2.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not now")]'))).click()
not_now2 = wait2.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()

#search
searchbox = wait2.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']")))
searchbox.clear()
tag1 = "#harassment"
searchbox.send_keys(tag1)
time.sleep(2)
searchbox.send_keys(Keys.ENTER)
time.sleep(3)
searchbox.send_keys(Keys.ENTER)
time.sleep(3)

# #scroll

driver.execute_script("window.scrollBy(0,1000000)")
time.sleep(5)
driver.execute_script("window.scrollBy(0,1000000)")
time.sleep(5)
driver.execute_script("window.scrollBy(0,1000000)")
time.sleep(5)


#  #getting the posts
# links = driver.find_elements_by_tag_name('a')
# links = [link.get_attribute('href') for link in links]
# print(links)

#select the images
# images = driver.find_elements_by_tag_name('img')
# images = [image.get_attribute('src') for image in images]
# images = images[:-2] #slicing-off IG logo and Profile picture
# print('Number of scraped images: ', len(images))

# path = os.getcwd()
# path = os.path.join(path, tag1[1:] + "s")
# os.mkdir(path)

# #download images
# counter = 0
# for image in images:
#     save_as = os.path.join(path, tag1[1:] + str(counter) +
#     '.jpg')
#     wget.download(image, save_as)
#     counter += 1


# df = pd.DataFrame(links,columns=["InstagramPostLink"])
# print(df)
# df.to_csv('uniqlojapan.csv')

texts=[]
while True:
    soup=bs(driver.page_source,"html.parser")
    reviews = soup.find_all('div', {'class':'_9AhH0'})
    print('_________________post are oppended___________________')
    for post in reviews:
        try:
                
                post_text=post.find('div', {'class':'_7UhW9   xLCgt      MMzan   KV-D4            se6yk       T0kll '})
        except:
                post_text="not found"

        texts.append(post_text)
        print(texts)
       


