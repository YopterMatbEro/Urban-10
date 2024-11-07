import os
from threading import Thread
from datetime import datetime
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r') as f:
        for line in f:
            all_data.append(line)


if __name__ == '__main__':
    directory = './Files/'
    files = [os.path.join(directory, file) for file in os.listdir(directory)]

    # Линейный вызов
    # start = datetime.now()
    # thread1 = Thread(target=read_info, args=(files[0],))
    # thread2 = Thread(target=read_info, args=(files[1],))
    # thread3 = Thread(target=read_info, args=(files[2],))
    # thread4 = Thread(target=read_info, args=(files[3],))
    # thread1.start()
    # thread2.start()
    # thread3.start()
    # thread4.start()
    # thread1.join()
    # thread2.join()
    # thread3.join()
    # thread4.join()
    # print(str(datetime.now() - start) + ' (линейный)')

    # Многопроцессный вызов
    start = datetime.now()
    with Pool(processes=4) as pool:
        pool.map(read_info, files)
    print(str(datetime.now() - start) + ' (многопроцессорный)')
