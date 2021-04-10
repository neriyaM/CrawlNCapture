from src import crawler
from src.sniffer import Sniffer
from src.utils import build_filename
import argparse
import json
from src.consts import ConfigKeys
from src.cookies import from_config


def main():
    parser = create_arg_parser()
    args = parser.parse_args()

    config = load_config(args.config)
    cookies_config = config[ConfigKeys.COOKIES]
    cookies = from_config(cookies_config)
    tls_config = config[ConfigKeys.TLS_VERSIONS][args.tls_version]
    for url in config[ConfigKeys.URLS]:
        print("Start {}".format(url))
        filename = build_filename(url)
        sniffer = Sniffer(filename, config[ConfigKeys.SNIFF_FILTER])
        sniffer.start()
        crawler.crawl(url, config[ConfigKeys.CRAWL_TIME], tls_config[ConfigKeys.CHROME_PATH],
                      tls_config[ConfigKeys.DRIVER_PATH], cookies)
        sniffer.stop()
        print("Stop {}".format(url))


def create_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', help="The path of the config file")
    parser.add_argument('--tls_version', help="Version of TLS")
    return parser


def load_config(path: str):
    with open(path, 'r') as f:
        return json.load(f)


if __name__ == "__main__":
    main()
