from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
 
fp = webdriver.FirefoxProfile('/home/chiren/.mozilla/firefox/s7q26fjl.default')
driver = webdriver.Firefox(fp)
price_num = []
theatre = {
	
}
def min():
	driver.get("https://in.bookmyshow.com/buytickets/tanhaji-the-unsung-warrior-mumbai/movie-mumbai-ET00059932-MT/20200117")
	#for loop to be added here 
	venue = driver.find_element_by_xpath("/html/body/section[1]/div[2]/div/ul/li[1]/div[1]/div[2]/div/a")
	venue_name = venue.text
	timing = driver.find_element_by_xpath("/html/body/section[1]/div[2]/div/ul/li[1]/div[2]/div[2]/div[1]/a/div/div")
	timing_value = timing.text
	print(timing_value)
	driver.find_element_by_xpath("/html/body/section[1]/div[2]/div/ul/li[1]/div[2]/div[2]/div").click() 
	driver.find_element_by_xpath('//*[@id="btnPopupAccept"]').click()
	sleep(2)
	#price_path = ("/html/body/div[19]/strong/div[6]/div[2]/div[3]/div/div[{}]/span[2]".format(i))
	for i in range (1,3):
		path = ("/html/body/div[19]/strong/div[6]/div[2]/div[3]/div/div[{}]/span[2]".format(i))
		price_char = driver.find_element_by_xpath(path)
		price_char = price_char.text.split()
		price_num.append(float(price_char[1]))
		print(price_num)								
	sleep(1)
	min_price = min(price_num)
	theatre[venue_name] = min_price
	print(theatre)
	driver.close()

def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except Exception as inst:
        return False
    return True

if __name__== "__main__":
	min()
