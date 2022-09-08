from selenium.common.exceptions import TimeoutException    
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

path = os.path.join(os.getcwd(),'chrome-data') 
chrome_options = Options()
chrome_options.add_argument(f"--user-data-dir={path}")
driver = webdriver.Chrome('chromedriver.exe',options=chrome_options)
driver.get('https://discord.com/channels/@me')

time.sleep(10)
scroll_for_all_channels = driver.find_element(By.ID, value='channels')
scroll_for_all_channels.send_keys(Keys.END)
try:
    vc_members = WebDriverWait(driver, 100).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".usernameFont-2oJxoI")))
except TimeoutException:
    print('time out for login.')

# for vc_member in vc_members:
#     print(vc_member.text)
# voice_channels = []
vc_names=[]
channels = driver.find_elements(By.XPATH, value='/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[1]/nav/div[4]/ul/li')
limit = len(channels)
channels=[]
vc_indx = []
for indx in range(1, limit+2):
    try:
        channels.append(driver.find_element_by_xpath(f'/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[1]/nav/div[4]/ul/li[{indx}]/div/div/div/a'))
        vc_indx.append(indx)
    except:
        continue

vc_with_members = []
#General (voice channel), 1 user
for count,channel in enumerate(channels):
    aria_label = channel.get_attribute('aria-label')
    # print('aria_label :',aria_label)
    # print()
    if "(voice channel)" in aria_label:
        name = str(aria_label).partition('(voice channel)')[0]
        vc_names.append(name)
        # voice_channels.append(channel)
        single_member = []
        #number of members in vc
        char_index = int(str(aria_label).rfind(','))
        split_string = int(str(aria_label[char_index+1:char_index+3]))
        # print('users(must be int) :', split_string)
        single_member.append(name)
        single_member.append(split_string)
        vc_with_members.append(single_member)

print('\n\n', 'vc_with_members :')
print(vc_with_members, '\n\n')
print('printing vc index',vc_indx)
vc_members_no = []
for i in vc_with_members:
    limit2 = int(vc_with_members[0][1])
    vc_members_no.append(limit2)
max_members = max(vc_members_no)
voice_members_as_channels = []

# xpaths =[]
# for indx in vc_indx:
#     xpath = f'/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[1]/nav/div[4]/ul/li[{indx}]/div/div/div'
#     xpaths.append(xpath)

#/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[1]/nav/div[4]/ul/li[9]/div[2]/div/div/div/div[2]
#/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[1]/nav/div[4]/ul/li[{indx}]/div/div/div/a
#/div[2]/div[{indx}]/div/div/div[2]
#/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[1]/nav/div[4]/ul/li[9]/div[2]/div/div/div/div[2]

for indx in vc_indx:
    xpath = f'/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[1]/nav/div[4]/ul/li[{indx}]' #/div[2]/div[{indx}]/div/div/div[2]
            #/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[1]/nav/div[4]/ul/li[26]/div[2]/div[1]/div/div/div[2]
            #/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[1]/nav/div[4]/ul/li[26]/div[2]/div[2]/div/div/div[2]
    for i in range(1,int(limit2)):        
        try:
            member = driver.find_element(By.XPATH, value=(xpath+f'/div[2]/div[{i}]/div/div/div[2]'))
            voice_members_as_channels.append(member)
            print(member.text)
        except:
            print('element not found.')

for indx in vc_indx:
    i = 0
    limit2 = int(vc_with_members[i][1])
    for i in range(1,(int(limit2+1))):
        try:
            xpath = f'/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div/div[1]/nav/div[4]/ul/li[{indx}]/div[2]/div[{i}]/div/div/div[2]'
            member = driver.find_element(By.XPATH, value=(xpath))
            print(member.text)
            i += 1
        except:
            print('fck off!')
            i += 1

#use enumerate in voice channels and then just iterate on them. 
# for indx in range(1,int(limit2)+1):
#     try:
#         vc_member = driver.find_element_by_xpath(f'/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div[1]/div/div[2]/div[1]/nav/div[4]/ul/li[{}]/div[2]/div[{indx}]/div/div/div[2]')
#         voice_members_as_channels.append(vc_member)
#     except:
#         print('element not found.')

# print(voice_members_as_channels)
# print('v channels : ', voice_channels, '\n\n','vc names :', vc_names, '\n\n')
print( '\n\n','vc names :', vc_names, '\n\n')

driver.close()