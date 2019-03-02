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
            print(int(years), 'years and', int(months), 'months')

#
# main loop
#
weeks = 1

while True:
    num_pool = allNum(49)
    num_draw = drawNum(6)
    num_result = sorted(num_draw)
    num_draw = drawNum(1)
    num_result.extend(num_draw)

    num_pool = allNum(49)
    num_draw = drawNum(6)
    num_picks = sorted(num_draw)

    print('\ndraw #', weeks)
    print('winning ', num_result[:-1], 'bonus', num_result[-1])
    print('my picks', num_picks)

    num_match = []
    for i in num_picks:
        if i in num_result:
            num_match.append(i)

    num_correct = len(num_match)
    print(num_correct, 'match ', num_match)

    # if num_correct == 6:
    if num_correct >= 4:
        howLong()
        input()

    weeks += 1
# eof
