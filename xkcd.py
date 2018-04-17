import datetime
import time
import webbrowser
import requests
import pickle
from random import randint

save = "C:\\Developer\\Pickles\\XKCD.pickle"
day = int(datetime.datetime.today().weekday())

def saver(pageNumber):
    with open(save, 'wb') as handle:
        pickle.dump(pageNumber, handle)
        
def load():
    with open(save, 'rb') as handle:
        a = pickle.load(handle)
    return a
time.sleep(60*5)
newpage = int(load())
site = str("https://www.xkcd.com/" + str(newpage))

if day == 0 or day == 2 or day == 4:
    while True:
        request = requests.get(site)
        if request.status_code == 200:
            webbrowser.open("https:\\www.xkcd.com", new=2)
            newpage += 1
            saver(newpage)
            break
        time.sleep(60)
else:
    randpage = (randint(1, newpage))
    randsite = ("https://xkcd.com/" + str(randpage))
    webbrowser.open(randsite)