# flashcard_generator.py
from generator import cli, generator

def main():
    # Parse command-line arguments
    args = cli.parse_arguments()

    # Parse input file
    words_list = generator.parse_input_file(args.input_file)

    # Generate flashcards
    flashcards = generator.generate_flashcards(words_list, args.font_size)

    # Generate PDF
    generator.generate_pdf(args.output_file, flashcards)

    print(f"Flashcards generated successfully. PDF saved to: {args.output_file}")

if __name__ == "__main__":
    main()
