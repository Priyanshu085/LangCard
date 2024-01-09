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
  parser.add_argument(
      "--color",
      help="Color for the flashcards in hex format (default: #000000)",
      default="#000000",
  )
  parser.add_argument(
      "--layout",
      choices=["Classic", "Boxes", "Subdiv"],
      help="Layout for the flashcards (default: Classic)",
      default="Classic",
  )

  return parser.parse_args()
