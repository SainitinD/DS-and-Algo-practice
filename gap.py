inp = [1,2,3,2,3,4]

skill_cap = (sum(inp)/len(inp))*2
h = {}
res = []
for i in range(len(inp)):
    if (skill_cap - inp[i]) in h:
        res.append([inp[i], int(skill_cap-inp[i])])
    else:
        h[inp[i]] = False

cnt = 0
for x,y in res:
    cnt = cnt + x*y
print(res)
print(cnt)