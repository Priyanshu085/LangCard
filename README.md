# LangCard

LangCards is a command-line tool for generating flashcards from a list of words and translations.

## Table of Contents
- [Usage](#usage)
- [Command-Line Interface](#command-line-interface)
- [Contributing](#contributing)
- [License](#license)

## Usage

1. Install the required dependencies:

  ```bash
  pip install -r requirements.txt
  ```

2. Run the script with the desired command-line arguments:

  ```bash
  python flashcard_generator.py input_files/words.csv --output_file flashcards.pdf --font_size 12
  ```

  - `input_files/words.csv`: Path to the input file containing words and translations.
  - `flashcards.pdf`: Path to the output PDF file.
  - `12`: Font size for the flashcards.

## Command-Line Interface

The command-line interface supports the following arguments:

- **Input File (`input_file`):** Path to the input file containing words and translations.
- **Output File (`output_file`):** Path to the output PDF file (default: flashcards.pdf).
- **Font Size (`font_size`):** Font size for the flashcards (default: 12).
- **Layout (`layout`):** Layout for the flashcards, either "Classic", "Boxes", or "Subdiv" (default: Classic).
- **Color (`color`):** Color for text in the flashcards, in the HEX format provided as a string (with brackets) (default: #000000).

Example:

```bash
python flashcard_generator.py input_files/test.csv --output_file flashcards.pdf --font_size 12
```

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please follow the guidelines in [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).