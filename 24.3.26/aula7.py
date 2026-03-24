m = [ 
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ]

for i in m:
    print(i)


for n in list(range(len(m))):
     for p in list(range(len (m[n]))):
          print(m[n][p])

