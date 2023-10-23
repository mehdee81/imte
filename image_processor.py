import os
from PIL import Image
from torchvision import transforms
import torch
class ImageProcessor:

    def __init__(self):
        self.transform = transforms.Compose([
        transforms.ToTensor()
        ])
        self.torch = torch

    def to_tensor(self, address , name):
        try:
            torch.set_printoptions(profile="full")

            image = Image.open(address)
            image = image.convert("RGB")
            tensor = self.transform(image)
            torch.save(tensor, name.split(".")[0]+'.pt')
            print(name.split(".")[0]+'.pt created.')

        except FileNotFoundError:
            print("File does not exist.")
            
        except PermissionError:
            print("You do not have the necessary access to read this file.")

    def to_image(self, tensor , name):
        try:
            transform = transforms.ToPILImage()
            tensor = torch.load(tensor)
            image = transform(tensor)
            image.save(name.split(".")[0]+".png")

            print(name.split(".")[0]+".png created.")

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
