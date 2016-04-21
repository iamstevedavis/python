
##: Russian Peasant Algorithm

##: Multiply two numbers together
##: Multiply by 2, divide by 2, add numbers

##: 24 x 16

##: x 12   32
##: x 6    64
##: 3    128
##: 1    256
##: --------
##:      384

##:
##: Inputs -> two numbers
##: Output -> the solution to those two numbers multiplied together
##:           using Russian Peasant Algorithm

import time

CACHE = {}

def russian_peasant(num_one, num_two):
    key = (num_one, num_two)
    first_num = num_one
    second_num = num_two
    result = 0

    if key in CACHE:
        result = CACHE[key]
    else:
        while first_num > 0:
            if first_num % 2 == 1:
                result += second_num
            ##: You can shift here because you are
            ##: just multiplying and dividing by 2
            ##: eg. 4 << 1 == 8 (2^2 << 1 == 2^3)
            second_num = second_num << 1
            first_num = first_num >> 1
        CACHE[key] = result
    return result

def test_russian_peasant():
    ##: Test Run Time
    start_time = time.time()
    russian_peasant(999, 999)
    print 'Run Time (no cache) -> %f seconds' % (time.time() - start_time)

    ##: Test Run Time
    start_time = time.time()
    russian_peasant(999, 999)
    print 'Run Time (cache) -> %f seconds' % (time.time() - start_time)

    ##: Test Results
    assert russian_peasant(999, 999) == 998001
    assert russian_peasant(24, 16) == 384
    assert russian_peasant(20, 16) != 384

    return 'All Pass'

if __name__ == '__main__':
    test_russian_peasant()
