import threading
import datetime
def get_cubic(num):
    print(datetime.datetime.now())
    print("Cube: {}".format(num*num*num))

def get_inverse(num):
    print(datetime.datetime.now())
    print("Inverse: {}".format(1 / num))

if __name__ == '__main__':
    t1 = threading.Thread(target=get_cubic, args=(10,))
    t2 = threading.Thread(target=get_inverse, args=(10,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Done")