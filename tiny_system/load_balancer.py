import computer1
import computer2
import computer3
import time

#import itertools

SERVERS = [computer1, computer2, computer3]

def get_server():
    try:
        return next(get_server.s)
    except StopIteration:
        get_server.s = iter(SERVERS)
        return next(get_server.s)
setattr(get_server, 's', iter(SERVERS))

#CYCLE = itertools.cycle(SERVERS)
#def get_server():
#    global CYCLE
#    return CYCLE.next()

# Another option
# Yield does not return the value right away,
# it holds onto it and continues where it left off
# def get_server():
#     def f():
#         while True:
#             i = SERVERS.pop(0)
#             SERVERS.append(i)
#             yield i
#     return next(f())

if __name__ == '__main__':
    from random import randint
    # simulate requests
    for i in range(1000000):
        # generate some requested numbers
        z = randint(1, 21)
        a = randint(1, 99)#[23, 45, 123, 45, 34, 23, 12][z%7]
        b = randint(1, 99)#[89, 12, 875, 12, 90, 56, 73][z%7]

        # get a server from the load balancer to handle the request
        server = get_server()

        # print results
        print server.print_name()
        print server.multiply_handler(a, b)
        print server.last_multiplied_handler()
        print ' '
        #time.sleep(.5)
