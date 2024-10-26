from threading import Thread
from datetime import datetime
from time import sleep


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
        print(f'Завершилась запись в файл {file_name}')


start = datetime.now()
write_words(10, 'task_1_examples/example1.txt')
write_words(30, 'task_1_examples/example2.txt')
write_words(200, 'task_1_examples/example3.txt')
write_words(100, 'task_1_examples/example4.txt')
print(f'Работа потоков {datetime.now() - start}')


start = datetime.now()
thr_first = Thread(target=write_words, args=(10, 'task_1_examples/example5.txt'))
thr_second = Thread(target=write_words, args=(30, 'task_1_examples/example6.txt'))
thr_third = Thread(target=write_words, args=(200, 'task_1_examples/example7.txt'))
thr_fourth = Thread(target=write_words, args=(100, 'task_1_examples/example8.txt'))

thr_first.start()
thr_second.start()
thr_third.start()
thr_fourth.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_fourth.join()
print(f'Работа потоков {datetime.now() - start}')
