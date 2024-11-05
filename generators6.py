def remote_control_next():
        yield "cnn"
        yield "espn"

itr = remote_control_next()

print(next(itr))


for c in remote_control_next():
    print(c)


def fib():
    a, b = 0,1
    while True:
        yield a
        a, b = b, a+b
for f in fib():
    if f > 1000000:
        break
    print(f)
