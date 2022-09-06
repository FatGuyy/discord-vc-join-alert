from selenium.common.exceptions import TimeoutException    
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.chrome.options import Options

path = os.path.join(os.getcwd(),'chrome-data') 
chrome_options = Options()
chrome_options.add_argument(f"--user-data-dir={path}")
driver = webdriver.Chrome('chromedriver.exe',options=chrome_options)
driver.get('https://discord.com/login')


try:
    vc_members = WebDriverWait(driver, 100).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".usernameFont-2oJxoI")))
except TimeoutException:
    print('time out for login.')

for vc_member in vc_members:
    print(vc_member.text)

voice_channels = []
vc_names=[]
channels = driver.find_elements(By.XPATH, value='/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[1]/nav/div[4]/ul/li')
limit = len(channels)
channels=[]

for indx in range(1, limit+2):
    try:
        channels.append(driver.find_element_by_xpath(f'/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[1]/nav/div[4]/ul/li[{indx}]/div/div/div/a'))
        #channels.append(driver.find_element(By.XPATH,value=f'/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[1]/nav/div[4]/ul/li[{indx}]/div/div/div/a'))
    except:
        continue

#General (voice channel), 1 user
for channel in channels:
    aria_label = channel.get_attribute('aria-label')
    if "(voice channel)" in aria_label:
        name = str(aria_label).partition('(voice channel)')[0]
        vc_names.append(name)
        voice_channels.append(channel)

print('v channels : ', voice_channels, '\n\n','vc names :', vc_names, '\n\n')

# for indx,channel in enumerate(channels):
#     if channel.get_attribute('aria-label') == 'Voice':
#         voice_channels.append(indx)
# for indx in voice_channels:
#     peoples = driver.find_elements(by=By.XPATH,value=f"/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[1]/nav/div[4]/ul/li[{indx}]/div[2]/div[1]/div/div/div")
#     print(indx)
#     for people in peoples:
#         name = people.text   
#         print(name)

driver.close()