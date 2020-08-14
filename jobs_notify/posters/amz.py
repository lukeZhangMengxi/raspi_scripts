from pyvirtualdisplay import Display
from selenium import webdriver
from sys import platform
import time


amz_searched_contents = set()


def search_amz_newgrad_recent_10(url, key_words):
    # Only do virtual disply on linux system (supported by xvfb)
    if platform == 'linux' or platform == 'linux2':
        display = Display(visible=0, size=(800, 800))
        display.start()

    options = webdriver.chrome.options.Options()
    options.add_argument('--dns-prefetch-disable')
    driver = webdriver.Chrome(chrome_options=options)
    url = url or 'https://www.amazon.jobs/en/teams/jobs-for-grads?sort=recent'
    content = ''
    try:
        driver.get(url)
        time.sleep(1)   # Wait for the loading
        content = driver.find_elements_by_xpath(
            '//div[@class="search-page"][1]')[0].text
    finally:
        driver.close()

    has_key = False
    for key_word in key_words:
        if key_word.lower() in content.lower():
            has_key = True
            break
    
    if has_key:
        if content in amz_searched_contents:
            return False
        else:
            amz_searched_contents.add(content)
            return True

    return False


if __name__ == "__main__":
    print(search_amz_newgrad_recent_10(
        url='https://www.amazon.jobs/en/teams/jobs-for-grads?sort=recent',
        key_words=['Vancouver']
    ))
