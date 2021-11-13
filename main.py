'''
Bottles of Beer on the Wall
Inspired by The Big Book of Small Python Projects
Reformatted and changed by William Long <williamlong0726@gmail.com
'''

def main():
    bottles = 99
    while bottles:
        print(f"{bottles} bottles of beer on the wall")
        print(f"{bottles} bottles of beer")
        print(f"Take one down, pass it around")
        print(f"{bottles-1} bottles of beer on the wall")
        bottles -= 1

if __name__ == "__main__":
    main()
