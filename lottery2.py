# lottery2.py
# 2019-03-01 Tom Wizetek

from random import shuffle

#
# functions
#
def allNum(p):
    num_pool = []
    for i in range(1, p + 1):
        num_pool.append(i)
        shuffle(num_pool)
    return num_pool

def drawNum(d):
    num_draw = []
    for i in range(d):
        n = num_pool.pop()
        num_draw.append(n)
    return num_draw

def howLong():
    years = counter / 52
    if counter < 5:
        days = counter * 7
        print(int(days), 'days')
    elif counter < 52:
        months = years * 12
        print(int(months), 'months')
    else:
        months = years % int(years) * 12
        if months < 1:
            print(int(years), 'years')
        else:
            print(int(years), 'years and', int(months), 'months')

#
# main loop
#
lottery_pool = 49
lottery_draw = 6
lottery_bonus = 1
win_target = 4

counter = 1

while True:
    num_pool = allNum(lottery_pool)
    num_draw = drawNum(lottery_draw)
    num_result = sorted(num_draw)
    num_draw = drawNum(lottery_bonus)
    num_result.extend(num_draw)

    num_pool = allNum(lottery_pool)
    num_draw = drawNum(lottery_draw)
    num_picks = sorted(num_draw)

    print('\ndraw #', counter)
    print('winning ', num_result[:-1], 'bonus', num_result[-1])
    print('my picks', num_picks)

    # num_match = []
    # for i in num_picks:
    #     if i in num_result:
    #         num_match.append(i)
    ''' same as above but using list comprehension '''
    num_match = [i for i in num_picks if i in num_result]

    num_correct = len(num_match)
    print(num_correct, 'match ', num_match)

    if num_correct >= win_target:
        howLong()
        input()

    counter += 1
# eof
