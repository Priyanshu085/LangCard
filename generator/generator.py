from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def parse_input_file(file_path):
  """
  Parse the input file containing words and translations.

  Args:
      file_path (str): Path to the input file.

  Returns:
      list: List of dictionaries containing words and translations.
  """
  words_list = []
  with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
      # Assuming a CSV format where each line has word,translation
      word, translation = line.strip().split(",")
      words_list.append({"word": word, "translation": translation})
  return words_list

def generate_flashcards(words_list, font_size):
  """
  Generate flashcards from the list of words and translations.

  Args:
      words_list (list): List of dictionaries containing words and translations.
      font_size (int): Font size for the flashcards.

  Returns:
      list: List of strings representing flashcards.
  """
  flashcards = []
  for word_info in words_list:
    flashcard = f"Word: {word_info['word']}\nTranslation: {word_info['translation']}"
    flashcards.append(flashcard)
  return flashcards

def generate_pdf(output_file, flashcards):
  """
  Generate a PDF file containing flashcards.

  Args:
      output_file (str): Path to the output PDF file.
      flashcards (list): List of strings representing flashcards.
  """
  pdf_canvas = canvas.Canvas(output_file, pagesize=letter)

  # Set font size for the flashcards
  pdf_canvas.setFont("Helvetica", 12)

  # Write flashcards to the PDF
  for i, flashcard in enumerate(flashcards, start=1):
      pdf_canvas.drawString(50, 750 - i * 50, flashcard)

  pdf_canvas.save()
