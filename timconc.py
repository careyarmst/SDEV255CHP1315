import multiprocessing
import random

def itsnow(seconds):
    from datetime import datetime
    from time import sleep
    sleep(seconds)
    print('wait', seconds, 'seconds time is', datetime.utcnow())

if __name__ == '__main__':
    import random
    for n in range (3):
        seconds = random.random()
        process=multiprocessing.Process(target=itsnow, args=(seconds,))
        process.start()

