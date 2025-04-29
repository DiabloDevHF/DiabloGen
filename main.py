import os
import requests
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from bs4 import BeautifulSoup

class ImageEditor:
    def __init__(self, html_file):
        self.html_file = html_file
        self.image_url = None
        self.image = None
        self.output_path = "edited_image.png"

    def parse_html(self):
        """
        Parses the HTML file and extracts the first image URL/path.
        """
        try:
            with open(self.html_file, 'r') as file:
                soup = BeautifulSoup(file, 'html.parser')
                img_tag = soup.find('img')
                if img_tag and 'src' in img_tag.attrs:
                    self.image_url = img_tag['src']
                    print(f"Image found: {self.image_url}")
                else:
                    print("No image found in the HTML file.")
        except Exception as e:
            print(f"Error reading HTML file: {e}")

    def download_image(self):
        """
        Downloads the image from a URL or opens a local image if path is provided.
        """
        if not self.image_url:
            print("No image URL found. Please parse the HTML first.")
            return

        if self.image_url.startswith('http'):
            # It's a URL, download the image
            try:
                response = requests.get(self.image_url)
                response.raise_for_status()
                self.image = Image.open(response.content)
                print("Image downloaded successfully.")
            except requests.exceptions.RequestException as e:
                print(f"Error downloading image: {e}")
        else:
            # It's a local path
            try:
                self.image = Image.open(self.image_url)
                print("Image opened successfully from local path.")
            except IOError as e:
                print(f"Error opening image: {e}")

    def apply_grayscale(self):
        """
        Converts the image to grayscale.
        """
        if self.image:
            self.image = self.image.convert("L")
            print("Applied grayscale filter.")
        else:
            print("No image loaded to apply grayscale.")

    def apply_blur(self):
        """
        Applies a blur filter to the image.
        """
        if self.image:
            self.image = self.image.filter(ImageFilter.GaussianBlur(radius=5))
            print("Applied blur filter.")
        else:
            print("No image loaded to apply blur.")

    def add_watermark(self, text="Sample Watermark"):
        """
        Adds a watermark to the image.
        """
        if self.image:
            draw = ImageDraw.Draw(self.image)
            try:
                font = ImageFont.load_default()
            except IOError:
                font = None

            text_width, text_height = draw.textsize(text, font=font)
            width, height = self.image.size

            position = (width - text_width - 10, height - text_height - 10)
            draw.text(position, text, (255, 255, 255), font=font)
            print(f"Watermark added: {text}")
        else:
            print("No image loaded to add watermark.")

    def save_image(self, output_path=None):
        """
        Saves the edited image to a file.
        """
        if not self.image:
            print("No image to save.")
            return

        if output_path:
            self.output_path = output_path

        try:
            self.image.save(self.output_path)
            print(f"Image saved as {self.output_path}")
        except Exception as e:
            print(f"Error saving image: {e}")

    def show_image(self):
        """
        Displays the image using the default image viewer.
        """
        if self.image:
            self.image.show()
        else:
            print("No image loaded to display.")

    def process_image(self):
        """
        Runs the entire image processing pipeline.
        """
        self.parse_html()
        self.download_image()
        self.apply_grayscale()
        self.apply_blur()
        self.add_watermark("Edited by Python Script")
        self.save_image("output_edited_image.png")
        self.show_image()


def main():
    html_file = input("Enter the path to the HTML file: ")
    if not os.path.exists(html_file):
        print("Error: HTML file not found.")
        return

    editor = ImageEditor(html_file)
    editor.process_image()

if __name__ == "__main__":
    main()
