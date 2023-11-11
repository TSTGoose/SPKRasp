import time
from assets import SPKRasp

spkrasp = SPKRasp()

if __name__ == '__main__':
    start_time = time.time()
    spkrasp.start_parser()
    print("--- %s seconds ---" % (time.time() - start_time))


