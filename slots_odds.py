import random,sys

def all_equal(iterator):
    iterator = iter(iterator)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return all(first == rest for rest in iterator)

if len(sys.argv) >= 2:
    repeats = int(sys.argv[1])
else:
    print("Usage:", "python", sys.argv[0], "<number>")
    sys.exit(0)
wins = 0
losses = 0
for v in range(repeats): 
    if all_equal([random.randint(1,10), random.randint(1,10),random.randint(1,10)]): wins += 1
    else: losses += 1

print("Wins:", wins, "\nLosses:", losses)
print("Percent of wins:", str(round(wins / repeats * 100, 2)) + "%")