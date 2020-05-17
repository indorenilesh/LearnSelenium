from selenium import webdriver
import logging

browser = webdriver.Chrome('C:\\Nilesh Indore\\Projects\\LearnSelenium\\chromedriver_win32\\chromedriver')

browser.get("http://nukspdev11.bt.spindices.com:42802/grip/login.jsp")

report = open("report.txt","w")

def login():
    elem_userid = browser.find_element_by_id('userid')
    elem_userid.send_keys("nilesh")
    elem_userid.submit()
try:
    login()
    report.write("Login - Passed.\n")
except:
    logging.error("Not able to login.")
    report.write("Login - Failed.\n")

try:
    status_tab = browser.find_element_by_id("ui-id-4")
    status_tab.click()
    logging.info("Open status tab.")
    report.write("Status page - Passed.\n")
except:
    print("Status page failed.")
    report.write("Status page - Failed.\n")

browser.close()