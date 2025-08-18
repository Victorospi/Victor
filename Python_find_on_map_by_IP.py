import requests
from pyfiglet import Figlet
import folium

def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()

        if response.get('status') != 'success':
            print('[!] Invalid IP or API error')
            return

        data = {
            '[IP]' : response.get('query'),
            '[Int provider]' : response.get('isp'),
            '[Organization]' : response.get('org'),
            '[Country]' : response.get('country'),
            '[Region]' : response.get('regionName'),
            '[City]' : response.get('city'),
            '[ZIP]' : response.get('zip'),
            '[lat]' : response.get('lat'),
            '[lon]' : response.get('lon'),
        }

        for k,v in data.items():
            print(f'{k} : {v}')

        # создаём карту
        area = folium.Map(location=[response.get('lat'), response.get('lon')], zoom_start=10)

        # добавляем метку
        folium.Marker(
            [response.get('lat'), response.get('lon')],
            popup=f"{response.get('query')} - {response.get('city')}, {response.get('country')}"
        ).add_to(area)

        # сохраняем карту
        filename = f"{response.get('query')}_{response.get('city').replace(' ', '_')}.html"
        area.save(filename)
        print(f"[+] Map saved as {filename}")

    except requests.exceptions.ConnectionError:
        print('[!] Please check your connection!')

def main():
    try:
        preview_text = Figlet(font='slant')
        print(preview_text.renderText('IP INFO'))
    except ImportError:
        print("IP INFO")

    IP = input('Please enter a target IP: ')
    get_info_by_ip(ip=IP)

if __name__ == '__main__':
    main()
