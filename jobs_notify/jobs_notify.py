from pyvirtualdisplay import Display
from selenium import webdriver
from sys import platform


def search_amz_newgrad_recent_10(locations):
    # Only do virtual disply on linux system (supported by xvfb)
    if platform == "linux" or platform == "linux2":
        display = Display(visible=0, size=(800, 800))
        display.start()

    driver = webdriver.Chrome()
    url = "https://www.amazon.jobs/en/teams/jobs-for-grads?sort=recent"
    content = ''
    try:
        driver.get(url)
        content = driver.find_elements_by_xpath(
            '//div[@class="search-page"][1]')[0].text
    finally:
        driver.close()

    for location in locations:
        if location.lower() in content.lower():
            return True
    return False


# Expected to be False currently
print(search_amz_newgrad_recent_10(['Vancouver']))
# Expected to be True currently
print(search_amz_newgrad_recent_10(['Santiago']))
