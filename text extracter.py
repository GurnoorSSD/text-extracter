from PIL import Image
import pytesseract

def extract_text_from_image(image_path):
    try:
        # Open the image
        img = Image.open(image_path)

        # Extract text using pytesseract
        text = pytesseract.image_to_string(img)

        print("\n📝 Extracted Text:\n")
        print(text.strip())

    except FileNotFoundError:
        print("❌ Image file not found.")
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    image_file = input("Enter the path to the image file: ")
    extract_text_from_image(image_file)
