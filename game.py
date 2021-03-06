import sys
from random import randint

def all_equal(iterator):
    iterator = iter(iterator)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return all(first == rest for rest in iterator)

def main(argv, argc):
    money = 100
    cost = 25
    win = 75
    jackpot = 200
    print("You get all the same numbers - ${0}\nYou don't get all the same numbers - $0\nYou get 7, 7, and 7 - ${1}\n".format(win,jackpot))
    while True:
        print("You have ${0}. It costs ${1} to roll the slots once.".format(money, cost))
        cmd = input("What would you like to do? Roll the slots (r) or quit (q)? ").lower()
        if cmd in ["q","quit"]:
            sys.exit(0)
        elif cmd in ["r", "roll"]:
            if money >= cost:
                money -= cost
            else:
                print("\nUh oh, looks like you're out of money! Come back when you're a little -mmm- richer!\n")
                sys.exit(0)
            slot_nums = [randint(1,9), randint(1,9), randint(1,9)]
            
            print("")
            print(slot_nums[0], slot_nums[1], slot_nums[2], sep="")
            print("")
            if slot_nums == [7, 7, 7]:
                print("Congrats! You won the jackpot and got ${0}.".format(jackpot))
                money += jackpot
            elif all_equal(slot_nums):
                print("You won! Here's ${0}.".format(win))
                cost += win
        elif "money" in cmd:
            new_cmd = cmd.split(" ", 3)[1:]
            if new_cmd[0] == "add":
                money += int(new_cmd[1])
            elif new_cmd[0] == "remove":
                if int(new_cmd[1]) > money:
                    print("\nYou can't have negative money!\n")
                else:
                    money -= int(new_cmd[1])
            

if __name__ == "__main__":
    main(sys.argv,len(sys.argv))