#!/usr/bin/env python3

'''
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.
'''

cont = True
i = 0
while cont:
    i += 1
    tmp = str(i**2)
    if len(tmp) > 19:
        cont = False
        print ('oups {}'.format(i))
    if len(tmp) == 19:
        if tmp[0] == '1' and tmp[2] == '2' and tmp[4] == '3' and tmp[6] == '4'\
                and tmp[8] == '5' and tmp[10] == '6' and tmp[12] == '7'\
                and tmp[14] == '8' and tmp[16] == '9' and tmp[18] == '0':
            cont = False
            print (i)
