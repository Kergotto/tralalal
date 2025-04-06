from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd
import os
import time
import datetime
import csv
import re

chrome_driver_path = "C:\\Users\\Кирил\\PycharmProjects\\Amazon_webscraper\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("start-maximized")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

url = "https://www.amazon.com/Frigidaire-Beverage-Refrigerator-Experience-Cars-12V/dp/B0BGYK6SVQ/ref=sr_1_7?_encoding=UTF8&content-id=amzn1.sym.3ee8a8b8-12a8-4ba9-9886-109b6d3579a2&dib=eyJ2IjoiMSJ9.kdk_DANmsKfk1R3vHdaigrzOfo5IoL0Aj8zj_hjvbOhXFl2kTvONLEXf36VlwbWPW0huRz1FLm4EC90NvBVXD397LPiAmuoxKlvNjzpKaheIj4Z7hzjHzfkAMpivabelICWM7jV5SCtazyrz-DWQRczmn7HJxsU2XYLPKJPZApOpafyirEy1M--z6f-U33K6v1b6HMpQ70SfTYqlYCFQUp5d4KC1B8VPPWNUbp9E858IG9hvidy3v51WSXUgcBCFypFD_wdw2VkJ3TR42v2Ag97VXOuLCqcnafSheWa18lM.B3uVWuBq34WVZvlqQh9_3mArRFlO4xffwHZ2Zdlmv-E&dib_tag=se&keywords=gaming&pd_rd_r=b25cbc12-45aa-4600-8820-45398ea880ae&pd_rd_w=NXu6b&pd_rd_wg=VrHPN&qid=1743927960&sr=8-7&th=1"
driver.get(url)

time.sleep(3)

def parsing_data():
    title = driver.find_element(By.ID, "productTitle").text

    price = driver.find_element(By.CSS_SELECTOR, ".a-price .a-price-whole").text
    decimal = driver.find_element(By.CSS_SELECTOR, ".a-price .a-price-fraction").text
    currency_symbol = driver.find_element(By.CSS_SELECTOR, ".a-price-symbol").text
    full_price = f"{price},{decimal}{currency_symbol}"

    time.sleep(1)

    rates = driver.find_element(By.CSS_SELECTOR, '[data-hook="rating-out-of-text"]').text
    rating_value = int(re.search(r'(\d)', rates).group(1))
    stars = '★' * rating_value + '☆' * (5 - rating_value)

    today = datetime.date.today()

    file_exists = os.path.exists('AmazonDataset.csv')

    header = ['Title', 'Price', 'Rates', 'Date']
    data = [title, full_price[:-1], stars, today]
    with open('AmazonDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(header)
        writer.writerow(data)

    df = pd.read_csv('C:\\Users\\Кирил\\PycharmProjects\\Amazon_webscraper\\AmazonDataset.csv')
    print(f"\n{df}\n")
    time.sleep(86400)
    parsing_data()


parsing_data()
driver.quit()