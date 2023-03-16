from random import*
my_set = set()
while len(my_set) < 7:
    my_set.add(randint(1,49))
print(*sorted(my_set))
