# -*- coding: utf-8 -*-

'''

    Generator mock data-file for redis

'''


__author__='leasynoth'
__email__='kms.stan@gmail.com'
__DATE__='10.06.2022'


import random as rand
import hashlib as hl

DEFAULT_SIZE = 10

# ==========================
# ==== Global variables ====
# ==========================

str_count = 0
list_count = 0
set_count = 0
zset_count = 0
hash_count = 0

# ==========================


def str_hash(res_str):

    '''

        hash calculating for resourse string

    '''
    hash_object = hl.sha512(res_str)
    res = hash_object.hexdigest()

    return res


def str_generate(count):

    '''

        srting mocking data generate

    '''

    res_value = 'python_test_value_' + str(count)
    byte_res_value = bytes(res_value, encoding='utf-8')
    res = str_hash(byte_res_value)

    return res


def list_set_generate(size=DEFAULT_SIZE):

    '''

        list (set) mocking data generate

    '''

    res = []

    for elem in range(size):

        res.append(str_generate(elem))

    return res


def zset_generate(size=DEFAULT_SIZE):

    '''

        structured set mocking data generate

    '''

    res = []

    for elem in range(size):

        item = str(elem) + ' ' + str_generate(elem)
        res.append(item)

    return res


def hash_ganerate(size=DEFAULT_SIZE):

    '''

        hash mocking data generate

    '''

    res = []

    for elem in range(size):

        res_key = 'test_key:' + str(elem) + ':string'
        res_value = str_generate(elem)
        res.append(res_key + ' ' + res_value)

    return res


def struct_generate(size=DEFAULT_SIZE):

    '''

        generate base structure data's

        0 - string
        1 - list
        2 - set
        3 - zset
        4 - hash

    '''

    global str_count, list_count, set_count, zset_count, hash_count

    res = []

    for _ in range(size):

        res.append(rand.randint(0, 4))

    final_arr = []

    for elem in res:

        if (elem == 0):

            final_res_key = 'test_key:' + str(str_count) + ':string'
            final_res_value = str_generate(str_count)
            final_arr.append('set ' + final_res_key + ' ' + final_res_value)
            str_count += 1

        elif (elem == 1):

            final_res_key = 'test_key:' + str(list_count) + ':list'
            final_res_value = ''

            for list_item in list_set_generate():

                final_res_value += ' ' + list_item

            final_arr.append('lpush ' + final_res_key + ' ' + final_res_value)
            list_count += 1

        elif (elem == 2):

            final_res_key = 'test_key:' + str(set_count) + ':set'
            final_res_value = ''

            for set_item in list_set_generate():

                final_res_value += ' ' + set_item

            final_arr.append('sadd ' + final_res_key + final_res_value)
            set_count += 1

        elif (elem == 3):

            final_res_key = 'test_key:' + str(zset_count) + ':zset'
            final_res_value = ''

            for zset_item in zset_generate():

                final_res_value += ' ' + zset_item

            final_arr.append('zadd ' + final_res_key + final_res_value)
            zset_count += 1

        elif (elem == 4):

            final_res_key = 'test_key:' + str(hash_count) + ':hash'
            final_res_value = ''

            for hash_item in hash_ganerate():

                final_res_value += ' ' + hash_item

            final_arr.append('hmset ' + final_res_key + final_res_value)
            hash_count += 1

    return final_arr


def file_gen(file_name, data):

    with open(file_name, 'w') as f:

        for elem in data:

            f.write(str(elem) + '\n')

    f.close()


def main():

    name = 'redis_mock_data_file.txt'
    amount_records = 5

    file_gen(name, struct_generate(amount_records))


if (__name__ == '__main__'):

    main()