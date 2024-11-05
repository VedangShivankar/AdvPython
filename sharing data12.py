import multiprocessing


def calc_square(numbers, q):
    for n in numbers:
        q.put(n*n)

    print('inside process' + str(result))
 

if __name__ == "__main__":
    numbers = [2,3,8,9]
    q = multiprocessing.Queue()
    p1= multiprocessing.Process(target = calc_square, args=(numbers,q))
    p1.start()
    p1.join()

    while q.empty() is False:
        print(q.get())