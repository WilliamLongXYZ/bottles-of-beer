'''
Bottles of Beer on the Wall
Inspired by The Big Book of Small Python Projects
Reformatted and changed by William Long <williamlong0726@gmail.com>
'''
import time


def print_verse(verse, st=2):
    if "0" in verse: verse = "No more bottles of beer on the wall"
    print(verse)
    time.sleep(st)

def show_stanza(bottles, word, it):
    print_verse(f"{bottles} {word} of beer on the wall")
    print_verse(f"{bottles} {word} of beer")
    print_verse(f"Take {it} down, pass it around")
    print_verse(f"{bottles-1} {word} of beer on the wall", 3)
    print()
    return bottles-1

def main():
    bottles = 99
    word = "bottles"
    it = "one"
    while bottles:
        if bottles == 1:
            word = "bottle"
            it = "it"
        bottles = show_stanza(bottles, word, it)

if __name__ == "__main__":
    main()

