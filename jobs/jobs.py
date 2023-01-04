from django.conf import settings
from frontend.models import B_users
import requests

def send_mail() -> None:
    users = B_users.objects.all()
    for i in users:
        balance = requests.get(
            'https://blockchain.info/q/addressbalance/' + i.Btc_address)
        # print(balance)
        if str(balance.text) == "0":
            print("no")
        else:
            print("yes")
        print("happy")
    print('it worked well')
