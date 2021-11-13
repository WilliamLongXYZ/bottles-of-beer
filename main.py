'''
Bottles of Beer on the Wall
Inspired by The Big Book of Small Python Projects
Reformatted and changed by William Long <williamlong0726@gmail.com
'''
import time

def main():
    bottles = 99
    while bottles:
        word = "bottle"
        it = "it"
        if bottles != 1:
            word += "s"
            it = "one"
        print(f"{bottles} {word} of beer on the wall")
        time.sleep(2)
        print(f"{bottles} {word} of beer")
        time.sleep(2)
        print(f"Take {it} down, pass it around")
        bottles -= 1
        time.sleep(2)
        print(f"{bottles} {word} of beer on the wall")
        time.sleep(3)
        print()

if __name__ == "__main__":
    main()

