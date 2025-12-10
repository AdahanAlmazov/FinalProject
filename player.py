class Player:
    def __init__(self, name):
        self.name = name
        self.energy = 100
        self.clues = []
        self.inventory = []

    def add_clue(self, clue):
        self.clues.append(clue)
        print(f"Clue added: {clue}")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"Item added to inventory: {item}")

    def reduce_energy(self, amount):
        self.energy -= amount
        print(f"Energy reduced by {amount}. Current energy: {self.energy}")

    def rest(self):
        self.energy = 100
        print("You rested at the inn. Energy restored to 100.")