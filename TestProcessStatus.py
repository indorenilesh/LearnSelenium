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
    dashboard = browser.find_element_by_id("ui-id-1")
    processFrame = dashboard.find_element_by_id("processbody")
    for element in processFrame:
        counter = 1
        #colorcode = browser.find_element_by_xpath('//*[@id="processtbody"]/tr[1]/td[2]/img')
        #if colorCodeA in colorcode:
        if element in colorcode:
            logging.write("Process is UP.")
            report.write("Process is UP.")
        else:
            logging.write("Process is DOWN.")
            report.write("Process is DOWN.")
        counter += 1
except:
    logging.error("Not able to get process.")

browser.close()

