import requests
from pyfiglet import Figlet
import urllib.request
import json
import colorama
from bs4 import BeautifulSoup
import os


def get_info_by_phone(phone):
    if os.path.isfile('info.txt'):
        os.remove('info.txt')

    service = "http://phoneradar.ru/phone/"
    link = service + phone

            
    def get_html(link, params=None):
        r = requests.get(link, params=params)
        return r 
    def parse():
        html = get_html(link)
        if html.status_code == 200:
            get_content(html.text)
        else:
            print(colorama.Fore.RED + '''Ошибка!
    Вы ввели некорректный номер телефона!
    Убедитесь, что введённый Вами номер, не содержит лишних символов.''')
            stop()
            go()
    def get_content(html):
        soup = BeautifulSoup(html, 'html.parser')
        result = soup.find('tbody')
        file = open("trash.tr", "w")
        file.write(result.text)
        file.close()
        with open("trash.tr") as a:
            with open("info.txt", 'a') as out:
                for line in filter(lambda x: x != '\n', a):
                    out.write(line)
        os.remove('trash.tr')           
        file1 = open("info.txt", "r")
        while True:
            line = file1.readline()
            if not line:
                break
            print(colorama.Fore.BLUE + line.strip())
        file1.close
    parse()
    go()
def get_info_by_ip(ip='127.8.0.1'):

    try:
        response = requests.get(url=f' http://ip-api.com/json/{ip}').json()
        data = {
        '[Айпи]': response.get('query'),
        '[Провайдер]': response.get('isp'),
        '[Организация]': response.get('org'),
        '[Страна]': response. get('country'),
        '[Регион]': response.get('regionName'),
        '[Город]': response.get('city'),
        '[ZIP]': response.get('zip'),
        '[Высота]': response.get('lat'),
        '[Долгота]': response.get('lon')
        
    }

        for k, v in data.items():
            print(colorama.Fore.BLUE + f'{k} : {v}')
    


    except requests.exceptions.ConnectionError:
        print(colorama.Fore.RED + "[!] Please check your connection!")
        go()
    go()
def distribution(number):
    if number == 1:
        print('\nВы выбрали пробив IP')
        ip = input('\nВведите IP: ')
        get_info_by_ip(ip=ip)
    elif number == 2:
        print('\nВы выбрали пробив номера')
        phone = input('\nВведите номер: ')
        get_info_by_phone(phone=phone)
    elif number == 3:
        print('\ncoming soon...')
        go()
    else:
        print(colorama.Fore.RED + 'НЕВЕРНЫЙ ВЫБОР' + colorama.Fore.RESET)

def go():
    number = int(input(colorama.Fore.YELLOW + '\nВыберите действие:\n[1]Пробив IP\n[2]Пробив номера\n[3]Пробив по номеру авто\n' + colorama.Fore.RESET + '\n'))


    distribution(number=number)
def main():

    preview_text = Figlet(font='slant')
    preview_text1 = Figlet(font='bubble')
    print(colorama.Fore.MAGENTA + preview_text.renderText('SEARCHER'))
    print(colorama.Fore.MAGENTA + preview_text1.renderText( '            by vila'))
    go()

    
if __name__ == '__main__':
    main()