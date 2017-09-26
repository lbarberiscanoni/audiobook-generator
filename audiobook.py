from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import subprocess
import time
import os

def pdfToText():
    browser = webdriver.Chrome()
    browser.get("http://www.zamzar.com/convert/pdf-to-txt/")
    fileInpt = browser.find_element_by_id("inputFile")
    fileInpt.send_keys(os.getcwd() + "/project1.pdf")
    formatInpt = browser.find_element_by_id("toExtensionSel")
    formatInpt.send_keys("txt")
    emailInpt = browser.find_element_by_id("toEmail")
    emailInpt.send_keys("hllbck7@gmail.com")
    convertBtn = browser.find_element_by_id("uploadButton")
    convertBtn.click()
    time.sleep(2)
    browser.close()

def churn():
    subprocess.call("say -v Daniel -f test.txt -o bitch.m4a")

pdfToText()
