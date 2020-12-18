from scapy.all import AsyncSniffer, wrpcap


class Sniffer:
    def __init__(self, filename, sniff_filter=""):
        self.sniffer = AsyncSniffer(filter=sniff_filter)
        self.filename = filename

    def start(self):
        self.sniffer.start()

    def stop(self):
        results = self.sniffer.stop()
        wrpcap(self.filename, results)

