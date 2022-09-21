from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time

active_item='/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]/div/div/div[1]/div/div/div[2]/div/div/div/div[1]'
price_page='/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]/div/ul/div[3]'

mahdoodiyat_item='/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div[4]/div'
mahdoodiyat_check='/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]/div/div/div[3]/div/div/div[3]/div/div/div/div/div[1]/div[2]/div/div/span'
mahdoodiyat_submit='/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div/div/div/div[1]/div/div[1]/div/div/div[3]/div/div/div[3]/div/div/div/div/div[2]/div[2]'


go_page='/html/body/div[1]/div/div[4]/div/div[2]/div[1]/div/div[2]/div/div[2]/div/input'
submit_item='/html/body/div[1]/div/div[4]/div/div[2]/div[2]/div/div/div/div/div[2]/div[3]'

sticker_tag='/html/body/div[1]/div/div[4]/div/div[1]/div[2]/div[3]/div/div[2]/div[1]'
sticker_active_tag='/html/body/div[1]/div/div[4]/div/div[1]/div[2]/div[2]/div/div[2]/div[1]'


HighPrice='/html/body/div[1]/div/div/div[3]/div/div[1]/div[2]/div[4]/div/div[2]/div[2]'

def init(driver):
    driver.get('https://geektori.ir/admin/products')
    #loginPart
    INPUT_MAIL="farzam.mirmoeini@gmail.com"           
    PASS="AHAFA12345"
    time.sleep(10)
    InputMail=driver.find_element_by_id("username")
    InputMail.send_keys(INPUT_MAIL)
    InputPass=driver.find_element_by_id("password")
    InputPass.send_keys(PASS)
    InputPass.send_keys(Keys.RETURN)
    
def ret_page_item(x):
    x=x%5+13
    return '/html/body/div[1]/div/div[4]/div/div[2]/div[1]/div/div[1]/div['+str(x)+']'
          
def deactive(driver,i):
    loc=ret_page_item(i)
    driver.implicitly_wait(1)
    x=WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,loc))
            )
    action=ActionChains(driver)
    action.move_to_element(x)
    action.perform()
    driver.implicitly_wait(3)
    WebDriverWait(driver, 10).until(                
            EC.element_to_be_clickable((By.XPATH,loc+'/div/div[4]/div[1]/div[1]'))
            ).click()
    driver.implicitly_wait(1)
    time.sleep(0.1)
    driver.find_element_by_xpath(active_item).click()
    time.sleep(0.1)
    driver.find_element_by_xpath(price_page).click()
    time.sleep(0.1)
    driver.find_element_by_xpath(mahdoodiyat_item).click()
    time.sleep(0.1)
    driver.find_element_by_xpath(mahdoodiyat_check).click()
    time.sleep(0.1)
    driver.find_element_by_xpath(mahdoodiyat_submit).click()
    time.sleep(0.1)
    driver.find_element_by_xpath(submit_item).click()
    time.sleep(0.1)


def Go_page(driver,page):
    x=WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,go_page))
        )
    x.send_keys(Keys.CONTROL + "a")
    x.send_keys(page)
    x.send_keys(Keys.RETURN)
    

def select_sticker(driver):
    driver.implicitly_wait(5)

    x=WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.ID,'filter-2'))
            )
    action=ActionChains(driver)
    action.move_to_element(x)
    action.click(x)
    action.perform()
    WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH,sticker_tag))
            ).click()
    action=ActionChains(driver)
    action.move_to_element(x)
    action.click(x)
    action.perform()    
    
def select_active(driver):
    driver.implicitly_wait(5)

    x=WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.ID,'filter-1'))
            )
    action=ActionChains(driver)
    action.move_to_element(x)
    action.click(x)
    action.perform()
    WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH,sticker_active_tag))
            ).click()
    action=ActionChains(driver)
    action.move_to_element(x)
    action.click(x)
    action.perform()    
    
def select_HighPrice(driver):
    driver.implicitly_wait(5)

    x=WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.ID,'sort'))
            )
    action=ActionChains(driver)
    action.move_to_element(x)
    action.click(x)
    action.perform()
    WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH,HighPrice))
            ).click()
    action=ActionChains(driver)
    action.move_to_element(x)
    action.click(x)
    action.perform()    