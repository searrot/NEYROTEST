from selenium.webdriver import Firefox
from getpass import getpass
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import urllib
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image_dataset_from_directory
import time

batch_size = 32
image_size = (254, 254)


driver = Firefox()
driver.get('https://twitter.com/login')
time.sleep(3)
username = driver.find_element_by_xpath('//input[@name="session[username_or_email]"]')
username.send_keys("@IKudryavtzeff")
time.sleep(3)
my_password = 'Persik228'
password = driver.find_element_by_xpath('//input[@name="session[password]"]')
password.send_keys(my_password)
password.send_keys(Keys.RETURN)
time.sleep(3)
driver.get('https://twitter.com/IKudryavtzeff')
time.sleep(2)
card = driver.find_element_by_xpath('//div[@data-testid="tweet"]')
time.sleep(3)
time_post = card.find_element_by_xpath('.//time').get_attribute('datetime')
last_time = time_post



def get_image(card):
    try:
        img = card.find_elements_by_xpath('./div[2]/div[2]//img')
        if len(img) > 1:
            src = img.get_attribute('src')
            urllib.request.urlretrieve(src, f'trig.jpg')
        else:
            for element in img:
                src = element.get_attribute('src')
                urllib.request.urlretrieve(src, f'trig.jpg')
    except:
        pass

def get_text(card):
    try:
        text = card.find_element_by_xpath('.//div[2]/div[2]/div[1]').text
        print(text)
    except:
        pass
#//div[2]/div[2]

def check_tweets(l_t):
    last_time = l_t
    while True:
        card = driver.find_element_by_xpath('//div[@data-testid="tweet"]')

        time.sleep(3)
        #card = cards[0]
        time_post = card.find_element_by_xpath('.//time').get_attribute('datetime')

        if time_post != last_time:
            get_text(card)
            get_image(card)
        
        last_time = time_post
        driver.refresh()
        time.sleep(2)

check_tweets(last_time)
'''while True:
    card = driver.find_element_by_xpath('//div[@data-testid="tweet"]')
    time_post = card.find_element_by_xpath('.//time').get_attribute('datetime')

    if time_post != last_time:
        print(get_text())
        get_image()

    last_time = time_post'''
