basket = {"orange","banana","apple","mango","orange","apple"}

print(type(basket))

a =  set()
a.add(1)
a.add(2)
print(a)

a = {}
print(type(a))


numbers = [1,2,3,4,2,3,4]
unique_numbers = set(numbers)
print(unique_numbers)
unique_numbers.add(5)

fs = frozenset(numbers)
print(fs)



x = {"a","b","c"}
print(  "a" in x)
y = {"a","e","f"}


print(x|y)
print(x&y)
