from time import sleep
from selenium import webdriver
from whois import whois
import csv

browser = webdriver.Firefox(executable_path=r"C:\\Phantomjs\\bin\\geckodriver.exe")
browser.get('http://www.google.com')
search = browser.find_element_by_name('q')
search.send_keys("created and hosted by danaweb\n")
links = []
sleep(5)
urls = browser.find_elements_by_css_selector('h3.r a')
sleep(5)
for l in urls:
    links.append(l.get_attribute('href'))
    l.get_attribute('href')
    sleep(1)

print(links)
bins = ['domain', 'expiry date', 'status']
c = len(links)
f = open("test.csv", "w", encoding="utf-8")
for l in range(0,c):
    b = whois(links[l])
    print (b.domain_name)
    f.write("{} \t{} \n".format(b.domain_name, b.status))   
f.close()
browser.quit()
