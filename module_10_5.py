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
    start = datetime.now()

    threads = [Thread(target=read_info, args=(file,)) for file in files]
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(str(datetime.now() - start) + ' (линейный)')

    # Многопроцессный вызов
    # start = datetime.now()
    #
    # with Pool(processes=4) as pool:
    #     pool.map(read_info, files)
    #
    # print(str(datetime.now() - start) + ' (многопроцессорный)')
