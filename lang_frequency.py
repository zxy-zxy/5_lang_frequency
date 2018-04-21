import sys
import re
import argparse
from collections import Counter


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-filepath",
        type=str,
        required=True,
        help="Please, provide a filepath"
    )
    return parser


def load_text_to_process(filepath):
    with open(filepath) as file:
        text_to_process = file.read()
        return text_to_process


def split_text_into_words(text_to_split):
    return re.findall("\w+", text_to_split.lower())


def get_most_frequent_words(words_list):
    counter = Counter(words_list)
    top_words_count = 10
    return counter.most_common(top_words_count)


if __name__ == "__main__":
    args_parser = create_parser()
    args = args_parser.parse_args()

    try:
        text_to_process = load_text_to_process(args.filepath)
    except FileNotFoundError:
        sys.exit("Error has occured while reading file")

    words_list = split_text_into_words(text_to_process)
    most_frequent_words = get_most_frequent_words(words_list)

    for order, (word, frequency) in enumerate(most_frequent_words):
        print("Order: {}, frequency: {}, word: {}".format(
            order,
            frequency,
            word)
        )
