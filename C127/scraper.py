from bs4 import BeautifulSoup
from selenium import webdriver
import csv
url= "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/"
browser=webdriver.Chrome("chromedriver.exe")
browser.get(url)

def scrape():
    headers=["name","light_years_from_earth","planet_mass","stellar_magnitude","discovery_date"]
    planet_data=[]
    
    for i in range(0,198):
        soup=BeautifulSoup(browser.page_source,"html.parser")
        all_ul_tags=soup.find_all("ul",attrs={"class","exoplanet"})
        for  ul_tags in all_ul_tags:
            li_tags= ul_tags.find_all("li")
            temp=[]
            for index,data_li in enumerate(li_tags):
                
                if index == 0:
                    temp.append(data_li.find_all("a")[0].contents[0])
                else:
                    temp.append(data_li.contents[0])
            planet_data.append(temp)
        browser.find_element_by_xpath('/html/body/div[2]/div/div[3]/section[2]/div/section[2]/div/div/article/div/div[2]/div[1]/div[2]/div[1]/div/nav/span[2]/a').click()
    with open("scaper.csv","w") as f:
        writer=csv.writer(f)
        writer.writerow(headers)
        writer.writerows(planet_data)

scrape()
    


