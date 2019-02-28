# lottery
# 2019-02-28 Tom Wzietek

import random

# functions
def draw(n, p):
    s = set()

    while len(s) < n:
        r = random.randint(1, p)
        s.add(r)

    return(list(s))

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

    print('matching', matching_num)

# main
counter = 0

while True:
    counter += 1

    print()
    print('draw #', counter)

    sixFortyNine()

    result = len(matching_num)
    print('matched', result)

    # if result == 6:
    if result >= 4:
        years = counter / 52

        if counter < 5:
            days = counter * 7
            print(int(days), 'days')
        elif counter < 52:
            months = years * 12
            print(int(months), 'months')
        else:
            months = years % int(years) * 12
            print(int(years), 'years', int(months), 'months')

        input()
# eof
