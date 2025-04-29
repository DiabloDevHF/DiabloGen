from PIL import Image, ImageEnhance
import numpy as np

class ExtraImagePowers:
    def __init__(self, image):
        self.image = image

    def rotate_image(self, angle):
        """
        Rotates the image by a specified angle.
        """
        if self.image:
            self.image = self.image.rotate(angle, expand=True)
            print(f"Image rotated by {angle} degrees.")
        else:
            print("No image to rotate.")

    def resize_image(self, new_width, new_height):
        """
        Resizes the image to a new width and height.
        """
        if self.image:
            self.image = self.image.resize((new_width, new_height))
            print(f"Image resized to {new_width}x{new_height}.")
        else:
            print("No image to resize.")

    def apply_sepia(self):
        """
        Applies a sepia tone filter to the image.
        """
        if self.image:
            # Convert image to numpy array for manipulation
            width, height = self.image.size
            pixels = np.array(self.image)
            for py in range(height):
                for px in range(width):
                    r, g, b = pixels[py, px]
                    tr = int(0.393 * r + 0.769 * g + 0.189 * b)
                    tg = int(0.349 * r + 0.686 * g + 0.168 * b)
                    tb = int(0.272 * r + 0.534 * g + 0.131 * b)

                    # Apply sepia filter, cap the values at 255
                    pixels[py, px] = (min(tr, 255), min(tg, 255), min(tb, 255))

            # Convert back to an image from the numpy array
            self.image = Image.fromarray(pixels)
            print("Applied sepia filter.")
        else:
            print("No image to apply sepia filter.")

    def save_image(self, output_path):
        """
        Saves the edited image to a file.
        """
        if self.image:
            self.image.save(output_path)
            print(f"Image saved as {output_path}.")
        else:
            print("No image to save.")

    def show_image(self):
        """
        Displays the image using the default image viewer.
        """
        if self.image:
            self.image.show()
        else:
            print("No image to display.")


# Example usage
def extra_image_main(image_path, output_path):
    # Open the image from file
    image = Image.open(image_path)
    powers = ExtraImagePowers(image)

    # Apply extra powers
    powers.rotate_image(45)  # Rotate image by 45 degrees
    powers.resize_image(800, 600)  # Resize image to 800x600
    powers.apply_sepia()  # Apply sepia filter
    powers.save_image(output_path)  # Save the new image

    # Optionally show the image
    powers.show_image()

if __name__ == "__main__":
    image_path = input("Enter the image path: ")
    output_path = input("Enter the output path: ")
    extra_image_main(image_path, output_path)
