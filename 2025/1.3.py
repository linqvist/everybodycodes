import utils

rows = utils.load_file('1.3')
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
for d in temp:
    d %= len(names)
    names[0], names[d] = names[d], names[0]
print(names[0])