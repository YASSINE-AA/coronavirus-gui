import requests
from bs4 import BeautifulSoup
# Author Yassine Ahmed Ali


class CoronaCases:
    def __init__(self, country):
        result = requests.get(
            f"https://www.worldometers.info/coronavirus/{country}/")
        src = result.content
        soup = BeautifulSoup(src, features="html.parser")
        divs = soup.find_all("div", class_="maincounter-number")

        # Gets total cases
        total_cases = str(divs[0])
        total_cases_s = BeautifulSoup(total_cases, features="html.parser")
        total_cases = str(total_cases_s.find_all("span")[0])
        self.total_cases = total_cases.replace(
            '<span style="color:#aaa">', "").replace("</span>", "")

        # Gets deaths
        total_deaths = str(divs[1])
        total_deaths_s = BeautifulSoup(total_deaths, features="html.parser")
        total_deaths = str(total_deaths_s.find_all("span")[0])
        self.total_deaths = total_deaths.replace(
            "<span>", "").replace("</span>", "")

        # Gets recovered
        total_recovered = str(divs[2])
        total_recovered_s = BeautifulSoup(
            total_recovered, features="html.parser")
        total_recovered = str(total_recovered_s.find_all("span")[0])
        self.total_recovered = total_recovered.replace(
            "<span>", "").replace("</span>", "")
