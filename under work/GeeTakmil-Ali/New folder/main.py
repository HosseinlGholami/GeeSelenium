from selenium import webdriver
from util import (init ,scrab_details ,
                  next_page,open_consumer,check_open_dar_entezar)

import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


internet_speed=0.3

next_page_Xpath='//*[@id="root"]/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div/div[3]/div'

TNK_TXT='اگر از استیکر ها راضی بودید ما رو به دوستاتون معرفی کنید .\n جووون جووون به شما  '

confirm_Xpath=   '/html/body/div[1]/div/div/div[3]/div/div[2]/div[2]/div/div/div/div/div[2]/div[2]'
Takmil_Xpath='//*[@id="orderModalStatus"]/div/div/div[5]'

edit_ersal_Xpath='/html/body/div[1]/div/div/div[3]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div/div[3]/div/div/div[5]/div'
edit_ersal_yes_Xpath='/html/body/div[1]/div/div/div[3]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/div[3]/div/div/div[2]'
input_edit_ersal_Xpath='/html/body/div[1]/div/div/div[3]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/div/div/div[1]/div[4]/textarea'
confrim_edit_ersal_Xpath='/html/body/div[1]/div/div/div[3]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]'
def init(driver):
    driver.get('https://geektori.ir/admin/orders')
    #loginPart
    INPUT_MAIL="farzam.mirmoeini@gmail.com"           
    PASS="AHAFA12345"
    InputMail=driver.find_element_by_id("username")
    InputMail.send_keys(INPUT_MAIL)
    InputPass=driver.find_element_by_id("password")
    InputPass.send_keys(PASS)
    InputPass.send_keys(Keys.RETURN)
    #define costomer_listapth
    COUSTOMER_XPATH='/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[1]/div[2]/div'
    Page_item=[COUSTOMER_XPATH+"["+str(i)+']' for i in range(21) ]
    return Page_item
                
def next_page(driver,page):
    driver.find_element_by_xpath(next_page_Xpath).click()
    return page + 1
def open_consumer(driver,Page_item,index):
    time.sleep(internet_speed)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,Page_item[index]))
        ).click()
def check_open_dar_entezar(driver,Page_item,i):
    x=Page_item[i]+'/div/div[6]/div'
    y=WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,x))
        ).text
    print(y)
    return y=='ارسال شده'

def scrab_details(driver):
    time.sleep(internet_speed)
    WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,Takmil_Xpath))
            ).click()
    time.sleep(internet_speed)
    WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,edit_ersal_Xpath))
            ).click()
    time.sleep(internet_speed)
    WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,edit_ersal_yes_Xpath))
            ).click()
    time.sleep(internet_speed)
    input_edit_ersal=WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,input_edit_ersal_Xpath))
            )
    input_edit_ersal.send_keys(TNK_TXT)
    time.sleep(internet_speed)
    WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH,confrim_edit_ersal_Xpath))
            ).click()
    time.sleep(internet_speed)
    WebDriverWait(driver, 10).until(
      EC.presence_of_element_located((By.XPATH,confirm_Xpath))
      ).click()

#     if Name in sefareshat_list:
#         WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.XPATH,ersal_Xpath))
#             ).click()
#         WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.XPATH,marsoole_Xpath))
#             ).click()
#         time.sleep(internet_speed)
#         InputMarsoole=WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.XPATH,inputmarso_Xpath))
#             )
#         InputMarsoole.send_keys(sefareshat_list[Name][0])
#         time.sleep(internet_speed)
#         InputMarsoole.send_keys(Keys.RETURN)
#         time.sleep(internet_speed)
  

driver = webdriver.Chrome('./chromedriver.exe')


#Xh : Excel handller ,DT:Date Time
Page_item=init(driver)

#local parameter
stop=False
page=1
end_page=0
i=0
while(stop==False):
    i +=1
    print (page , ' - ' , end_page,' : ', i)
    if check_open_dar_entezar(driver,Page_item,i) :
        try:
            open_consumer(driver,Page_item,i)
            scrab_details(driver)
            end_page = page +3
        except:
            print('stm wrong')
            
    #stop condition
    # stop =True
    if(i==20):
        i=0
        if(page==end_page):
            stop=True
        else:
            page=next_page(driver,page)
        
driver.quit()
