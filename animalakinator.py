import json

class AnimalGame:
    def __init__(self, data_file="animals.json"):
        # Load animal data from a JSON file
        with open(data_file, "r") as file:
            self.animals = json.load(file)
        self.current_question = None
        self.current_node = self.animals

    def ask_question(self):
        # Ask the current question and update the current node
        print(self.current_question)
        user_response = input("Enter 'yes' or 'no': ").lower()
        if user_response == 'yes' and 'yes' in self.current_node:
            self.current_node = self.current_node['yes']
        elif user_response == 'no' and 'no' in self.current_node:
            self.current_node = self.current_node['no']
        else:
            print("Invalid response. Please enter 'yes' or 'no'.")

    def play_game(self):
        # Main game loop
        print("Welcome to the Animal Guessing Game!")
        while 'question' in self.current_node:
            self.current_question = self.current_node['question']
            self.ask_question()

        # Display the guessed animal
        if 'animal' in self.current_node:
            print(f"I guess your animal is a {self.current_node['animal']}!")
            self.play_again()

    def play_again(self):
        response = input("Do you want to play again? (yes/no): ").lower()
        if response == 'yes':
            self.__init__()  # Reset the game state
            self.play_game()
        else:
            print("Thanks for playing!")

if __name__ == "__main__":
    # Example data in animals.json file
    # Can expand and modify this as needed
    example_data = {
        "question": "Does it have fur?",
        "yes": {
            "question": "Is it a carnivore?",
            "yes": {
                "question": "Does it live in the jungle?",
                "yes": {"animal": "Lion"},
                "no": {"animal": "Wolf"}
            },
            "no": {
                "question": "Is it a herbivore?",
                "yes": {"animal": "Elephant"},
                "no": {"animal": "Giraffe"}
            }
        },
        "no": {
            "question": "Can it fly?",
            "yes": {
                "question": "Is it colorful?",
                "yes": {"animal": "Parrot"},
                "no": {"animal": "Penguin"}
            },
            "no": {
                "question": "Is it a reptile?",
                "yes": {"animal": "Snake"},
                "no": {"animal": "Horse"}
            }
        }
    }

    # Save the example data to a JSON file
    with open("animals.json", "w") as file:
        json.dump(example_data, file, indent=2)

    # Create an instance of the AnimalGame and play the game
    game = AnimalGame()
    game.play_game()
