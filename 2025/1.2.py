import utils

rows = utils.load_file('1.2')
names = rows[0].split(',')
moves = rows[1].split(',')

def delta(s):
    d = s[0]
    n = int(s[1:])
    return -n if d == 'L' else n

i = 0
temp = []

for move in moves:
    temp.append(delta(move))
i = sum(temp) % len(names)
print(names[i])