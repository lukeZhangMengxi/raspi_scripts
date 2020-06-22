import time
from pyvirtualdisplay import Display
from selenium import webdriver
from sys import platform


def search_ms_newgrad_ca(url=None, key_words=None):
    # Only do virtual disply on linux system (supported by xvfb)
    if platform == 'linux' or platform == 'linux2':
        display = Display(visible=0, size=(800, 800))
        display.start()

    options = webdriver.chrome.options.Options()
    options.add_argument('--dns-prefetch-disable')
    driver = webdriver.Chrome(chrome_options=options)
    url = url or 'https://careers.microsoft.com/students/us/en/canada-full-time-results'
    content = ''
    try:
        driver.get(url)
        time.sleep(1)   # Wait for the loading
        content = driver.find_elements_by_xpath('//li[@class="jobs-list-item"]')
    finally:
        driver.close()

    return len(content) > 0


if __name__ == "__main__":
    # Expected false, as the implemented time, there is no posting
    print(search_ms_newgrad_ca())
    
    # Expected true, as the implemented time, there are postings
    print(search_ms_newgrad_ca(url='https://careers.microsoft.com/students/us/en/search-results?qcountry=Canada'))
