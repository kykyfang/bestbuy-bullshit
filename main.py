from checker import xbox_status, ps5_status, check_status
from time import sleep
from datetime import datetime

def main():
    while True:
        #3060s
        try:
            print('checking GTX 3060')
            check_status()
        except:
            print('error checking GTX3060s', datetime.now().strftime('%m-%d-%y %H:%M'))
        #PS5
        try:
            print('checking PS5')
            ps5_status()
        except:
            print('error checking PS5', datetime.now().strftime('%m-%d-%y %H:%M'))
        #xbox
        try:
            print('checking xbox')
            xbox_status()
        except:
            print('error checking Xbox', datetime.now().strftime('%m-%d-%y %H:%M'))
        #sleeping loop
        print('checked all status taking a nap')
        sleep(600)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
