#!/usr/bin/env python
#
# Author: Christian Rebischke
# License is MIT. Do what you want with it :)
#
# This little script logins into the studip server of the Technical University of Clausthal
# and tries to lookup a lecture.
from selenium import webdriver
import subprocess


def main(USERNAME, LECTURE_NAME, PASSWORD):
    # First we retrieve the password from the password store. The line starting with "result" may be different for you.
    # You can trigger every program you like with subprocess. More documentation here: https://docs.python.org/3/library/subprocess.html
    # Alternatively, you can just set the PASSWORD variable above, but this is NOT recommended.
    if PASSWORD == "":
        result = subprocess.run(['gopass', 'show', '-o', 'tu-clausthal/websites/studip.tu-clausthal.de'], stdout=subprocess.PIPE)
        PASSWORD = result.stdout.decode('utf-8')
    driver = webdriver.Firefox()
    driver.get("https://studip.tu-clausthal.de/index.php?again=yes")
    driver.find_element_by_id('loginname').send_keys(USERNAME)
    driver.find_element_by_id('password').send_keys(PASSWORD)
    driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[3]/form/button').click()
    driver.find_element_by_xpath('/html/body/div/div[2]/ul/li[7]/a').click()
    driver.find_element_by_xpath('/html/body/div/div[3]/nav/div/ul/li[2]/a').click()
    driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[1]/section/div[3]/div[2]/ul/li[1]/form/div/input[2]').send_keys(LECTURE_NAME)
    driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[1]/section/div[3]/div[2]/ul/li[1]/form/div/input[3]').click()
    if driver.find_element_by_xpath('/html/body/div/div[3]/div[2]/div[2]/div').is_displayed():
        print("No {} yet :( ... sending no email".format(LECTURE_NAME))
        # TODO: write your code for handling a "NOT FOUND" error here :)
    else:
        print("{} found. Sending notification".format(LECTURE_NAME))
        # TODO: write your code for handling a found lecture here.


# TODO: deploy script on linux server and trigger it via cronjob every few minutes.
if __name__ == "__main__":
    USERNAME = "your username" # Set your username here
    LECTURE_NAME = "The lecture to lookup" # Set your lecture name here
    PASSWORD = "" # WARNING: setting your personal password in plaintext is not recommended. Retrieve it via API from your password store or a separate config file
    main(USERNAME, LECTURE_NAME, PASSWORD)