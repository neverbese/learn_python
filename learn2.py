#threading 学習
import time
import threading
def print_info(func):
    def wrapper(*args, **kwargs):
        print('-' * 60)
        result = func(*args, **kwargs)
        print('-' * 60)
    return wrapper
        
def noodle():
    print(' 面を3分茹でます')
    time.sleep(3)
    print('   面が出来ました！')

def soup():
    print(' soupを準備します')
    time.sleep(2)
    print('   soupが準備出来ました')

def design():
    print(' 盛り付けします')
    time.sleep(1)
    print('   盛り付け出来ました')

print('ラーメンをつくります')
thread1 = threading.Thread(target=noodle)
thread2 = threading.Thread(target=soup)
thread3 = threading.Thread(target=design)

# 処理開始
thread1.start()
thread2.start()

# 処理が終わるまで待機
thread1.join()
thread2.join()

thread3.start()
thread3.join()
print('ラーメンが出来ました')