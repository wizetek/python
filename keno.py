# keno.py
# 2019-03-05 Tom Wizetek

from random import shuffle

while True:
    try:
        picks = int(input('How many Keno picks? (1-10): '))
    except:
        continue
    if 1 <= picks <= 10:
        break
    else:
        continue

# picks = 8
draws = 10000
scramble = 5

collection = list()
my_numbers = set()

print('Processing..', end='', flush=True)

while True:

    for n in range(draws):

        pool = [i for i in range(1, 71)]

        # shuffle(pool)
        ''' shuffle more than once '''
        [shuffle(pool) for i in range(scramble)]

        num = [pool.pop() for i in range(picks)]
        collection.extend(num)

    most_common = max(set(collection), key=collection.count)
    my_numbers.add(most_common)
    print(most_common, end='..', flush=True)

    if len(my_numbers) == picks:
        break

print('done\nFinal picks', sorted(my_numbers))
# EOF
