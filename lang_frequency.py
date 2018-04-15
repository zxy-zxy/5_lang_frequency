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


def load_data(filepath):
    with open(filepath) as file:
        data = file.read()
        return data


def split_text_into_words(multi_line_text):
    words_list = map(
        str.lower,
        re.findall(
            "\w+",
            multi_line_text
        )
    )
    return words_list


def get_most_frequent_words(words_list):
    counter = Counter(words_list)
    top_n_words = 10
    return counter.most_common(top_n_words)


if __name__ == '__main__':
    args_parser = create_parser()
    args = args_parser.parse_args()

    try:
        multi_line_text = load_data(args.filepath)
    except FileNotFoundError:
        sys.exit("Error has occured while reading file")

    words_list = split_text_into_words(multi_line_text)
    most_frequent_words = get_most_frequent_words(words_list)

    for order, (word, frequency) in enumerate(most_frequent_words):
        print("Order: {}, frequency: {}, word: {}".format(
            order,
            frequency,
            word)
        )
