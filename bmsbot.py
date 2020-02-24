from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

#Adding Firefox Profile to the driver
#This is done to avoid the "Give location access" Prompt
fp = webdriver.FirefoxProfile('/home/chiren/.mozilla/firefox/s7q26fjl.default')
driver = webdriver.Firefox(fp)

#A dictonary to store all the theatres
theatre = {
	
}
def min():
	#list to store dictionaries
	l1 = []
	c = 1
	a = 1
	#URL of the movie / Will be automated in the next update
	driver.get("https://in.bookmyshow.com/buytickets/tanhaji-the-unsung-warrior-mumbai/movie-mumbai-ET00059932-MT/20200224")
	#while there exist a theatre the loop persists
	theatre_path = "/html/body/section[1]/div[2]/div/ul/li[{}]/div[1]/div[2]/div/a".format(a)
	while len(driver.find_elements_by_xpath(theatre_path)) > 0 :
		theatre_path = "/html/body/section[1]/div[2]/div/ul/li[{}]/div[1]/div[2]/div/a".format(a)
		#Get theatre name
		venue = driver.find_element_by_xpath(theatre_path)
		venue_name = venue.text
		#Dictionary storing venue name and timing along with prices
		venue_name = {
		"Name" : venue_name
	 	}
		timing_path1 = "/html/body/section[1]/div[2]/div/ul/li[1]/div[2]/div[2]/div"
		timing_text = driver.find_element_by_xpath(timing_path1)
		timing_value = timing_text.text
		print(timing_value)
		timing_path = "/html/body/section[1]/div[2]/div/ul/li[{}]/div[2]/div[2]/div[{}]/a".format(a,c)
		while len(driver.find_elements_by_xpath(timing_path)) > 0 :
			"""timing_value = driver.find_element_by_xpath(timing_path).text
			price_min = check_pricing("/html/body/section[1]/div[2]/div/ul/li[{}]/div[2]/div[2]/div[{}]".format(a,c))
			venue_name [timing_value] = price_min
			#print(venue_name)
			l1.append(venue_name)
			c = c + 1
			timing_path = "/html/body/section[1]/div[2]/div/ul/li[4]/div[2]/div[2]/div[{}]".format(c)"""
			element = driver.find_element_by_xpath("/html/body/section[1]/div[2]/div/ul/li[{}]/div[2]/div[2]/div[{}]/a".format(a,c))
			href_val = element.get_attribute("data-cat-popup")
			c = c + 1
			timing_path = "/html/body/section[1]/div[2]/div/ul/li[{}]/div[2]/div[2]/div[{}]/a".format(a,c)
			print(href_val)
		a = a + 1
		theatre_path = "/html/body/section[1]/div[2]/div/ul/li[{}]/div[1]/div[2]/div/a".format(a)
	print (venue_name)
	driver.close()

# def check_exists_by_xpath(xpath):
#     if (len(driver.find_elements_by_xpath(xpath))) > 0 :
# 				return True
#     else:
# 		return False

def check_pricing(xpath):
	price_num = []
	driver.find_element_by_xpath(xpath).click() 
	if(driver.find_elements_by_xpath('//*[@id="btnPopupAccept"]')>1):
		driver.find_element_by_xpath('//*[@id="btnPopupAccept"]').click()
	sleep(2)
	for i in range (1,3):
		for x in range (16,20):
			path = ("/html/body/div[{}]/strong/div[6]/div[2]/div[3]/div/div[{}]/span[2]".format(x,i))
			if (len(driver.find_elements_by_xpath(path))) > 0 :
				first_price_char = driver.find_element_by_xpath(path)
				first_price_char = first_price_char.text.split() 
				if(first_price_char):
					print(first_price_char)
					price_num.append(float(first_price_char[1]))
				else:
					price_char = driver.find_elements_by_class_name("seatP")
					for price in price_char:
						price_num = price.get_attribute("textContent").split()				
						print(price.get_attribute("textContent"))
						price_num.append(price_num[1])
	driver.back()
	return price_num

if __name__== "__main__":
	min()
