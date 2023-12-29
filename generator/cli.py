# flashcard_generator/cli.py
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description="Language Flashcards Generator")

    # Add arguments
    parser.add_argument(
        "input_file",
        help="Path to the input file containing words and translations (e.g., words.csv)",
    )
    parser.add_argument(
        "--output_file",
        help="Path to the output PDF file (default: flashcards.pdf)",
        default="flashcards.pdf",
    )
    parser.add_argument(
        "--font_size",
        type=int,
        help="Font size for the flashcards (default: 12)",
        default=12,
    )
    # Add more customization options as needed

    return parser.parse_args()
