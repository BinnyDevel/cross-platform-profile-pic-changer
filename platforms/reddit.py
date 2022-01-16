from selenium import webdriver
import sys

reddit_username = ""
reddit_password = ""
if not reddit_username or not reddit_password:
    print("Please set your reddit username and password")
    sys.exit(1)
driver = webdriver.Chrome()
driver.get("https://www.reddit.com/login")
username = driver.find_element_by_name("username")
driver.keyboard.send_keys(reddit_username)
password = driver.find_element_by_name("password")
driver.keyboard.send_keys(reddit_password)
loginbutton= driver.find_element_by_xpath("/html/body/div/main/div[1]/div/div[2]/form/fieldset[5]/button")
loginbutton.click()
doesuserhave2fa = input("Does your account have 2FA? (y/n)")
if doesuserhave2fa == "y":
    reddit2fa = input("Enter your 2FA code: ")
    reddit2fainput = driver.find_element_by_name("otp")
    reddit2fainput.send_keys(reddit2fa)
    submit2fabutton = driver.find_element_by_xpath("/html/body/div/main/div[1]/div/div[2]/form/fieldset[5]/button")
    submit2fabutton.click()
    redditprofilebuttondropdown = driver.find_element_by_id("USER_DROPDOWN_ID")
    redditprofilebuttondropdown.click()
    redditprofilebutton = driver.find_element_by_xpath("/html/body/div[29]/div/a[2]")
    redditprofilebutton.click()
    redditchangepfpbutton = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[2]/div/div[1]/div/div[2]/div/label/div[2]")
    redditchangepfpbutton.click()
else:
 print("Reddit 2FA not enabled skipping to changing profile picture")
 redditprofilebuttondropdown = driver.find_element_by_id("USER_DROPDOWN_ID")
 redditprofilebuttondropdown.click()
 redditprofilebutton = driver.find_element_by_xpath("/html/body/div[29]/div/a[2]")
 redditprofilebutton.click()
 redditchangepfpbutton = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[2]/div/div[1]/div/div[2]/div/label/div[2]")
 redditchangepfpbutton.click()