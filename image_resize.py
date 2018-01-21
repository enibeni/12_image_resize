import argparse
from PIL import Image
import os
import sys


def open_image(path_to_original):
    image = Image.open(path_to_original)
    return image


def calculate_new_image_size(old_width, old_height, new_width, new_height):
    if new_width and not new_height:
        new_height = int(new_width * old_height / old_width)
        return new_width, new_height
    elif not new_width and new_height:
        new_width = int(new_height * old_width / old_height)
        return new_width, new_height
    else:
        check_proportions(new_height, new_width, old_height, old_width)
        return new_width, new_height


def check_proportions(old_width, old_height, new_width, new_height):
    if old_width / old_height != new_width / new_height:
        print("Proportion won't be saved!")


def resize_image(image, new_image_size):
    output_image = image.resize(
        new_image_size,
        Image.ANTIALIAS
    )
    return output_image


def scale_image(image, scale):
    output_image = image.resize(
        tuple([int(scale * x) for x in image.size]),
        Image.ANTIALIAS
    )
    return output_image


def get_path_to_result(path_to_original, image_size):
    file_name, _ = os.path.splitext(path_to_original)
    width, height = image_size
    path_to_result = "{}__{}x{}.png".format(
        file_name,
        width,
        height
    )
    return path_to_result


def save_image(path_to_result, image):
    image.save(path_to_result)


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
        help="Path to save image"
    )
    parser.add_argument(
        "-w",
        "--width",
        type=int,
        help="result image width"
    )
    parser.add_argument(
        "-t",
        "--height",
        type=int,
        help="result image height"
    )
    parser.add_argument(
        "-s",
        "--scale",
        type=float,
        help=""

    )
    return parser


if __name__ == "__main__":
    parser = get_input_argument_parser()
    args = parser.parse_args()
    path_to_original = args.file
    path_to_result = args.output
    new_width = args.width
    new_height = args.height
    scale = args.scale

    if scale and (new_width or new_height):
        sys.exit("Wrong parameters. "
                 "Can't be scale and width/height the same time!")

    image = open_image(path_to_original)
    old_width, old_height = image.size

    if new_width or new_height:
        new_image_size = calculate_new_image_size(
            old_width,
            old_height,
            new_width,
            new_height
        )
        output_image = resize_image(image, new_image_size)
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
            output_image.size
        )
    save_image(path_to_result, output_image)
