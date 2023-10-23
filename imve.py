import argparse
from image_processor import ImageProcessor



parser = argparse.ArgumentParser()
parser.add_argument("-tovector", help="Convert image to vector.")
parser.add_argument("-toimage", help="Convert vector to image.")
parser.add_argument("-rm", help="Remove file.")
args = parser.parse_args()

processor = ImageProcessor()

if args.rm:
    processor.delete_file(args.rm)

if args.tovector:
    processor.tovector(args.tovector)

if args.toimage:
    processor.toimage(args.toimage)