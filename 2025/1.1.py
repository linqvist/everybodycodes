import utils

rows = utils.load_file('1.1')
names = rows[0].split(',')
moves = rows[1].split(',')

def delta(s):
    d = s[0]
    n = int(s[1:])
    return -n if d == 'L' else n

i = 0

for move in moves:
    d = delta(move)
    i += d
    if i < 0:
        i = 0
    if i >= len(names):
        i = len(names) -1
print(names[i])
        