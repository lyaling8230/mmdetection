
import pickle
F = open('output.pkl', 'rb')

content = pickle.load(F)
f = open('output.txt', 'w')

# for n in content:
#     print(n)
#     print(n, file=f)

# 或者
for n in content:
    # print(n)
    f.write(str(n) + '\n')
