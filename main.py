import os
import requests
import cowsay
from bs4 import BeautifulSoup
from datetime import datetime
from time import sleep
from dotenv import load_dotenv
from send.enviar_email import envio



# settings
load_dotenv()

config = {
    "USER":os.getenv("USER", None),
    "PASSWORD":os.getenv("PASSWORD", None),
}


user = config.get("USER")
password = config.get("PASSWORD")




url = 'https://www.placardefutebol.com.br/time/sport/proximos-jogos'
request = requests.get(url)
soup = BeautifulSoup(request.content, 'html.parser')

games = soup.find_all('div', attrs={'class': 'match__lg_card'})

for game in games:
    while True:
        today = datetime.now()
        today_br = today.strftime("%d/%m")

        team1 = game.find('div', attrs={'class': 'match__lg_card--ht-name text'}).get_text()
        team2 = game.find('div', attrs={'class': 'match__lg_card--at-name text'}).get_text()
        day_and_time = game.find('div', attrs={'class': 'match__lg_card--datetime'}).get_text().strip()
            
        _, date_and_time = day_and_time.split(' ', 1)
        separator = date_and_time.split()
        day = separator[0]
        time = separator[1]
    
        if day == today_br:
            mensagem = f'{team1} x {team2} -- {day} {time}'
            envio(user, password, mensagem)
            cowsay.tux(mensagem)
            break
        else:
            print(f'Data: {today_br} - não tem jogo')
            sleep(1)
