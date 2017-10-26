from bs4 import BeautifulSoup
from selenium import webdriver
import smtplib
import time
import heroku

# get the path for chromedriverserver
driver = webdriver.PhantomJS()

# navigate to the selection front page
driver.get(stat140_url)

# url
stat140_url = "http://classes.berkeley.edu/content/2018-spring-stat-140-001-lec-001"


while (True):
	# define the selection criteria
	driver.find_element_by_css_selector('div.update-enrollment > span').click()

	# finding enrollment
	p_selectors = driver.find_elements_by_css_selector("div.enrollment-update-target.enrollment-update-target > p")
	enrollment_data_selectors = p_selectors[1].find_elements_by_css_selector("span > strong")

	#current waitlist and waitlist cap
	waitlist_curr = int(enrollment_data_selectors[2].text)
	waitlist_cap = int(enrollment_data_selectors[3].text)

	if waitlist_curr < waitlist_cap:
		iserver = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login("averyyip99@gmail.com", "Luckyfast1")
		msg = "Stat 140 is now open"
		server.sendmail("averyyip99@gmail.com", "averyyip@berkeley.edu", msg)
		server.quit()
	print("Successful Run")
	time.sleep(600)