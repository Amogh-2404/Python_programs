meow = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]
new_string = []

for zing in meow:
    new = zing
    for i in range(0, len(meow)):
        if meow.index(zing) == i:
            continue
        else:
            if zing[0] == meow[i][0]:
                temp = new
                new = temp + meow[i]
                temp2=meow[i]
                continue
            else:
                continue
    new_string.append(new)
# for i in new_string:
#     for z in range(new_string.index(i)):
#         if i==new_string[i]:
#             new_string.remove(new_string.index(i))
nnn =[]
for j in new_string:
  for i in range(len(new_string)):
     if (list(j)).sort() == (list(new_string[i])).sort():
        new = new_string.pop(i)
print(nnn)