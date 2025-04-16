# Ranking Tool

**Description**: A command-line tool that reads competition results from an input file and generates a ranking based on the scores. A win grants 3 points, and a tie grants 1 point.

---

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Testing](#testing)
4. [License](#license)

---

## Installation

### Prerequisites

Make sure you have the following installed:

- Python 3.11
- pip (Python package installer) — *currently not needed*

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/FabioSol/coding-challenge.git
    ```
2. Navigate to the project directory:

    ```bash
    cd coding-challenge
    ```
3. Create a virtual environment:
    ```bash
    python3.11 -m venv venv
    ```

4. Activate the virtual enviroment:
    ```bash
    source venv/bin/activate
    ```

5. Since the `requirements.txt` is currently empty, no additional dependencies are required for installation. If you need to add dependencies later, you can include them in `requirements.txt` and install them using:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Prepare an input file with the following format (example: `matches.txt`):
    ```text
    Lions 3, Snakes 3
    Tarantulas 1, FC Awesome 0
    Lions 1, FC Awesome 1
    Tarantulas 3, Snakes 1
    Lions 4, Grouches 0
    ```
   - Each line represents the result of a game.
   - Format: `<Team 1> <Score 1>, <Team 2> <Score 2>`

2. Run the ranking tool with:
    ```bash
    python -m ranking_tool rank path/to/input.txt
    ```
3. The ranking will be printed to the console based on the rules:
    ```text
    1. Tarantulas, 6 pts
    2. Lions, 5 pts
    3. FC Awesome, 1 pt
    3. Snakes, 1 pt
    5. Grouches, 0 pts
    ```
## Testing

This project includes both unit and integration tests.

### Structure

- `tests/test_core.py` — unit tests for the core ranking logic
- `tests/test_utils.py` — unit tests for utility functions
- `tests/test_integration.py` — integration tests using sample input files
- `tests/fixtures/` — sample input/output files for integration testing

### Running Tests
First, activate your virtual environment. Then run:
```bash
  python -m unittest discover tests
```

## License

This project is licensed under the [MIT License](LICENSE).
