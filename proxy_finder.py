from selenium import webdriver
import json
def get_proxy():#function to pull proxies from the website"https://free-proxy-list.net/"and save it to a json file
    driver = webdriver.Edge()
    web = driver.get("https://free-proxy-list.net/")
    x = driver.find_elements_by_class_name("even")#visit the website for class name specified
    y = driver.find_elements_by_class_name("odd")
    even_d = ""
    odd_d = ""
    for i in range (0, len(x)):
        even_d = (x[i].text)+'\n'+ even_d
        odd_d = (y[i].text)+'\n'+odd_d
    all_list = str(even_d + odd_d)#join both lists at even place and odd place
    all_list = all_list.split('\n')
    all_list.remove('')
    all_list_Len = (len(all_list))+1
    proxy_list = []
    for i in range (1,all_list_Len):
        l = int(i-8)
        if(i%8 == 0):
            proxy_list.append(all_list[l:i])
    driver.quit()
    proxy_list_len = (len(proxy_list))
    proxy_dictionary = {}
    for j in range(0,proxy_list_len):#add proxies to a dictionary for easy information retrieval 
        proxy_dict = {'proxy_info'+str(j+1):{'host_ip'+str(j+1):proxy_list[j][0], 'port'+str(j+1):proxy_list[j][1], 'country'+str(j+1):proxy_list[j][3]}}
        proxy_dictionary.update(proxy_dict)
    with open('proxy.json', 'w') as file:#save required info into a json file
        json.dump(proxy_dictionary,file , indent=2)
