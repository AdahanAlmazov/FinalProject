Ravenwood Mystery Adventure Game
A modular, text-based mystery/thriller adventure game built in Python.
The player takes on the role of a young detective investigating strange disappearances in the fog-covered town of Ravenwood.
The game features multi-chapter progression, inventory and clue tracking, and a dedicated player class object.
Table of Contents
Features
Chapter Structure
Technologies Used
Project Structure
Installation
How to Run
Game Flow
Player Class Overview
Contributing
License
Features
Multi-chapter story progression (5 modular chapters)
Player class system handles:
energy tracking
inventory
collected clues
Branching narrative paths and replayability
Fully modular architecture with each chapter as a separate Python module
Easy to extend with new chapters or alternate endings
Chapter Structure
Each chapter exists in its own Python file and contains:
Story narration
Action choices
Branching logic
Calls to player class methods
Return values that indicate the next chapter
Chapters Included
Arrival in Ravenwood
The Wailing Alley
The Abandoned Warehouse
The Secret Room
The Final Showdown
Technologies Used
Python 3.x
No external libraries required
Standard I/O text interface
Modular Python imports
GitHub for version control and collaboration
Project Structure
adventure_game/
│
├── main.py
├── player.py
│
├── chapter1.py
├── chapter2.py
├── chapter3.py
├── chapter4.py
├── chapter5.py
│
└── README.md
Installation
Prerequisites
Python 3.8+
Terminal or IDE (VS Code, PyCharm, IDLE, etc.)
Clone the Repository
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
How to Run
Run the main entry point:
python main.py
If using macOS or Linux:
python3 main.py
Follow the on-screen choices to progress through the chapters.
Game Flow
The game flow is controlled by main.py, which:
Creates a Player object
Starts the game loop
Calls the appropriate chapter function
Moves to the next chapter based on return values
Ends the game when Chapter 5 returns "end"
Player Class Overview
The Player class is located in player.py.
Responsibilities:
Track player name
Manage energy levels
Store found clues
Store inventory items
Provide methods such as:
add_clue()
add_item()
reduce_energy()
rest()
Example:
player = Player("Detective")
player.add_clue("Torn cloth from alley")
player.add_item("Rusty Key")
The Player object is passed into every chapter, maintaining persistent state.
Contributing
If you would like to contribute:
Fork the repository
Create a new branch
Submit a pull request describing your changes
Recommended improvements:
UI enhancements
Save/load system
More branching paths
Additional characters or encounters
Combat or puzzle subsystems
License
This project is created for academic use.
You may modify or extend the game for personal or educational purposes.
