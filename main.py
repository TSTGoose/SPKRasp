import time
from assets import SPKRasp

spkrasp = SPKRasp()

if __name__ == '__main__':
    start_time = time.time()
    print("--- %s seconds ---" % (time.time() - start_time))


