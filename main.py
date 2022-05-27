import telebot
import requests, random

weaval = {'clear': ('ясно', "https://yandex.ru/images/search?pos=11&from=tabbar&img_url=https%3A%2F%2Fpbs.twimg.com%2Fmedia%2FDlUt2zLWsAIhRay.jpg%3Alarge&text=%D1%81%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F+%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0+%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8&rpt=simage"),
'partly-cloudy' : ('малооблачно',"https://yandex.ru/images/search?pos=8&from=tabbar&img_url=https%3A%2F%2Fpbs.twimg.com%2Fmedia%2FE2R9GJGWUAAkacB.jpg&text=%D0%BC%D0%B0%D0%BB%D0%BE%D0%BE%D0%B1%D0%BB%D0%B0%D1%87%D0%BD%D0%BE&rpt=simage"),
'cloudy' : ('облачно с прояснениями', "https://yandex.ru/images/search?pos=1&from=tabbar&img_url=https%3A%2F%2Fi.obozrevatel.com%2Fnews%2F2020%2F4%2F8%2F330735main-1.jpg%3Fsize%3D1944x924&text=%D0%BE%D0%B1%D0%BB%D0%B0%D1%87%D0%BD%D0%BE+%D1%81+%D0%BF%D1%80%D0%BE%D1%8F%D1%81%D0%BD%D0%B5%D0%BD%D0%B8%D1%8F%D0%BC%D0%B8&rpt=simage"),
'overcast' : ('пасмурно',"https://yandex.ru/images/search?pos=1&from=tabbar&img_url=https%3A%2F%2Fsun9-68.userapi.com%2Fc858228%2Fv858228545%2F2083ae%2FEKazAVRk6EE.jpg&text=%D0%BF%D0%B0%D1%81%D0%BC%D1%83%D1%80%D0%BD%D0%BE+%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8&rpt=simage"),
'drizzle' : ('морось',"https://yandex.ru/images/search?pos=1&from=tabbar&img_url=https%3A%2F%2Fsun9-27.userapi.com%2Fc856524%2Fv856524141%2Fd2773%2F8u3iAlvLhMI.jpg&text=%D0%BC%D0%BE%D1%80%D0%BE%D1%81%D1%8C&rpt=simage"),
'light-rain' : ('небольшой дождь',"https://yandex.ru/images/search?pos=19&from=tabbar&img_url=https%3A%2F%2Fpbs.twimg.com%2Fmedia%2FETdQ6kdXsAEw4TV.jpg&text=%D0%BD%D0%B5%D0%B1%D0%BE%D0%BB%D1%8C%D1%88%D0%BE%D0%B9+%D0%B4%D0%BE%D0%B6%D0%B4%D1%8C&rpt=simage"),
'rain' : ('дождь', "https://yandex.ru/images/search?pos=23&from=tabbar&img_url=https%3A%2F%2Fpbs.twimg.com%2Fmedia%2FEzpzbRGXIAcU7lE.jpg&text=%D0%B4%D0%BE%D0%B6%D0%B4%D1%8C&rpt=simage"),
'moderate-rain' : ('умеренно сильный дождь',"https://yandex.ru/images/search?p=1&text=%D1%83%D0%BC%D0%B5%D1%80%D0%B5%D0%BD%D0%BD%D0%BE+%D1%81%D0%B8%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9+%D0%B4%D0%BE%D0%B6%D0%B4%D1%8C&pos=50&rpt=simage&img_url=https%3A%2F%2Fpbs.twimg.com%2Fmedia%2FE4UiUPcXwAMmjSU.jpg&from=tabbar"),
'heavy-rain' : ('сильный дождь',"https://yandex.ru/images/search?pos=18&from=tabbar&img_url=https%3A%2F%2Fpbs.twimg.com%2Fmedia%2FEzQrVv1VEAMzIRE.jpg&text=%D1%81%D0%B8%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9+%D0%B4%D0%BE%D0%B6%D0%B4%D1%8C&rpt=simage"),
'continuous-heavy-rain' : ('длительный сильный дождь',"https://yandex.ru/images/search?pos=3&from=tabbar&img_url=https%3A%2F%2Fpix.avax.news%2Favaxnews%2Fe0%2Fe2%2F0002e2e0.jpeg&text=%D0%B4%D0%BB%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9+%D1%81%D0%B8%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9+%D0%B4%D0%BE%D0%B6%D0%B4%D1%8C&rpt=simage"),
'showers' : ('ливень',"https://yandex.ru/images/search?pos=3&from=tabbar&img_url=https%3A%2F%2Ftuapse24.tv%2Fwp-content%2Fuploads%2F2021%2F12%2Fvoda-liven-dozhd.jpg&text=%D0%BB%D0%B8%D0%B2%D0%B5%D0%BD%D1%8C&rpt=simage"),
'wet-snow' : ('дождь со снегом',"https://yandex.ru/images/search?pos=2&from=tabbar&img_url=https%3A%2F%2Fpbs.twimg.com%2Fmedia%2FEnGvEP2WMAMgT40.jpg&text=%D0%B4%D0%BE%D0%B6%D0%B4%D1%8C+%D1%81%D0%BE+%D1%81%D0%BD%D0%B5%D0%B3%D0%BE%D0%BC&rpt=simage"),
'light-snow' : ('небольшой снег',"https://yandex.ru/images/search?pos=18&from=tabbar&img_url=https%3A%2F%2Fic.pics.livejournal.com%2Firnella%2F66734384%2F2552078%2F2552078_original.jpg&text=%D0%BD%D0%B5%D0%B1%D0%BE%D0%BB%D1%8C%D1%88%D0%BE%D0%B9+%D1%81%D0%BD%D0%B5%D0%B3&rpt=simage"),
'snow' : ('снег',"https://yandex.ru/images/search?pos=13&from=tabbar&img_url=https%3A%2F%2Fwallbox.ru%2Fwallpapers%2Fmain%2F201121%2Feefb4a48162159f591fb117987fee375.jpg&text=%D1%81%D0%BD%D0%B5%D0%B3+%D0%BF%D0%BE%D0%B4%D0%B0%D0%B5%D1%82&rpt=simage"),
'snow-showers' : ('снегопад',"https://yandex.ru/images/search?pos=1&from=tabbar&img_url=https%3A%2F%2Flviv.molbuk.ua%2Fuploads%2Fposts%2F2020-02%2F1580744629_mm3bpzwea4hvsghr.jpg&text=%D1%81%D0%BD%D0%B5%D0%B3%D0%BE%D0%BF%D0%B0%D0%BB&rpt=simage"),
'hail' : ('град',"https://yandex.ru/images/search?pos=16&from=tabbar&img_url=https%3A%2F%2Fphonoteka.org%2Fuploads%2Fposts%2F2021-07%2F1625675649_25-phonoteka-org-p-grad-art-krasivo-26.jpg&text=%D0%B3%D1%80%D0%B0%D0%B4&rpt=simage"),
'thunderstorm' : ('гроза',"https://yandex.ru/images/search?pos=1&from=tabbar&img_url=https%3A%2F%2Fotv-media.ru%2Fupload%2Fiblock%2F2d6%2F2d64af30dd093cc1f25a08600e63032b.jpg&text=%D0%B3%D1%80%D0%BE%D0%B7%D0%B0&rpt=simage"),
'thunderstorm-with-rain' : ('дождь с грозой',"https://yandex.ru/images/search?pos=4&from=tabbar&img_url=https%3A%2F%2Ftownsquare.media%2Fsite%2F204%2Ffiles%2F2015%2F03%2Fthink.jpg%3Fw%3D1200%26h%3D0%26zc%3D1%26s%3D0%26a%3Dt%26q%3D89&text=%D0%B4%D0%BE%D0%B6%D0%B4%D1%8C+%D1%81+%D0%B3%D1%80%D0%BE%D0%B7%D0%BE%D0%B9&rpt=simage"),
'thunderstorm-with-hail' : ('гроза с градом'"https://yandex.ru/images/search?pos=0&from=tabbar&img_url=https%3A%2F%2Ffotos.piqs.de%2F8%2F2%2Fd%2Fc%2F4%2Fb0168a01eacd40f3547e252d2f7056cc.jpg&text=%D0%B3%D1%80%D0%BE%D0%B7%D0%B0+%D1%81+%D0%B3%D1%80%D0%B0%D0%B4%D0%BE%D0%BC&rpt=simage"),}

otvet = {
  "now": 1470220206,
  "now_dt": "2016-08-03T10:30:06.238Z",
  "info": {
    "lat": 55.833333,
    "lon": 37.616667,
    "url": "https://yandex.ru/pogoda/moscow"
  },
  "fact": {
    "temp": 20,
    "feels_like": 21,
    "icon": "ovc",
    "condition": "drizzle",
    "wind_speed": 2,
    "wind_gust": 5.9,
    "wind_dir": "n",
    "pressure_mm": 745,
    "pressure_pa": 994,
    "humidity": 83,
    "daytime": "d",
    "polar": False,
    "season": "summer",
    "obs_time": 1470214800
  },
  "forecast": {
    "date": "2016-08-03",
    "date_ts": 1522702800,
    "week": 15,
    "sunrise": "04:38",
    "sunset": "20:31",
    "moon_code": 1,
    "moon_text": "moon-code-1",
    "parts": [
      {
        "part_name": "day",
        "temp_min": 20,
        "temp_max": 21,
        "temp_avg": 21,
        "feels_like": 23,
        "icon": "bkn_n",
        "condition": "cloudy",
        "daytime": "n",
        "polar": False,
        "wind_speed": 0.9,
        "wind_gust": 4,
        "wind_dir": "nw",
        "pressure_mm": 746,
        "pressure_pa": 995,
        "humidity": 81,
        "prec_mm": 0,
        "prec_period": 360,
        "prec_prob": 0
      },
    ]
  }
}

class ret:
    def __init__(self,message, b):
        self.message = message
        self.now_weather = b
    def ret_now(self):
        a = ''
        a += "Сейчас: {}\n".format(weaval[self.now_weather["fact"]["condition"]][0])
        a += "Температура {}°C, ощущается как {}°C\n".format(self.now_weather["fact"]["temp"], self.now_weather["fact"]["feels_like"])
        a += "Скорость ветра {} м\с направление {}\n".format(self.now_weather["fact"]["wind_speed"], self.now_weather["fact"]["wind_dir"].upper())
        a += "Давление {} мм рт. ст.\n".format(self.now_weather["fact"]["pressure_mm"])
        a += "Влажность {}%\n".format(self.now_weather["fact"]["humidity"])
        bot.send_photo(self.message.chat.id, weaval[self.now_weather["fact"]["condition"]][1])
        bot.send_message(self.message.chat.id, a)
    def ret_farther(self):
        a = ''
        a += "Данные на {}: {}\n".format(self.now_weather["forecast"]["date"], weaval[self.now_weather["forecast"]["parts"][0]["condition"]][0])
        a += "Температура {} - {}°C, ощущается как {}°C\n".format(self.now_weather["forecast"]["parts"][0]['temp_min'], self.now_weather["forecast"]["parts"][0]['temp_max'], self.now_weather["forecast"]["parts"][0]['feels_like'] )
        a += "Скорость ветра {} м\с направление {}\n".format(self.now_weather["forecast"]["parts"][0]["wind_speed"], self.now_weather["forecast"]["parts"][0]["wind_dir"].upper())
        a += "Давление {} мм рт. ст.\n".format(self.now_weather["forecast"]["parts"][0]["pressure_mm"])
        a += "Влажность {}%\n".format(self.now_weather["forecast"]["parts"][0]["humidity"])
        a += "Вероятонсть осадеов {}%".format(self.now_weather["forecast"]["parts"][0]['prec_prob'])
        bot.send_photo(self.message.chat.id, weaval[self.now_weather["forecast"]["parts"][0]["condition"]][1])
        bot.send_message(self.message.chat.id, a)

class commands:
    def __init__(self,message):
        self.message = message

    def start_message(self):
        bot.send_message(self.message.chat.id, 'Что мне снег, что мне зной,\nЧто мне дождик проливной,\nКогда погодаBot со мной')
        bot.send_message(self.message.chat.id, 'Вот что я могу:\nПри в воде я гадаю погоду в указаном месте.', reply_markup=keyboard1)

    def weather(self, a = True):
        #тут запрашиваю погоду
        if a:
            b = ret(self.message, otvet)
            b.ret_now()
        else:
            b = ret(self.message, otvet)
            b.ret_farther()

class log:
    def __init__(self, message):
        self.message = message
    def see(self):
        if self.message.text.lower() == 'покажи погоду на сейчас':
            b = commands(self.message)
            b.weather()
        elif self.message.text.lower() == 'прогноз':
            b = commands(self.message)
            b.weather(False)
        else:
            b = commands(self.message)
            b.weather(False)


token = '5298156959:AAFdbzvldtqmUI4vnM5yWGulTPI88eA5Nwk'
bot = telebot.TeleBot(token)

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Покажи погоду на сейчас', "Прогноз")


@bot.message_handler(commands=['start'])
def start_message(message):
    b = commands(message)
    b.start_message()

@bot.message_handler(content_types="text")
def new_message(message):
    b = log(message)
    b.see()


bot.infinity_polling()