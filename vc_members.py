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
vc_names=[]
channels = driver.find_elements(By.XPATH, value='/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[1]/nav/div[4]/ul/li')
limit = len(channels)
print(channels , '\n\n', limit)
channels=[]

for indx in range(1, limit+2):
    try:
        channels.append(driver.find_element(By.XPATH,value=f'/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[1]/nav/div[4]/ul/li[{indx}]/div/div/div/a'))
    except:
        continue

print(len(channels))

#General (voice channel), 1 user
#res = test_string.partition(spl_word)[0]
for channel in channels:
    aria_label = channel.get_attribute('aria-label')
    if "(voice channel)" in aria_label:
        name = str(aria_label).partition('(voice channel)')[0]
        vc_names.append(name)
        voice_channels.append(channel)

print('v channels : ', voice_channels, '\n\n','vc names :', vc_names, '\n\n')
# for indx in range(1,limit+2): 
#         channels.append(driver.find_element(By.XPATH, value=f'/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[1]/nav/div[4]/ul/li[{indx}]/div[1]/div/div/a'))
#         print('here.')

# for channel in channels:
#     if channel.get_attribute('aria-label') == 'Voice':
#         voice_channels.append(channel)   
#         print('added.') 

# for indx,channel in enumerate(channels):
#     if channel.get_attribute('aria-label') == 'Voice':
#         voice_channels.append(indx)



# for indx in voice_channels:
#     peoples = driver.find_elements(by=By.XPATH,value=f"/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[1]/nav/div[4]/ul/li[{indx}]/div[2]/div[1]/div/div/div")
#     print(indx)
#     for people in peoples:
#         name = people.text   
#         print(name)


if __name__ == '__main__':
    pass
    # for i in range(len(vc_members)):
    #     print(vc_members[i].text)
    # time.sleep(5)

driver.close()