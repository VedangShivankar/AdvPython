import time
import threading

arr = [2,3,8,9]
print("numbers:", arr)


def calc_square(numbers):
    print("calc square numbers")
    for n in numbers:
        time.sleep(0.2)
        print("square:", n*n)

def calc_cube(numbers):
    print("clac cube of numbers")
    for n in numbers:
        time.sleep(0.2)
        print('cube:', n*n*n)
 


t = time.time()

t1 = threading.Thread(target=calc_square, args=(arr,))
t2 = threading.Thread(target=calc_cube, args=(arr,))


t1.start()
t2.start ()

t1.join()
t2.join()


print("done in", time.time()-t)
