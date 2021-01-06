import os
import datetime

OUTPUT_DIR = "captures"
URL_SEPARATOR = '//'
TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S"
PCAP_FILE_FORMAT = "{}.pcap"


def build_filename(url):
    extracted_domain = url.split(URL_SEPARATOR)[1]
    base_dir = os.path.join(OUTPUT_DIR, extracted_domain)
    timestamp = datetime.datetime.now().strftime(TIMESTAMP_FORMAT).replace(":", "_")
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    filename = os.path.join(base_dir, PCAP_FILE_FORMAT.format(timestamp))
    return filename
