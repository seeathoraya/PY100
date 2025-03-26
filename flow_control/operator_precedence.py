print(1 or 2 and 3)     # 1 truthy
print(0 or 2 and 3)     # 3 truthy
print(1 or 0 and 3)     # 1 truthy
print(1 or 2 and 0)     # 1 truthy
print(0 or 0 and 3)     # 0 falsy
print(0 or 2 and 0)     # 0 falsy
print(1 or 0 and 0)     # 1 truthy
print(0 or 0 and 0)     # 0 falsy

print(1 and 2 or 3)     # 2 truthy
print(0 and 2 or 3)     # 3 truthy
print(1 and 0 or 3)     # 3 truthy
print(1 and 2 or 0)     # 2 truthy
print(0 and 0 or 3)     # 3 truthy
print(0 and 2 or 0)     # 0 falsy
print(1 and 0 or 0)     # 0 falsy
print(0 and 0 or 0)     # 0 falsy