# lottery2.py
# 2019-03-01 Tom Wizetek

from random import shuffle

#
# FUNCTIONS
#

# def genNum(p):
#     num_pool = []
#     for i in range(1, p + 1):
#         num_pool.append(i)
#         # shuffle(num_pool)
#     ''' shuffle only once instead of every time when adding a number '''
#     shuffle(num_pool)
#     return num_pool
''' same as above but using a list comprehension '''
def genNum(p):
    num_pool = [i for i in range(1, p + 1)]
    shuffle(num_pool)
    return num_pool

# def drawNum(d):
#     num_draw = []
#     for i in range(d):
#         n = num_pool.pop()
#         num_draw.append(n)
#     return num_draw
''' same as above but using a list comprehension '''
def drawNum(d):
    num_draw = [num_pool.pop() for i in range(d)]
    return num_draw

def sixFortyNine():
    global lottery_pool, lottery_draw, lottery_bonus
    lottery_pool, lottery_draw, lottery_bonus = 49, 6, 1

def lottoMax():
    global lottery_pool, lottery_draw, lottery_bonus
    lottery_pool, lottery_draw, lottery_bonus = 49, 7, 1

def dailyKeno():
    global lottery_pool, lottery_draw, lottery_bonus
    lottery_pool, lottery_draw, lottery_bonus = 70, 20, 0

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
# MAIN LOOP
#

sixFortyNine()
# lottoMax()
# dailyKeno()
win_target = 5

counter = 1

while True:
    # LOTTERY DRAW
    num_pool = genNum(lottery_pool)
    num_draw = drawNum(lottery_draw)
    num_result = sorted(num_draw)
    # BONUS NUMBER
    num_draw = drawNum(lottery_bonus)
    num_result.extend(num_draw)
    # MY PICKS
    num_pool = genNum(lottery_pool)
    num_draw = drawNum(lottery_draw)
    num_picks = sorted(num_draw)

    print('\ndraw #', counter)
    if lottery_bonus == 0:
        print('winning ', num_result)
    else:
        print('winning ', num_result[:-1], 'bonus', num_result[-1])
    print('my picks', num_picks)

    # num_match = []
    # for i in num_picks:
    #     if i in num_result:
    #         num_match.append(i)
    ''' same as above but using a list comprehension '''
    num_match = [i for i in num_picks if i in num_result]

    num_correct = len(num_match)
    print(num_correct, 'match ', num_match)

    if num_correct >= win_target:
        howLong()
        input()

    counter += 1
# EOF
