import argparse
from image_processor import ImageProcessor



parser = argparse.ArgumentParser()
parser.add_argument("-totensor", help="Convert image to tensor.")
parser.add_argument("-name", help="Name of new tensor.")
parser.add_argument("-toimage", help="Convert tensor to image.")
parser.add_argument("-rm", help="Remove file.")
args = parser.parse_args()

processor = ImageProcessor()

if args.rm:
    processor.delete_file(args.rm)

if args.totensor and args.name:
    processor.to_tensor(args.totensor , args.name)

if args.toimage and args.name:
    processor.to_image(args.toimage , args.name)