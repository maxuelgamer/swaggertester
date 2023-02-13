#MaxuelGamer#1529
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

alertbox = False

payl = "YOUR_PAYLOAD_HERE"

def send_message_to_discord(url):
    if url:
        webhook_url = "YOUR_WEBHOOK_HERE"
        message = f"```An alert has found at```\n{url}"

        try:
            response = requests.post(webhook_url, json={"content": message})
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error sending message to Discord: {e}")

with open("sites.txt", "r") as file:
    urls = file.readlines()

for url in urls:
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')

    try:
        driver = webdriver.Chrome(options=options)
    except Exception as e:
        print(f"Error launching Chrome: {e}")
        continue

    urlfinal = url.strip() + payl
    try:
        driver.get(urlfinal)
    except Exception as e:
        print(f"Error accessing URL: {e}")
        driver.quit()
        continue

    try:
        element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, "html"))
        )
        print(f"Testing at {url}")
        time.sleep(2)
        try:
            alert = driver.switch_to.alert
            alertbox = True
            send_message_to_discord(url)
        except:
            pass
    except Exception as e:
        print(f"Error locating HTML tag: {e}")
    finally:
        driver.quit()
