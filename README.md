# Snake-Game

This project is a Python implementation of the classic Snake game using the Pygame library. The game is designed with modular components to follow the SOLID principles, making the codebase more maintainable and scalable.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [How to Play](#how-to-play)
- [Running the Game in Spyder](#running-the-game-in-spyder)
- [Contributing](#contributing)
- [License](#license)

## Features

- Modular design using classes for different game components (`Snake`, `Bait`, `Display`, `Game`).
- Snake movement and direction control using arrow keys.
- Randomly generated bait that makes the snake grow when eaten.
- Collision detection for self-collision and out-of-bounds detection.
- Score tracking and game over screen.
- Restart and quit options on the game over screen.

## Requirements

To run this game, you will need:

- Python 3.x
- Pygame library

## Installation

1. If you don't have Python 3.x installed, download and install it from the [official Python website](https://www.python.org/downloads/).
2. Install the required Pygame library by running the following command in your terminal or command prompt:

    ```bash
    pip install pygame
    ```

3. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/ZeynepDilanKilic/Snake-Game.git
    ```

4. Navigate to the project directory:

    ```bash
    cd snake-game
    ```

## Usage

To run the game:

1. Open a terminal or command prompt and navigate to the project directory.
2. Start the game by running:

    ```bash
    python main.py
    ```

## How to Play

- Use the arrow keys to control the snake's movement:
  - Up Arrow: Move the snake up.
  - Down Arrow: Move the snake down.
  - Left Arrow: Move the snake left.
  - Right Arrow: Move the snake right.
- The snake grows longer and the score increases as it eats the bait.
- The game ends if the snake goes out of bounds or collides with itself.
- After the game ends:
  - Press the "R" key to restart the game.
  - Press the "ESC" key to exit the game.

## Running the Game in Spyder

If you're using Spyder IDE and encounter messages like "Reloaded modules: snake, bait, display" in red, it's due to Spyder's automatic module reloading feature. Here’s how to run the game smoothly:

1. **Disable Automatic Reloading**:
   - Go to `Tools` > `Preferences` in Spyder.
   - Navigate to the `Python interpreter` section.
   - Disable the "Enable UMR (User Module Reloader)" option.

2. **Restart Spyder**: After changing the settings, restart Spyder to apply the changes.

3. **Run the Game**: Use the F5 key or the `Run > Run` menu option to start the game in Spyder.

4. **Alternatively Run in Terminal**: If issues persist, open a terminal in the project directory and run:

    ```bash
    python main.py
    ```

## Contributing

If you want to contribute to this project, please follow these steps:

1. Fork this repository.
2. Create a new branch: `git checkout -b feature-name`
3. Make your changes and commit them: `git commit -m 'Add new feature'`
4. Push to your branch: `git push origin feature-name`
5. Open a pull request.

## License

This project is licensed under the MIT License. For more details, see the `LICENSE` file.
