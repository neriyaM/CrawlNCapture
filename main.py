from lib import crawler
from lib.sniffer import Sniffer
from lib.utils import build_filename

urls = ["https://ynet.co.il", "https://walla.co.il"]
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


if __name__ == "__main__":
    main()
