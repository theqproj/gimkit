import requests
import random
import time
import json
from concurrent.futures import ThreadPoolExecutor
counter = 0
def check(code: int):
    global counter 
    counter += 1
    url = "https://www.gimkit.com/api/matchmaker/find-info-from-code"
    payload = {'code': str(code)}

    response = requests.post(url, data=payload)

    if response.status_code == 200 or json.loads(response.text)["code"]==200:
        xtra = ''
        if json.loads(response.text)["useRandomNamePicker"] == True:
             xtra = '(note: namerator enabled)'
        print(f"{code} {xtra}")
        
    else:
        if response.status_code == 429 or json.loads(response.text)["code"]==429:
            print('429')
            return
    


def start_checking():
    global counter
    pins_to_check = [str(pin).zfill(6) for pin in range(100000, 999999)]
    random.shuffle(pins_to_check)
    with ThreadPoolExecutor(max_workers=20) as executor:
        for pin in pins_to_check:
            executor.submit(check, pin)
            if counter > 99:
                counter = 0
                print('Checked 100 games')


print("Starting PIN finding... \n\n")
start_checking()
