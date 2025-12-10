from player import Player
import chapter1
import chapter2
import chapter3
import chapter4
import chapter5

def main():
    print("Welcome to the Ravenwood Mystery Adventure!")
    name = input("Enter your detective's name: ")
    player = Player(name)

    current_chapter = "chapter1"

    while True:
        if current_chapter == "chapter1":
            current_chapter = chapter1.chapter1(player)
        elif current_chapter == "chapter2":
            current_chapter = chapter2.chapter2(player)
        elif current_chapter == "chapter3":
            current_chapter = chapter3.chapter3(player)
        elif current_chapter == "chapter4":
            current_chapter = chapter4.chapter4(player)
        elif current_chapter == "chapter5":
            current_chapter = chapter5.chapter5(player)
        elif current_chapter == "end":
            print("\nThank you for playing!")
            break
        else:
            print("Error: unknown chapter.")
            break

if __name__ == "__main__":
    main()
