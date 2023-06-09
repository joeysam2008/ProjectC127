from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

START_URL = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser = webdriver.Chrome('chromedriver')
browser.get(START_URL)
time.sleep(10)

def scrape():
    headers = ["Proper_name", "distance", "mass", "radius"]
    star_data = []
    
    soup = BeautifulSoup(browser.page_source, "html.parser")
    temp_list = []

    for tr_tag in soup.find("table").find_all("tr"):
        td = tr_tag.find_all("td")
        row = [i.text.rstrip() for i in td]
        temp_list.append(row)

    name = []
    distance = []
    mass = []
    radius = []

    for i in range(1, len(temp_list)):
        name.append(temp_list[i][1])
        distance.append(temp_list[i][3])
        mass.append(temp_list[i][5])
        radius.append(temp_list[i][6])

    df = pd.DataFrame(
    list(zip(name, distance, mass, radius)),
    columns=["Star_name", "Distance", "Mass", "Radius"],
    )
    df.to_csv("data.csv")

scrape()


