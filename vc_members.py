from selenium.common.exceptions import TimeoutException    
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time


os.environ['PATH'] += r'.chromedriver.chromedriver.exe'
url = 'https://discord.com/login'
driver = webdriver.Chrome()
driver.get(url)

print('\n Waiting for user to  login... Login using scanner or entering your mail and pass \n')
driver.implicitly_wait(15)
time.sleep(10)

#WebDriverWait(driver, timeout).until(element_present)
#vc_members = driver.find_elements(by=By.CSS_SELECTOR, value='.usernameFont-2oJxoI')
try:
    vc_members = WebDriverWait(driver, 100).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".usernameFont-2oJxoI")))
except TimeoutException:
    print('time out for login.')



# class to  xpath containerDefault-YUSmu3 to //li[@class='containerDefault-YUSmu3'] --- //div[contains(@class, 'conContainer-21RCa3')]
#test = driver.find_element(by=By.XPATH,value="//div [@class='iconContainer-21RCa3']") #iconContainer-21RCa3
 
voice_channels = []
channels = driver.find_elements(By.XPATH, value='/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[1]/nav/div[4]/ul/li')
limit = len(channels)
channels= []
for i in range(limit): 
    channels.append(driver.find_elements(By.XPATH, value=f'/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[1]/nav/div[4]/ul/li{i}/div/div/a/div[1]'))
    print('here.')
for channel in channels:
    if channel.get_attribute('aria-label') == 'Voice':
        voice_channels.append(channel)   
        print('added.') 

# for indx,channel in enumerate(channels):
#     if channel.get_attribute('aria-label') == 'Voice':
#         voice_channels.append(indx)
print(voice_channels)


for indx in voice_channels:
    peoples = driver.find_elements(by=By.XPATH,value=f"/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[1]/nav/div[4]/ul/li[{indx}]/div[2]/div[1]/div/div/div")
    print(indx)
    for people in peoples:
        name = people.text   
        print(name)


# print(voice_channels)
# print(voice_channels, 'printing voice channels as elements ')


#for channel in voice_channels:
# for i in range(len(voice_channels)):
    # voice_channels_names.append(driver.find_element(by=By.XPATH, value="//div [@class='iconContainer-21RCa3']").text)



if __name__ == '__main__':
    for i in range(len(vc_members)):
        print(vc_members[i].text)
    time.sleep(5)

driver.close()