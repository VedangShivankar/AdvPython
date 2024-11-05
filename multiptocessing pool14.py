from multiprocessing import Pool
import time

def f(n):
    sum = 0
    for x in range(100):
        sum += x*x
    return sum

if __name__ == '__main__':
    t1 = time.time()
    p = Pool()
    result = p.map(f,range(10000))
    p.close
    p.join

    print("time", time.time()-t1)

    t2 = time.time()
    result = []
    for x in range(10000):
        result.append(f(x))

    print("time2", time.time()-t2)
    

#section 2


def f(n):
    return(n*n)

    p = Pool(processes=3)
    result = p.imap_unordered(f,[1,2,3,4,5])
    for n in result:
        print(n)