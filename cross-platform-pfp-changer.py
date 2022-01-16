import os
import sys  
import argparse 
from selenium import webdriver
import discord
import time
import threading
parser = argparse.ArgumentParser()
parser.add_argument("image", help="the profile pic you want to change to")
args = parser.parse_args() 
print(args.image)

# twitter code 
twitter_username = ""
twitter_password = ""
if twitter_username == "":
    print("Please enter your twitter username")
    sys.exit(1)
if twitter_password == "":
    print("Please enter your twitter password")
    sys.exit(1)
driver = webdriver.Chrome()
driver.get("https://twitter.com/login")
driver.implicitly_wait(0.5)
twitterloginusername = driver.find_element_by_name("text")
twitterloginusername.send_keys(twitter_username)
twitternextbutton = driver.find_element_by_class_name("css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-ywje51 r-usiww2 r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr r-13qz1uu")
twitternextbutton.click()
driver.implicitly_wait(0.5)
twitterloginpassword = driver.find_element_by_name("password")
twitterloginpassword.send_keys(twitter_password)
twitterloginbutton = driver.find_element_by_class_name("css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0")
twitterloginbutton.click()
driver.implicitly_wait(0.5)
doesuserhave2fa = input("Does your account have 2FA? (y/n)")
if doesuserhave2fa == "y":
    twitter2fa = input("Enter your 2FA code: ")
    twitter2fainput = driver.find_element_by_name("text")
    twitter2fainput.send_keys(twitter2fa)
    driver.implicitly_wait(0.5)
    profilebutton = driver.find_element_by_class_name("css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0")
    profilebutton.click()
    driver.implicitly_wait(0.5)
    editprofilebutton = driver.find_element_by_class_name("css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0")
    editprofilebutton.click()
    driver.implicitly_wait(0.5)
    profilepicturechangebutton = driver.find_element_by_class_name("css-901oao r-1awozwy r-jwli3a r-6koalj r-18u37iz r-16y2uox r-37j5jr r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0")
    handle_dialog(profilepicturechangebutton, args.image)
    def handle_dialog(element_initiating_dialog, dialog_text_input):
     def _handle_dialog(_element_initiating_dialog):
        _element_initiating_dialog.click() # thread hangs here until upload dialog closes
     t = threading.Thread(target=_handle_dialog, args=[element_initiating_dialog] )
     t.start()
     time.sleep(1) # poor thread synchronization, but good enough

    upload_dialog = webdriver.switch_to_active_element()
    upload_dialog.send_keys(dialog_text_input)
    upload_dialog.send_keys(selenium.webdriver.common.keys.Keys.ENTER) # the ENTER key closes the upload dialog, other thread exits
else:
        print("2FA not enabled skipping straight to changing profile picture")
        profilebutton = driver.find_element_by_class_name("css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0")
        profilebutton.click()
        driver.implicitly_wait(0.5)
        editprofilebutton = driver.find_element_by_class_name("css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0")
        editprofilebutton.click()
        driver.implicitly_wait(0.5)
        profilepicturechangebutton = driver.find_element_by_class_name("css-901oao r-1awozwy r-jwli3a r-6koalj r-18u37iz r-16y2uox r-37j5jr r-a023e6 r-b88u0q r-1777fci r-rjixqe r-bcqeeo r-q4m81j r-qvutc0")
