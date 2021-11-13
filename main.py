'''
Bottles of Beer on the Wall
Inspired by The Big Book of Small Python Projects
Reformatted and changed by William Long <williamlong0726@gmail.com
'''
import time


def print_verse(verse, st=2):
    print(verse)
    time.sleep(st)

def main():
    bottles = 99
    while bottles:
        word = "bottle"
        it = "it"
        if bottles != 1:
            word += "s"
            it = "one"
        print_verse(f"{bottles} {word} of beer on the wall")
        print_verse(f"{bottles} {word} of beer")
        print_verse(f"Take {it} down, pass it around")
        bottles -= 1
        print_verse(f"{bottles} {word} of beer on the wall", 3)
        print()

if __name__ == "__main__":
    main()

