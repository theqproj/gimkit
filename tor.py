import requests
import random
import time
import json
import logging
from concurrent.futures import ThreadPoolExecutor
from stem import Signal
from stem.control import Controller
import os
# Set logging level for 'stem' to WARNING to ignore debug and info logs
logging.getLogger('stem').setLevel(logging.WARNING)

os.system('''sudo service tor start
!sudo /etc/init.d/tor status''')

proxies = {
    'http': 'socks5h://localhost:9050',
    'https': 'socks5h://localhost:9050'
}

def renew_connection(msg):
  global lim
  if not lim:
    lim = True
    print(msg)
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password="d")
        controller.signal(Signal.NEWNYM)
        time.sleep(2)
        lim = False
        return


lim = False
counter = 0
def check(code: int):
    global counter
    counter += 1
    url = "https://www.gimkit.com/api/matchmaker/find-info-from-code"
    payload = {'code': str(code)}

    response = requests.post(url, data=payload, proxies=proxies)
    #print(response.json())
    if response.status_code == 200:
        xtra = ''
        if "useRandomNamePicker" in response.json():

          if json.loads(response.text)["useRandomNamePicker"] == True:
              xtra = '(note: namerator enabled)'
          print(f"{code} {xtra}")
        else:
          if response.status_code == 429:

            renew_connection('Rate limited, renewing...')
            #time.sleep(1)
            check(code)

def start_checking():
    global counter
    pins_to_check = [str(pin) for pin in range(10000, 999999)]
    random.shuffle(pins_to_check)
    with ThreadPoolExecutor(max_workers=40) as executor:
        for pin in pins_to_check:
            executor.submit(check, pin)
            if counter > 199:
                counter = 0

                renew_connection('Renewing circuit...')
            time.sleep(0.01)

print("Starting PIN hunting: (please ignore stem logs)")

start_checking()
