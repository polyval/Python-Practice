# -*- coding: utf-8 -*-
# @Date    : 2015-12-15 10:06:35
# @Author  : Lucien Zhou
import string


def initial(word):
    alphabet = str(word)[0]
    return alphabet.upper()


def check_dictionary(word):
    directory = 'F:/DICT/%s_terms.txt' % initial(word)
    list1 = []
    with open(directory, 'r') as dictionary:
        for line in dictionary.readlines():
            line = line.strip('\n')
            list1.append(line)

    try:
        i = list1.index(str(word))
        if i:
            count = 1
            index = i + 1
            while len(list1[index]) > 30 and count <= 5:
                print list1[index]
                count += 1
                index = i + count
        else:
            print "Not Found"
    except:
        print "Not Found"


def validate_word(word):
    while initial(word) not in string.uppercase:
        print "Hey, input a real word"
        word = raw_input("input again >> ")
    return word


while 1:
    input_word = raw_input("type word to search or press Enter to exit\n ")
    word_to_check = validate_word(input_word)
    check_dictionary(word_to_check)

raw_input('exit')
