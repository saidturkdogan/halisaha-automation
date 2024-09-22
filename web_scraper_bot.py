from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import os
import pickle

class WebScraperBot:
    def __init__(self):
        # WebDriver'ı başlat
        options = Options()
        #options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-software-rasterizer")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-background-networking")
        options.add_argument("--disable-background-timer-throttling")
        options.add_argument("--disable-backgrounding-occluded-windows")
        options.add_argument("--disable-breakpad")
        options.add_argument("--disable-client-side-phishing-detection")
        options.add_argument("--disable-component-update")
        options.add_argument("--disable-default-apps")
        options.add_argument("--disable-domain-reliability")
        options.add_argument("--disable-features=AudioServiceOutOfProcess")
        options.add_argument("--disable-hang-monitor")
        options.add_argument("--disable-ipc-flooding-protection")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-prompt-on-repost")
        options.add_argument("--disable-renderer-backgrounding")
        options.add_argument("--disable-sync")
        options.add_argument("--force-color-profile=srgb")
        options.add_argument("--metrics-recording-only")
        options.add_argument("--no-first-run")
        options.add_argument("--safebrowsing-disable-auto-update")
        options.add_argument("--enable-automation")
        options.add_argument("--password-store=basic")
        options.add_argument("--use-mock-keychain")
        #options.add_argument("--user-data-dir=./chrome_profile")
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
        self.wait = WebDriverWait(self.driver, 30)
        self.load_cookies()


    def save_cookies(self):
        with open("cookies.pkl", "wb") as file:
            pickle.dump(self.driver.get_cookies(), file)

    def load_cookies(self):
        if os.path.exists("cookies.pkl"):
            self.driver.get("https://online.spor.istanbul/anasayfa")
            with open("cookies.pkl", "rb") as file:
                cookies = pickle.load(file)
                for cookie in cookies:
                    self.driver.add_cookie(cookie)
                self.driver.refresh()

    def navigate_and_fill(self):
        # Belirtilen web sayfasını açın
        self.driver.get("https://online.spor.istanbul/anasayfa")
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

        # ID'si closeModal olan butona tıklayın
        close_modal_button = self.wait.until(EC.element_to_be_clickable((By.ID, 'closeModal')))
        close_modal_button.click()

        # Belirtilen XPath'e tıklayın
        nav_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/form/header/div/nav/div/div/div/ul/li[4]/a')))
        nav_button.click()

        # Yeni sayfanın tamamen yüklenmesini bekleyin
        self.wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

        # ID'si txtTCPasaport olan input alanını bulun ve değer girin
        input_element = self.wait.until(EC.presence_of_element_located((By.ID, 'txtTCPasaport')))
        input_element.send_keys("21935167880")

        password_element = self.wait.until(EC.presence_of_element_located((By.ID, 'txtSifre')))
        password_element.send_keys("xajmeorDUNekG8N")

        login_button = self.wait.until(EC.element_to_be_clickable((By.ID, 'btnGirisYap')))
        login_button.click()

        close_modal_button = self.wait.until(EC.element_to_be_clickable((By.ID, 'closeModal')))
        close_modal_button.click()

        radio_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/form/section[1]/div/div/div/div/div/div/div/div[1]/div/div[1]/div/div/div[2]/input')))
        radio_button.click()

    def close(self):
        # Tarayıcıyı kapatın
        #self.driver.quit()
        pass

if __name__ == "__main__":
    bot = WebScraperBot()
    bot.navigate_and_fill()
    #bot.close()
    input("Press Enter to close the browser...")
    