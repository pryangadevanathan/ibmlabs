flag = 0
print(2)
for i in range(2,101):
     for j in range(2,i):
         if i%j == 0:
             flag = 0
             break
         else:
             flag = 1
     if flag == 1:
         print(i)