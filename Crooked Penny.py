import random

highest_count = 1
uses_count = 0
count = 1
success_streak = 0

while True:
    res = random.choice(['Worked!','Failed :('])

    if res == 'Worked!':
        count *= 2
        success_streak += 1
    elif res == 'Failed :(':
        count = 1
        success_streak = 0

    if count > highest_count:
        highest_count = count
        print('New highest score is ' + str(highest_count) + ' at attempt number ' + str(uses_count) + ' and its probability is about 1 to ' + str(100 * 0.5 ** success_streak) + ' with streak ' + str(success_streak))
        

    uses_count += 1

