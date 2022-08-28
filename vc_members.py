from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

#Put your email and password here
#---------------------------------------
mail = ""
password = ""
#---------------------------------------


os.environ['PATH'] += r'.\chromedriver.chromedriver.exe'
url = 'https://discord.com/login'
driver = webdriver.Chrome()
driver.get(url)

linkElem = driver.find_element(by=By.NAME, value='email')
linkElem.send_keys(mail) #email
linkElem = driver.find_element(by=By.NAME, value='password')
linkElem.send_keys(password) #password
driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/form/div/div/div[1]/div[2]/button[2]').click() #logs in
driver.implicitly_wait(15)
time.sleep(10)

vc_members = driver.find_elements(by=By.CSS_SELECTOR, value='.usernameFont-2oJxoI')

#vc = driver.find_element(By.XPATH, value="//li[@class='containerDefault-YUSmu3']").get_attribute('data-dnd-name')
#print(vc)
voice_channels = []
channels = driver.find_elements(By.CLASS_NAME, value='iconContainer-21RCa3')
for channel in channels:
    if channel.get_attribute('aria-label') == 'Voice':
        voice_channels.append(channel)

print(voice_channels)


if __name__ == '__main__':
    for i in range(len(vc_members)):
        print(vc_members[i].text)
    time.sleep(5)

driver.close()