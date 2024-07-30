from selenium import webdriver
from dotenv import load_dotenv
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
load_dotenv()
ACCOUNT_EMAIL =os.environ["ID"]
ACCOUNT_PASSWORD =os.environ["pass"]
Mobile_Number=os.environ["Mobile"]

# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(
    "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491"
    "&keywords=python%20developer"
    "&location=London%2C%20England%2C%20United%20Kingdom"
    "&redirect=false&position=1&pageNum=0"
)
sign_in=driver.find_element(By.LINK_TEXT,value="Sign in")
sign_in.click()
time.sleep(2)

your_email=driver.find_element(By.XPATH,value='//*[@id="username"]')
your_email.send_keys(ACCOUNT_EMAIL)
Your_pass=driver.find_element(By.XPATH,value='//*[@id="password"]')
Your_pass.send_keys(ACCOUNT_PASSWORD)

log_in=driver.find_element(By.XPATH,value='//*[@id="organic-div"]/form/div[3]/button')
log_in.click()

time.sleep(2)


close_tab=driver.find_element(By.ID,value="ember111")
close_tab.click()

time.sleep(2)
# job_dis=driver.find_element(By.XPATH,value='//*[@id="ember233"]/ul/li')
# job_dis.click()

apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
apply_button.click()

time.sleep(2)

my_number=driver.find_element(By.XPATH,value='//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3966924613-1884414289-phoneNumber-nationalNumber"]')
my_number.send_keys(Mobile_Number)
time.sleep(2)

my_address=driver.find_element(By.XPATH,value='//*[@id="single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3966924613-1884414297-text"]')
my_address.send_keys("Bangalore")
time.sleep(2)
next_buton=driver.find_element(By.CSS_SELECTOR,value="artdeco-button__text")
next_buton.click()

time.sleep(2)
next_button=driver.find_element(By.CSS_SELECTOR, value="footer button")
next_button.click()


