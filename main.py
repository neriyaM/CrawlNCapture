from lib import crawler
import os
from lib.sniffer import Sniffer
import datetime

urls = ["https://ynet.co.il"]
OUTPUT_DIR = "captures"
crawl_time = 10


def main():
    for url in urls:
        print("Start {}".format(url))
        filename = build_filename(url)
        sniffer = Sniffer(filename, "tcp")
        sniffer.start()
        crawler.crawl(url, crawl_time)
        sniffer.stop()
        print("Stop {}".format(url))


def build_filename(url):
    extracted_domain = url.split('//')[1]
    base_dir = os.path.join(OUTPUT_DIR, extracted_domain)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S").replace(":", "_")
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    filename = os.path.join(base_dir, "{}.pcap".format(timestamp))
    return filename


if __name__ == "__main__":
    main()
