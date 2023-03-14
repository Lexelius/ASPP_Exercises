import animals

# 1 d,e.
m = animals.Mammals()
m.printMembers()

b = animals.Birds()
b.printMembers()

f = animals.Fish()
f.printMembers()


# 1 f.
"""
$ mkdir animals/harmless
$ mkdir animals/dangerous
# For the sake of the Hand-In, I'm copying (instead of moving) bird.py and 
# fish.py to harmless and dangerous so that code above still works.
$ cp animals/birds.py animals/harmless/birds.py
$ cp animals/fish.py animals/dangerous/fish.py
"""
print('\n')
harmless_birds = animals.harmless.Birds()
harmless_birds.printMembers()

dangerous_fish = animals.dangerous.Fish()
dangerous_fish.printMembers()