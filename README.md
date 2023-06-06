# Prime Playground
A web application that allows users to generate a grid of numbers with various highlighting patterns. The project is built using HTML, CSS, and JavaScript, with Flask serving as the web framework.

## Features

- Generate a grid of numbers up to a user-specified limit
- Highlight "left-hand side" primes in the 4th column
- Highlight "right-hand side" primes in the 6th column
- Highlight multiples of 5
- Highlight multiples of 7
- Highlight multiles of user-specified input
- ... more to come

## Local Setup

Follow these instructions to run this project locally.

### Prerequisites

- Python 3
- Flask

### Installation

1. Clone this repository

`git clone https://github.com/dennissmith0/Primus.git`

2. Navigate into the directory of the project

`$ cd Primus`

3. Install the required packages

`$ pip install -r requirements.txt`

4. Run the Flask application

`$ flask run`

After running these commands, you should be able to see the application by opening a browser and visiting `http://127.0.0.1:5000/`.

## Usage

Enter a number in the input field and press the "Create Number Field" button or press Enter to generate a grid of numbers up to that limit. Use the buttons above the grid to toggle various highlighting patterns.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
