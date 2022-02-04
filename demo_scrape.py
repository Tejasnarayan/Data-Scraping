from bs4 import BeautifulSoup
import requests


def find_hotel():
    html_text = requests.get('https://www.booking.com/city/in/bangalore.html?aid=306395;label=in-bangalore-GQKn2HZfAZqFZH7qpOhE1AS392710300029:pl:ta:p1700:p2:ac:ap:neg;ws=-GQKn2HZfAZqFZH7qpOhE1AS392710300029:pl:ta:p1700:p2:ac:ap:neg:fi:tiaud-1183547561427:kwd-101860043:lp9062069:li:dec:dm:ppccp=UmFuZG9tSVYkc2RlIyh9YZVcNNsENnH02-pWD53qm9c;ws=&gclid=CjwKCAiAl-6PBhBCEiwAc2GOVMSo87N5qnDQZ01p9AfD0kh-qzsOy7KMr8hQ9tqjmlf5puKvlBSY4xoCiSoQAvD_BwE').text
    soup = BeautifulSoup(html_text, 'lxml')
    hotels = soup.find_all('header', class_ = 'bui-spacer--medium')
    for index, hotel in enumerate(hotels):
        hotel_name = hotel.find('h3', class_ = 'bui-spacer--smaller').text
        loc = hotel.find('p', class_ = 'bui-card__subtitle').span.text
        with open(f'list/{index}.txt', 'w') as f:
            f.write(f"Hotel name: {hotel_name.strip()} \n")
            f.write(f"Location: {loc.strip()} \n")
        print(f'File Saved: {index}')

if __name__ == ' __main__':
    while True:
        find_hotel()
        