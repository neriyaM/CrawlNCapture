from src import crawler
from src.sniffer import Sniffer
from src.utils import build_filename
import argparse
import json
from src.consts import ConfigKeys
import sqlite3 as sql


def main():
    parser = create_arg_parser()
    args = parser.parse_args()

    config = load_config(args.config)
    domains = load_domains(config[ConfigKeys.DOMAINS_DB])
    #domains = load_top_domains()
    with open('domains.txt', 'w') as f:
        for domain in domains:
            f.write(domain + '\n')
    exit()
    for i in range(1):
        for domain in domains:
            print("Start {}".format(domain))
            filename = build_filename(domain)
            sniffer = Sniffer(filename, config[ConfigKeys.SNIFF_FILTER])
            sniffer.start()
            crawler.crawl(domain, config[ConfigKeys.CRAWL_TIME])
            sniffer.stop()
            print("Stop {}".format(domain))


def create_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', help="The path of the config file")
    return parser


def load_config(path: str):
    with open(path, 'r') as f:
        return json.load(f)


def load_domains(path):
    conn = sql.connect(path)
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT(domain) from DOMAINS")
    domains = cursor.fetchall()
    return [domain[0] for domain in domains]


def load_top_domains():
    with open('top-1m.csv', 'r') as f:
        content = f.read()

    domains = [x.split(',')[-1] for x in content.splitlines()]
    return domains[:1000]


if __name__ == "__main__":
    main()
