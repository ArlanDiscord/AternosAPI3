from flask import *
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium_stealth import stealth
from seleniumbase import Driver
import time
import warnings
import undetected_chromedriver

app = Flask(__name__)
@app.route("/status/", methods=['GET'])
def status():
	server_path = str(request.args.get('server'))
	username = str(request.args.get('username'))
	passwords = str(request.args.get('password'))
	driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
	stealth(driver,languages=["en-US", "en"],vendor="Mozilla/5.0",platform="Win64",webgl_vendor="Intel Inc.",renderer="Intel Iris OpenGL Engine",fix_hairline=True)
	driver = Driver(headless=True, uc=True)
	driver.get("https://aternos.org/go/")
	user = driver.find_element(by=By.CLASS_NAME, value="username")
	user.send_keys(username)
	password = driver.find_element(by = By.CLASS_NAME, value = "password")
	password.send_keys(passwords)
	data_set = 0
	driver.find_element(by = By.XPATH, value = '/html/body/div[3]/div/div/div[4]/div[4]/div[4]').click()
	tim = 0
	go = 0
	while True:
		time.sleep(0.1)
		tim = tim + 1
		if tim == 30 and driver.current_url == "https://aternos.org/go/":
			go = 0
			data_set = {"Error": f'Error with Connection to your Account, Error: " + {driver.find_element(by = By.XPATH, value = "/html/body/div[3]/div/div/div[4]/div[2]/span").text}'}
			break
		if not driver.current_url == "https://aternos.org/go/":
			go = 1
			break
	if go == 0:
		return data_set
	if go == 1:
		driver.find_element(by = By.XPATH, value = server_path).click()
		time.sleep(2)
		stat = driver.find_element(by = By.CLASS_NAME, value="statuslabel-label").text
		data_set = {"Status": f"{stat}"}
		print(stat)
		driver.quit()
		return data_set

if __name__ == "__main__":
	app.run(port=3000)