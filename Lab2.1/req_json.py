import json
import requests
import sys
import time

# print(sys.argv[1])
# path = "https://lookup.binlist.net/" + sys.argv[1]
# bb = requests.get(path)
# print(bb.json())
# 344891225354387"

card_list = json.load(open("card1.json"))
# print(card_list)
bank_name = []
for i in card_list:
    card_num = i["CreditCard"]["CardNumber"]
    print(card_num)
    path = "https://lookup.binlist.net/" + str(card_num)
    bb = requests.get(path)
    # time.sleep(1)
    if 200 <= int(bb.status_code) <= 299:
        print(bb.json())
        bb_bank = bb.json()["bank"]
        if bb_bank:
            bank_name.append(bb_bank["name"])
    else: print(bb.status_code)
print(sorted(bank_name))
