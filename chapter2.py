def chapter2(player):
    print("\n--- CHAPTER 2: The Wailing Alley ---")
    print("A strange wailing echoes from the alley as night falls.")

    while True:
        print("\nActions:")
        print("1 – Examine the alley")
        print("2 – Follow footprints (Chapter 3)")
        print("3 – Ask a nearby resident (return to Chapter 1)")

        choice = input("Enter choice: ")

        if choice == "1":
            print("You find a torn piece of cloth caught on a nail.")
            player.add_clue("Torn cloth from alley.")
        elif choice == "2":
            print("You follow the tracks leading away from the alley…")
            return "chapter3"
        elif choice == "3":
            print("A resident gives vague information and retreats into their home.")
            return "chapter1"
        else:
            print("Invalid choice.")
