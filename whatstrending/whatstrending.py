from bs4 import BeautifulSoup
import requests
import sys
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as Soup

def get_day_trends(how_many, country_name):
    user_agent = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    trends_url = 'https://getdaytrends.com/' + country_name
    try:
        response = requests.get(trends_url, headers=user_agent)
        if response.status_code == 403:
            print('Request Denied')
            return
        soup = BeautifulSoup(response.text, 'lxml')

        trends_div = soup.find(id='trends') #latest trend card
        trends = list()
        for tr in trends_div.find_all('tr'):
            trend_text = tr.td.a.text.strip()
            trend_count = tr.find('span').text.strip()
            trends.append((trend_text, trend_count))

        trends_text = 'Top %s trends in %s\n' % (how_many, country_name.capitalize())
        for i in range(how_many):
            trends_text += trends[i][0], '-' * 3, trends[i][1] + "\n"
        return trends_text
    except Exception as ex:
        return str(ex)


def trends_24(country_name):

    trends_url = 'https://trends24.in/' + country_name
    try:
        response = urlopen(trends_url)
        soup = BeautifulSoup(response.read(), 'lxml')
        trends_text = 'Top trends in %s\n' % (country_name.strip().capitalize())
        trend_list = soup.find('ol')  # latest trend card
        for n, i in enumerate(trend_list.find_all('li')):
            if n < 40: # show just first 40 trends
                trend = i.find('a')
                trend_count = i.find('span')
                trends_text += (trend.text.strip() + ('' if trend_count is None else '-' * 3 + trend_count.text.strip() + ' Tweets')) + "\n"
        return trends_text
    except Exception as ex:
        return str(ex)

def google_trends():

    options = webdriver.FirefoxOptions()
    options.headless = True

    browser = webdriver.Firefox(options=options)
    browser.get('https://google.com')
    search_bar = browser.find_element(By.NAME, 'q')
    search_bar.send_keys(Keys.ARROW_DOWN)
    ul = browser.find_element(By.TAG_NAME, 'ul')
    soup = Soup(ul.get_attribute('innerHTML'), 'lxml')
    trending_text = "Trending Searches:\n"
    for li in soup.find_all('li'):
        trending_text += (li.text.strip().replace('Remove','')) + "\n"

    browser.close()
    return trending_text

def main():
    how_many = int(sys.argv[1])
    country = '-'.join(sys.argv[2:])
    if how_many < 0:
        print( google_trends().strip(),end='')
    elif how_many == 0:
        print(trends_24(country).strip(),end='')
    else:
        print(get_day_trends(how_many, country).strip(),end='')

if __name__ == "__main__":
    main()
