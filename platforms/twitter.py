import os
import sys
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def twitter_change_pfp(username, password, pfp):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=options)
    driver.get("https://twitter.com/login")
    
    # Type in username
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.NAME, "text"))
    ).send_keys(username)

    # Press Next
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]/div/span/span"))
    ).click()

    # Type in password
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.NAME, "password"))
    ).send_keys(password)
    
    # Press Login
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/span/span"))
    ).click()

    doesuserhave2fa = input("Does your account have 2FA? (y/n)")
    if doesuserhave2fa == "y":
        twitter2fa = input("Enter your 2FA code: ")
        driver.find_element(By.NAME, "text").send_keys(twitter2fa)
        
        # Press Next after 2FA
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/span/span"))
        ).click()
    
    driver.implicitly_wait(5)  # Twitter's weird    
    # Jump into their profile
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "[aria-label=Profile]"))
    ).click()
    
    # Select edit profile button
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="editProfileButton"]'))
    ).click()

    # Find the change profile picture element
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[aria-label="Add avatar photo"]'))
    ).click()
    
    pyautogui.write(os.path.abspath(pfp))
    pyautogui.press('return')
    driver.implicitly_wait(5)  # Twitter's weird    
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="applyButton"]'))
    ).click()
        
        
if __name__ == "__main__":
    twitter_username = sys.argv[1]
    twitter_password = sys.argv[2]
    pfp_path = sys.argv[3]
    
    twitter_change_pfp(twitter_username, twitter_password, pfp_path)