from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')
chrome_browser.maximize_window()
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title
assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('I am extra cool')

show_message_button = chrome_browser.find_element_by_class_name('btn-default')
show_message_button.click()

output_message = chrome_browser.find_element_by_id('display')
assert 'I am extra cool' in output_message.text

chrome_browser.close()
#chrome_browser.close() might need to call this twice
#chrome_browser.quit()