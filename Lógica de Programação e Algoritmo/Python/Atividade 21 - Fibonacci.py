v1 = int(input("Digite o número de termos que deseja ver: "))

t1 = 1
t2 = 1
con = 2

print(t1, end=" ")
print(t2, end=" ")

while con < v1:
    v2 = t1 + t2
    print(v2, end=" ")
    t1, t2 = t2, v2
    con += 1