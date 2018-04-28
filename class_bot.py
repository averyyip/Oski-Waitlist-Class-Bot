from selenium import webdriver
import smtplib
import time
import sys
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



output_email = "averyyip@berkeley.edu"
class_url = "http://classes.berkeley.edu/content/2018-fall-indeng-115-001-lec-001"


# get the path for chromedriverserver
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = GOOGLE_CHROME_BIN
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)

# navigate to the selection front page
driver.get(class_url)

# define the selection criteria
WebDriverWait(driver, 10).until(
	EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.update-enrollment'))
    ).click()

# finding enrollment
p_selectors = driver.find_elements_by_css_selector("div.enrollment-update-target.enrollment-update-target > p")
enrollment_data_selectors = p_selectors[1].find_elements_by_css_selector("span > strong")

#current waitlist and waitlist cap
waitlist_curr = int(enrollment_data_selectors[2].text)
waitlist_cap = int(enrollment_data_selectors[3].text)

if waitlist_curr < waitlist_cap:
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(os.environ.get("USERN"), os.environ.get("USERP"))
	msg = "Stat 140 is now open"
	server.sendmail(os.environ.get("USERN"), output_email, msg)
	server.quit()
	print("Class has open waitlist")

print("Successful Run")
sys.stdout.flush()