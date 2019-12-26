from selenium import webdriver
import proxy_finder#file that was creted earlier
import json
import time
proxy_finder.get_proxy()
with open('proxy.json', 'r') as proxy_file:#read the json file containg the proxy details 
    proxy_dict = json.load(proxy_file)

def proxy_config(HOST, PORT):#setup firefox browser to use the proxies
    profile = webdriver.FirefoxProfile()
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.http", HOST)
    profile.set_preference("network.proxy.http_port", PORT)
    profile.set_preference("network.proxy.ssl", HOST)
    profile.set_preference("network.proxy.ssl_port", PORT)
    profile.set_preference("dom.webnotifications.enabled", False)
    driver = webdriver.Firefox(firefox_profile=profile)
    driver.get('https://www.facebook.com/')#open facebook anonymously 
    time.sleep(60)
    print('closing driver')
    driver.close()
with open("proxy.json")as proxy_file:
    proxy_information = json.load(proxy_file)
for i in range(0, len(proxy_information)+1):
    try:
        HOST_info = proxy_information['proxy_info'+str(i+1)]['host_ip'+str(i+1)]
        PORT_info = int(proxy_information['proxy_info'+str(i+1)]['port'+str(i+1)])
        #print(i+1)
        print (HOST_info)
        proxy_config(HOST_info, PORT_info)

    except:
        continue
