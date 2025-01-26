from bs4 import BeautifulSoup
import requests



def rf():
    url = "https://www.investing.com/rates-bonds/india-10-year-bond-yield"

    
    response = requests.get( url)
    soup = BeautifulSoup(response.content, "html.parser")

    div = soup.find_all("div", attrs={"data-test":"instrument-price-last"})
    return float(div[0].text.strip())/100


