import time
import random
from threading import Thread, Lock


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            cash = random.randint(50, 500)
            self.balance += cash
            print(f'Пополнение: {cash}. Баланс: {self.balance}.')
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            cash = random.randint(50, 500)
            print(f'Запрос на {cash}')
            if cash <= self.balance:
                self.balance -= cash
                print(f'Снятие: {cash}. Баланс: {self.balance}.')
                time.sleep(0.001)
            else:
                print(f'Запрос отклонён. Недостаточно средств.')
                self.lock.acquire()
                time.sleep(0.001)


if __name__ == '__main__':
    bk = Bank()
    th1 = Thread(target=Bank.deposit, args=(bk,))
    th2 = Thread(target=Bank.take, args=(bk,))
    th1.start()
    th2.start()

    th1.join()
    th2.join()

    print(f'Итоговый баланс: {bk.balance}')
