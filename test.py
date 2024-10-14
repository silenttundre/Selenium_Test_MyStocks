import time
from colorama import Fore, Back, Style
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

GEVO_STOCK = 3.23
IPWR_STOCK = 13.30
IPWR_STOCK2 = 14.17
LUCID_STOCK = 18.93
PACB_STOCK = 9.90
GFS_STOCK = 65.90


def open_web(web, driver):
    """
    Opens the website url
    """
    driver.get(web)
    return driver


def key_strokes(driver, text):
    """
    Key in the given text
    """
    print("Typing {}...".format(text))
    ActionChains(driver) \
        .send_keys(text) \
        .key_down(Keys.ENTER) \
        .perform()


def back_key_stroke(driver):
    """
    Go back one page on browser
    """
    print("Pressing back a page...")
    driver.back()


def report_price(title, cur_price, bought_price):
    """
    Calculates the stock price difference of current and the bought price
    """
    print("============= {} ==================".format(title))
    print("Current: " + cur_price)
    calc_diff = round(float(cur_price) - bought_price, 2)
    print("Bought: " + str(bought_price))
    color = Fore.GREEN
    if calc_diff < 0.0:
        color = Fore.RED
    print("diff: " + color + str(calc_diff) + Style.RESET_ALL)


def get_stock_price(driver, ticker_name, bought_price):
    """
    Obtain the current stock price
    """
    text = '{} stock'.format(ticker_name)
    print("Obtaining {} price...".format(text))

    key_strokes(driver, text)

    price = driver.find_element(by='xpath', value='//div[contains(@data-attrid, "Price")]')
    curr_price = price.find_element(by='xpath', value='//span[contains(@jsname, "vWLAgc")]').text

    report_price(ticker_name, curr_price, bought_price)

    print("Obtained {} price".format(text))


def go_google_search(driver):
    """
    Go to the Google search page and click in the search box
    """
    time.sleep(2)
    back_key_stroke(driver)
    time.sleep(2)
    search_input = driver.find_element(by='xpath', value='//textarea[contains(@name, "q")]')
    search_input.click()


web = 'http://www.google.com'
#chrome_path = 'C:\\Selenium\\ChromeDriver\\chromedriver.exe'
# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(service=service, options=chrome_options)
# Didn't want to use the chrome webdriver because you have to add extra functions to keep the browser open
# Instead, we use Edge webdriver
edge_path = 'C:\\Selenium\\pythonTest\\EdgeDriver\\msedgedriver.exe'
service = Service(executable_path=edge_path)


driver = webdriver.Edge(service=service)

driver = open_web(web, driver)

get_stock_price(driver, "GFS", GFS_STOCK)

go_google_search(driver)

get_stock_price(driver, "IPWR", IPWR_STOCK)

go_google_search(driver)

get_stock_price(driver, "IPWR", IPWR_STOCK2)

go_google_search(driver)

get_stock_price(driver, "PACB", PACB_STOCK)

go_google_search(driver)

get_stock_price(driver, "GEVO", GEVO_STOCK)

go_google_search(driver)

get_stock_price(driver, "LCID", LUCID_STOCK)

driver.quit()


