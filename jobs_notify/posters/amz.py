from pyvirtualdisplay import Display
from selenium import webdriver
from sys import platform


def search_amz_newgrad_recent_10(url, key_words):
    # Only do virtual disply on linux system (supported by xvfb)
    if platform == "linux" or platform == "linux2":
        display = Display(visible=0, size=(800, 800))
        display.start()

    options = webdriver.chrome.options.Options()
    options.add_argument('--dns-prefetch-disable')
    driver = webdriver.Chrome(chrome_options=options)
    url = url or "https://www.amazon.jobs/en/teams/jobs-for-grads?sort=recent"
    content = ''
    try:
        driver.get(url)
        content = driver.find_elements_by_xpath(
            '//div[@class="search-page"][1]')[0].text
    finally:
        driver.close()

    for key_word in key_words:
        if key_word.lower() in content.lower():
            return True
    return False
