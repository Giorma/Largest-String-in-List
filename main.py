l = []

for i in range(5):
    x = input("Enter String: ")
    l.append(x)

print(max(l, key=len))
