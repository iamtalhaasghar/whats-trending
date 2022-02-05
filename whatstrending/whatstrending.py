def scrap_trends(country_name):
    from bs4 import BeautifulSoup
    from urllib.request import urlopen

    trends_url = 'https://trends24.in/' + country_name
    try:
        response = urlopen(trends_url)
        soup = BeautifulSoup(response.read(), 'lxml')

        trend_list = soup.find('ol') #latest trend card
        for i in trend_list.find_all('li'):
            trend = i.find('a')
            trend_count = i.find('span')
            print(trend.text +"<=>"+ ('unknown' if trend_count == None else trend_count.text + ' Tweets'))
    except Exception as ex:
        print(ex)

def main():
    import sys
    args = '+'.join(sys.argv[1:])
    print('Fetching Trends for: ' + (args if len(args.strip()) != 0 else 'Worldwide'))
    scrap_trends(args)
    
if __name__ == "__main__":
    main()
