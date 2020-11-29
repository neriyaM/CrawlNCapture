from lib import crawler


def main():
    crawler.crawl("https://ynet.co.il", 10)
    crawler.crawl("https://walla.co.il", 10)


if __name__ == "__main__":
    main()
