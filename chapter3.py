def chapter3(player):
    print("\n--- CHAPTER 3: The Abandoned Warehouse ---")
    print("The footprints lead you to a dim, abandoned warehouse with broken windows.")

    while True:
        print("\nActions:")
        print("1 – Move carefully inside (find clues)")
        print("2 – Walk around perimeter (find secret back door)")
        print("3 – Return to town (Chapter 2)")

        choice = input("Enter choice: ")

        if choice == "1":
            print("You spot a loose board. Behind it lies a strange metallic key.")
            player.add_item("Rusty Key")
        elif choice == "2":
            print("You find a hidden back door slightly ajar…")
            return "chapter4"
        elif choice == "3":
            return "chapter2"
        else:
            print("Invalid choice.")
