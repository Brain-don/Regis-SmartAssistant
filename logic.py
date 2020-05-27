import re
import webbrowser
from pyowm import OWM
import datetime
import wikipedia
import response


def structure(command):
    if 'open' in command:
        reg_ex = re.search('open (.+)', command)
        url = 'https://www.'
        if reg_ex:
            domain = reg_ex.group(1)
            domain.replace(' ', '')
            url = f'{url}{domain}'
            webbrowser.open_new_tab(url)
        else:
            pass
    elif 'weather' in command:
        reg_ex = re.search('weather in (.*)', command)
        if reg_ex:
            city = reg_ex.group(1)
            owm = OWM(API_key='ab0d5e80e8dafb2cb81fa9e82431c1fa')
            obs = owm.weather_at_place(city)
            w = obs.get_weather()
            sky = w.get_status()
            tem = w.get_temperature(unit='fahrenheit')
            response.regis(
                f'''It is {sky} in {city} and the temperature is {int(tem['temp'])} degrees fahrenheit.''')
    elif 'time' in command:
        now = datetime.datetime.now()
        response.regis(f'The time is {(now.hour - 12)} {now.minute}')
