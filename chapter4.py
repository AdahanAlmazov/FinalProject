def chapter4(player):
    print("\n--- CHAPTER 4: The Secret Room ---")
    print("Inside the warehouse, candlelight flickers across crates and barrels.")
    print("Behind a false wall, you discover a secret room.")

    while True:
        print("\nActions:")
        print("1 – Search the room")
        print("2 – Open the safe")
        print("3 – Leave the warehouse (go to Chapter 5)")

        choice = input("Enter choice: ")

        if choice == "1":
            print("You find documents linking a town official to the disappearances.")
            player.add_clue("Incriminating documents found.")
        elif choice == "2":
            if "Rusty Key" in player.inventory:
                print("The key fits. You retrieve a final piece of evidence.")
                player.add_clue("Safe evidence: motive and plan.")
            else:
                print("The safe is locked. You need a key.")
        elif choice == "3":
            return "chapter5"
        else:
            print("Invalid choice.")
