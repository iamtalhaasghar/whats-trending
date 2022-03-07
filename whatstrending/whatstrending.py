def get_day_trends(how_many, country_name):
    from bs4 import BeautifulSoup
    import requests
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

        print('Top %s trends in %s' % (how_many, country_name.capitalize()))
        for i in range(how_many):
            print(trends[i][0], '-' * 3, trends[i][1])

    except Exception as ex:
        print(ex)


def trends_24(country_name):
    from bs4 import BeautifulSoup
    from urllib.request import urlopen
    trends_url = 'https://trends24.in/' + country_name
    try:
        response = urlopen(trends_url)
        soup = BeautifulSoup(response.read(), 'lxml')
        print('Top trends in %s' % (country_name.strip().capitalize()))
        trend_list = soup.find('ol')  # latest trend card
        for i in trend_list.find_all('li'):
            trend = i.find('a')
            trend_count = i.find('span')
            print(trend.text.strip() + ('' if trend_count is None else '-' * 3 + trend_count.text.strip() + ' Tweets'))
    except Exception as ex:
        print(ex)



def main():
    import sys
    how_many = int(sys.argv[1])
    country = '-'.join(sys.argv[2:])
    if how_many == 0:
        trends_24(country)
    else:
        get_day_trends(how_many, country)
    
if __name__ == "__main__":
    main()
