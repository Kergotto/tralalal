from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Path to your ChromeDriver
chrome_driver_path = "C:\\Users\\Кирgit ил\\PycharmProjects\\Amazon_webscraper\\chromedriver-win64"

# Set up options
options = Options()
# options.add_argument("--headless")  # Run without opening a browser window
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")

# Start the driver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# Open the Amazon product page
url = "https://www.amazon.com/Frigidaire-Beverage-Refrigerator-Experience-Cars-12V/dp/B0BGYK6SVQ/ref=sr_1_7?_encoding=UTF8&content-id=amzn1.sym.3ee8a8b8-12a8-4ba9-9886-109b6d3579a2&dib=eyJ2IjoiMSJ9.kdk_DANmsKfk1R3vHdaigrzOfo5IoL0Aj8zj_hjvbOhXFl2kTvONLEXf36VlwbWPW0huRz1FLm4EC90NvBVXD397LPiAmuoxKlvNjzpKaheIj4Z7hzjHzfkAMpivabelICWM7jV5SCtazyrz-DWQRczmn7HJxsU2XYLPKJPZApOpafyirEy1M--z6f-U33K6v1b6HMpQ70SfTYqlYCFQUp5d4KC1B8VPPWNUbp9E858IG9hvidy3v51WSXUgcBCFypFD_wdw2VkJ3TR42v2Ag97VXOuLCqcnafSheWa18lM.B3uVWuBq34WVZvlqQh9_3mArRFlO4xffwHZ2Zdlmv-E&dib_tag=se&keywords=gaming&pd_rd_r=b25cbc12-45aa-4600-8820-45398ea880ae&pd_rd_w=NXu6b&pd_rd_wg=VrHPN&qid=1743927960&sr=8-7&th=1"
driver.get(url)

# Give the page time to load (important!)
time.sleep(3)

try:
    price = driver.find_element(By.CLASS_NAME, "a-offscreen").text
    print("Price:", price)
except Exception as e:
    print("Could not find price:", e)

# Quit the driver
driver.quit()
