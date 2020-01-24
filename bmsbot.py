from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

#Adding Firefox Profile to the driver
#This is done to avoid the "Give location access" Prompt
fp = webdriver.FirefoxProfile('/home/chiren/.mozilla/firefox/s7q26fjl.default')
driver = webdriver.Firefox(fp)

#A dictonary to store all the 
theatre = {
	
}
def min():
	l1 = []
	c = 1
	driver.get("https://in.bookmyshow.com/buytickets/tanhaji-the-unsung-warrior-mumbai/movie-mumbai-ET00059932-MT/20200117")
	#for loop to be added here 
	venue = driver.find_element_by_xpath("/html/body/section[1]/div[2]/div/ul/li[1]/div[1]/div[2]/div/a")
	venue_name = venue.text
	venue_name = {
	"name" : venue_name
	 }
	timing_path = "/html/body/section[1]/div[2]/div/ul/li[1]/div[2]/div[2]/div"
	timing_text = driver.find_element_by_xpath(timing_path)
	timing_value = timing_text.text
	print(timing_value)
	while len(driver.find_elements_by_xpath(timing_path)) > 0 :
		price_min = check_pricing("/html/body/section[1]/div[2]/div/ul/li[4]/div[2]/div[2]/div[{}]".format(c))
		venue_name [timing_value] = price_min
		print(venue_name)
		l1.append(venue_name)
		c = c+1
		timing_path = "/html/body/section[1]/div[2]/div/ul/li[4]/div[2]/div[2]/div[{}]".format(c)
	driver.close()

# def check_exists_by_xpath(xpath):
#     if (len(driver.find_elements_by_xpath(xpath))) > 0 :
# 				return True
#     else:
# 		return False

def check_pricing(xpath):
	price_num = []
	driver.find_element_by_xpath(xpath).click() 
	driver.find_element_by_xpath('//*[@id="btnPopupAccept"]').click()
	sleep(2)
	for i in range (1,3):
		for x in range (16,20):
			path = ("/html/body/div[{}]/strong/div[6]/div[2]/div[3]/div/div[{}]/span[2]".format(x,i))
			if (len(driver.find_elements_by_xpath(path))) > 0 :
				first_price_char = driver.find_element_by_xpath(path)
				first_price_char = first_price_char.text.split() 
				if(first_price_char):
					price_num.append(float(first_price_char[1]))
				else:
					price_char = driver.find_elements_by_class_name("seatP")
					for price in price_char:
						price_num = price.get_attribute("textContent").split()				
						#print(price_num[1])
						price_num.append(price_num[1].get_attribute("textContent"))
	driver.back()
	return price_num

if __name__== "__main__":
	min()
