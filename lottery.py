# lottery.py
# 2019-02-28 Tom Wizetek

import random

#
# functions
#
def draw(n, p):
    s = set()

    while len(s) < n:
        r = random.randint(1, p)
        s.add(r)

    return list(s)

def sixFortyNine():
    my_num = draw(6, 49)
    their_num = draw(7, 49)
    main_num = their_num[:-1]
    bonus_num = their_num[-1]

    print('my picks', sorted(my_num))
    print('winning ', sorted(main_num), '+ bonus', bonus_num)

    global matching_num
    matching_num = list()

    for a in my_num:
        for b in their_num:
            if a is b:
                matching_num.append(a)

    print('matching', sorted(matching_num))

def howLong():
    years = weeks / 52

    if weeks < 5:
        days = weeks * 7
        print(int(days), 'days')
    elif weeks < 52:
        months = years * 12
        print(int(months), 'months')
    else:
        months = years % int(years) * 12

        if months < 1:
            print(int(years), 'years')
        else:
            print(int(years), 'years,', int(months), 'months')

#
# main
#
weeks = 1

while True:
    print('\ndraw #', weeks)
    sixFortyNine()
    result = len(matching_num)
    print('correct', result)

    # if result == 6:
    if result >= 4:
        howLong()
        input()

    weeks += 1
# eof
