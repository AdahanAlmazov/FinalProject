def chapter5(player):
    print("\n--- CHAPTER 5: The Final Showdown ---")
    print("At dawn, you confront the suspect in the town hall.")

    print("\nActions:")
    print("1 – Present current evidence")
    print("2 – Question the suspect")
    print("3 – Explore town freely")

    choice = input("Enter choice: ")

    if choice == "1":
        print("\nYou present your evidence:")
        for c in player.clues:
            print(" -", c)
        print("\nThe suspect is caught. Case closed.")
        return "end"

    elif choice == "2":
        print("The suspect breaks down and confesses after intense questioning.")
        return "end"

    elif choice == "3":
        print("You roam the town gathering any final clues.")
        return "chapter1"

    else:
        print("Invalid choice.")
        return "chapter5"
