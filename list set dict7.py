numbers = [1,2,4,5,6,7]


even = [0]
for i in numbers:
    if i%2 == 0:
        even.append(i)
even = [i for i in numbers if i%2== 0]
print(even)


sqr_numbers = [i*i for i in numbers]
print(sqr_numbers)

s = set([1,2,3,4,5,2,3])
print(s)


even{i for i in numbers if i%2== 0}
even{i for i in s ifnumbers if i%2== 0}


cities = ["mumbai","ny","paris"]
countries = ["india","us","france"]
z = zip(cities, countries)
for a in z:
    print(a)
d = {city :countries for city, country in zip (cities, countries) }
print(d)
