def chapter1(player):
    print("\n--- CHAPTER 1: Arrival in Ravenwood ---")
    print("The fog rolls in thick, concealing the narrow streets as you enter the town of Ravenwood.")
    print("The locals seem anxious and avoid speaking for too long.")

    while True:
        print("\nActions:")
        print("1 – Talk to locals")
        print("2 – Investigate surroundings")
        print("3 – Stay at the inn")
        print("4 – Visit the town square (go to Chapter 2)")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Residents whisper about recent strange disappearances… something lurking in the alleys.")
            player.add_clue("Locals mention disappearances.")
        elif choice == "2":
            print("You inspect the streets and discover a strange symbol etched into a wall.")
            player.add_clue("Found a strange symbol near a shop.")
        elif choice == "3":
            player.rest()
        elif choice == "4":
            print("You walk toward the town square.")
            return "chapter2"
        else:
            print("Invalid choice.")