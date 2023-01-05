from django.conf import settings
from frontend.models import B_users
import requests

def send_mail() -> None:
    users = B_users.objects.all()
    for i in users:
        response = requests.get(
            'https://chain.api.btc.com/v3/address/' + i.Btc_address +'/tx')
        response = response.json()
        # print(response["data"]["balance"])
        # if str(response.data.balance) == "0":
        #     print("no")
        # else:
        #     print("yes")
        # print("happy")
    print('it worked well')
