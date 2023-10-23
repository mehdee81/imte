import os
from PIL import Image
from torchvision import transforms

class ImageProcessor:

    def __init__(self):
        self.transform = transforms.Compose([
        transforms.ToTensor()
        ])

    def tovector(self, address):
        try:
            image = Image.open(address)
            image = image.convert("RGB")
            vector = self.transform(image)
            print(vector)
            return vector

        except FileNotFoundError:
            print("File does not exist.")
            
        except PermissionError:
            print("You do not have the necessary access to read this file.")

    def toimage(self, vector):
        try:
            transform = transforms.ToPILImage()
            image = transform(vector)
            image.save("new_image.jpg")
            print("New image created.")

        except FileNotFoundError:
            print("File does not exist.")

        except PermissionError:
            print("You do not have the necessary access to write this file.")

    def delete_file(self, file_path):
        try:
            os.remove(file_path)
            print("File removed successfully.")

        except FileNotFoundError:
            print("File does not exist.")

        except PermissionError:
            print("You do not have the necessary access to delete this file.")
