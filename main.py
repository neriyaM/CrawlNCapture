from src import crawler
from src.sniffer import Sniffer
from src.utils import build_filename
import argparse
import json
from src.consts import ConfigKeys


def main():
    parser = create_arg_parser()
    args = parser.parse_args()

    config = load_config(args.config)
    for url in config[ConfigKeys.URLS]:
        print("Start {}".format(url))
        filename = build_filename(url)
        sniffer = Sniffer(filename, config[ConfigKeys.SNIFF_FILTER])
        sniffer.start()
        crawler.crawl(url, config[ConfigKeys.CRAWL_TIME])
        sniffer.stop()
        print("Stop {}".format(url))


def create_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', help="The path of the config file")
    return parser


def load_config(path: str):
    with open(path, 'r') as f:
        return json.load(f)


if __name__ == "__main__":
    main()
