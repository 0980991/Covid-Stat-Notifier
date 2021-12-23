from win10toast import ToastNotifier
import requests
import datetime
import json

class Main():
    def __init__(self):
        self.toaster = ToastNotifier()
        self.msg = self.dataToMessage()
        self.notifier()

    def dataToMessage(self):
        try:
            data = requests.get('http://corona-rest-api.herokuapp.com/Api/netherlands')

        except:
            print('You are not connected to the internet')
            data = None

        if data is not None:
            get_data = data.json()
            covid_stats = get_data['Success']

            title = f'Covid Netherlands / {datetime.date.today()}'
            msg = f'Cases Today: {covid_stats["todayCases"]}\nTotal Cases: {covid_stats["cases"]}\nDeaths: {covid_stats["deaths"]}\nRecovered {covid_stats["recovered"]}'
            return [title, msg]

    def notifier(self):
        self.toaster.show_toast(self.msg[0], self.msg[1], duration=10)


if __name__ == '__main__':
    Main()