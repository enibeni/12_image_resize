import argparse
from PIL import Image
import os
import sys


def open_image(path_to_original):
    image = Image.open(path_to_original)
    return image


def resize_image(image, new_width, new_height):
    old_width, old_height = image.size[0], image.size[1]
    if new_width and new_height:
        new_width = int(new_width)
        new_height = int(new_height)
        if old_width/old_height != new_width/new_height:
            print_message("Proportion won't be saved!")
        output_image = image.resize(
            (new_width, new_height),
            Image.ANTIALIAS
        )
        return output_image
    elif new_width and not new_height:
        new_width = int(new_width)
        new_height = int(new_width * old_height / old_width)
        output_image = image.resize(
            (new_width, new_height),
            Image.ANTIALIAS
        )
        return output_image
    elif not new_width and new_height:
        new_height = int(new_height)
        new_width = int(new_height * old_width / old_height)
        output_image = image.resize(
            (new_width, new_height),
            Image.ANTIALIAS
        )
        return output_image
    else:
        output_image = image
        return output_image


def print_message(message):
    print(message)


def scale_image(image, scale):
    output_image = image.resize(
        tuple([int(float(scale) * x) for x in image.size]),
        Image.ANTIALIAS
    )
    return output_image


def get_path_to_result(path_to_original, image):
    file_name = os.path.splitext(path_to_original)[0]
    path_to_result = "{}__{}x{}.png".format(
        file_name,
        image.size[0],
        image.size[1]
    )
    return path_to_result


def save_image(path_to_result, image):
    image.save(path_to_result, "PNG")


def get_input_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--file",
        required=True,
        help="Path to image to resize"
    )
    parser.add_argument(
        "-o",
        "--output",
        required=False,
        help="Path to save image"
    )
    parser.add_argument(
        "-w",
        "--width",
        required=False,
        help="result image width"
    )
    parser.add_argument(
        "-t",
        "--height",
        required=False,
        help="result image height"
    )
    parser.add_argument(
        "-s",
        "--scale",
        required=False,
        help=""

    )
    return parser


if __name__ == "__main__":
    parser = get_input_argument_parser()
    args = parser.parse_args()
    path_to_original = args.file
    path_to_result = args.output
    width = args.width
    height = args.height
    scale = args.scale

    if scale and (height or width):
        sys.exit("Wrong parameters. "
                 "Can't be scale and width/height the same time!")

    image = open_image(path_to_original)

    if height or width:
        output_image = resize_image(image, width, height)
    elif scale:
        output_image = scale_image(image, scale)
    else:
        sys.exit(
            "You need enter a parameter. "
            "Scale (-s) or height (-t) or/and width (-w)"
        )
    if path_to_result is None:
        path_to_result = get_path_to_result(
            path_to_original,
            output_image
        )
    save_image(path_to_result, output_image)
