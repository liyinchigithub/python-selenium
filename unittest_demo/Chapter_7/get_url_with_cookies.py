def get_url_with_cookies(driver, target_url, file):
    cookies_file_path = file
    cookies_file = open(cookies_file_path, "r")
    cookies_str = cookies_file.readline()
    cookies_dict = json.loads(cookies_str)
    time.sleep(2)
    driver.get(target_url)
    driver.delete_all_cookies()
    for cookie in cookies_dict:
        for k in cookie.keys():
            if k == "expiry":
                cookie[k] = int(cookie[k])
        driver.add_cookie(cookie)

    time.sleep(2)
    driver.refresh()

if __name__ == '__main__':
    from selenium import webdriver
    import time
    import json
    from time import sleep

    driver = webdriver.Chrome()
    get_url_with_cookies(driver, 'http://mail.163.com/', 'mycookie.json')
    sleep(5)
    driver.quit()