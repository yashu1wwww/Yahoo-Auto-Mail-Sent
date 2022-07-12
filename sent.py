from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://login.yahoo.com/?.intl=in&.lang=en-IN&src=ym&activity=header-mail&pspid=2114723002&done=https%3A%2F%2Fin.mail.yahoo.com%2Fd%3F.intl%3Din%26.lang%3Den-IN%26pspid%3D2114723002%26activity%3Dheader-mail&add=1")

input=driver.find_element_by_xpath('//*[@id="login-username"]')
input.send_keys('google') #enter your yahoo mail address

input=driver.find_element_by_xpath('//*[@id="login-signin"]').click()

time.sleep(5)

input=driver.find_element_by_xpath('//*//*[@id="login-passwd"]')
input.send_keys('noway') #enter your yahoo exact password

time.sleep(5)

input=driver.find_element_by_xpath('//*[@id="login-signin"]').click()

input=driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div[1]/nav/div/div[1]/a').click()

input=driver.find_element_by_xpath('//*[@id="message-to-field"]')
input.send_keys('google@gmail.com')  #enter your receiver mail address

input=driver.find_element_by_xpath('//*[@id="mail-app-component"]/div/div/div/div[1]/div[3]/div/div/input')
input.send_keys('the more you learn the more you earn') #change what line you want to sent in it

input=driver.find_element_by_xpath('//*[@id="mail-app-component"]/div/div/div/div[2]/div[2]/div/button/span').click()

time.sleep(20)


