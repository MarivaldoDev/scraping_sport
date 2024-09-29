import requests
import cowsay
from bs4 import BeautifulSoup
from datetime import datetime
from time import sleep
from dotenv import load_dotenv
from config.configs import SETTINGS
from send.enviar_email import envio
from colorama import init, Fore



# settings
load_dotenv()
init()



user = SETTINGS.get("USER")
password = SETTINGS.get("PASSWORD")



url = 'https://www.placardefutebol.com.br/time/sport/proximos-jogos'
request = requests.get(url)
soup = BeautifulSoup(request.content, 'html.parser')

games = soup.find_all('div', attrs={'class': 'match__lg_card'})

for game in games:
    while True:
        today = datetime.now()
        today_day = today.strftime("%d")
        today_br = today.strftime("%d/%m")

        team1 = game.find('div', attrs={'class': 'match__lg_card--ht-name text'}).get_text()
        team2 = game.find('div', attrs={'class': 'match__lg_card--at-name text'}).get_text()
        day_and_time = game.find('div', attrs={'class': 'match__lg_card--datetime'}).get_text().strip()
            
        _, date_and_time = day_and_time.split(' ', 1)
        separator = date_and_time.split()
        day = separator[0]
        # time = separator[1]
    
        if day == today_br:
            mensagem = f'{team1} x {team2} -- {day}'
            envio(user, password, mensagem)
            cowsay.tux(Fore.GREEN + mensagem + Fore.RESET)
            break
        elif 'amanhã' in day_and_time:
            new_day = int(today_day) + 1
            new_today_br = today.strftime(f"{str(new_day)}/%m")
            
            if new_today_br == today_br:
                mensagem = f'{team1} x {team2} -- {today_br}'
                envio(user, password, mensagem)
                cowsay.tux(Fore.GREEN + mensagem + Fore.RESET)
                break
            else:
                continue
        else:
            print(f'Data: {today_br} - ' + Fore.YELLOW + 'não tem jogo' + Fore.RESET)
            sleep(1)
