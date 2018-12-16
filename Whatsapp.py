from selenium import webdriver
chromedriver = "/home/anchal/Infinitemsg/chromedriver"
browser = webdriver.Chrome(chromedriver)
browser.get('http://web.whatsapp.com')
input("press enter after scanning the qr code")
name = browser.find_element_by_xpath('//span[contains(text(),"WhatsAppName")]')
name.click()
box = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
N = 20
for i in range(N):

      box.send_keys('Hii, This is automation babes ;-)')
      browser.find_element_by_class_name('_35EW6').click()
