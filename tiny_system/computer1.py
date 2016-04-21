import fake_database

from memcache import Memcache

cache = Memcache()

def print_name():
    return str(__name__)

def update_last_multiplied(num_one, num_two, result):
    key = 'lastFive'
    last_five_list = cache.get(key)
    if last_five_list:
        if len(last_five_list) >= 5:
            new_list = last_five_list[1:]
            new_list.append('{}x{}={}'.format(num_one, num_two, result))
            done = cache.set(key, new_list)
        else:
            last_five_list.append('{}x{}={}'.format(num_one, num_two, result))
            done = cache.set(key, last_five_list)
    else:
        done = cache.set(key, ['{}x{}={}'.format(num_one, num_two, result)])

def last_multiplied_handler():
    key = 'lastFive'
    last = cache.get(key)
    if last:
        return 'Last 5 = {}'.format(last)
    else:
        return 'Russian not Used Before'

def multiply_handler(num_one, num_two):
    key = (num_one, num_two)
    cached_answer = cache.get(key)
    if cached_answer:
        return '====================================Cached Result: {}'.format(cached_answer)
    else:
      result = fake_database.russian_peasant(num_one, num_two)
      update_last_multiplied(num_one, num_two, result)
      done = cache.set(key, result)
      return 'Latest Result: {}'.format(result)
      last_multiplied_handler()

if __name__ == '__main__':
    multiply_handler(2, 6)
    multiply_handler(32, 4)
    multiply_handler(45, 122)
    multiply_handler(56, 34)
    multiply_handler(3, 16)
    multiply_handler(3466, 78)
    multiply_handler(78, 9)
    multiply_handler(22, 789)
