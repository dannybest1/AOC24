import pandas as pd 


df = pd.read_csv(r"C:\Users\DanielBest(RAPP)\Documents\personal\AOC2024\DAY_01\input.txt",delimiter='\s'\
    , header=None)


print(df.head())

df1 = df[0]
df2 = df[3]
# print(df2)

df1 = df1.sort_values()
df2 = df2.sort_values()

x = list(zip(df1,df2))


print(x)


x2 = [abs(i[0] - i[1]) for i in x]
print(sum(x2))

d_l = {}
for n in df2:
    if n in d_l.keys():
        d_l[n] = d_l[n]+1
    else:
        d_l[n]=1

# print(d_l)

y = [i*d_l.get(i,0) for i in df1]

print(sum(y))