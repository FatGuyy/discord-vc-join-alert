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
driver.get('https://discord.com/channels/@me')


try:
    vc_members = WebDriverWait(driver, 100).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".usernameFont-2oJxoI")))
except TimeoutException:
    print('time out for login.')

# for vc_member in vc_members:
#     print(vc_member.text)

voice_channels = []
vc_names=[]
channels = driver.find_elements(By.XPATH, value='/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[1]/nav/div[4]/ul/li')
limit = len(channels)
channels=[]

for indx in range(1, limit+2):
    try:
        channels.append(driver.find_element_by_xpath(f'/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[1]/nav/div[4]/ul/li[{indx}]/div/div/div/a'))
    except:
        continue


#/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div[2]/div[1]/nav/div[4]/ul/li[10]/div[2]/div[2]/div/div/div[2]
#/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div[2]/div[1]/nav/div[4]/ul/li[10]/div[2]/div[1]/div/div/div[2]
vc_with_members = []
#General (voice channel), 1 user
for channel in channels:
    aria_label = channel.get_attribute('aria-label')
    if "(voice channel)" in aria_label:
        name = str(aria_label).partition('(voice channel)')[0]
        vc_names.append(name)
        voice_channels.append(channel)
        single_member = []
        single_member.append(name)
        #number of members in vc
        res = aria_label.split(',', 1)
        splitString = res[1]
        #print((splitString[:2]).strip())
        single_member.append((splitString[:2]).strip())
        vc_with_members.append(single_member)
print('\n\n', 'vc_with_members :')
print(vc_with_members, '\n\n')


voice_members_as_channels = []
# for indx in range():
#     vc_member = driver.find_element_by_xpath(f'/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div[2]/div[1]/nav/div[4]/ul/li[10]/div[2]/div[{indx}]/div/div/div[2]')
#     voice_members_as_channels.append(vc_member)


print('v channels : ', voice_channels, '\n\n','vc names :', vc_names, '\n\n')

driver.close()