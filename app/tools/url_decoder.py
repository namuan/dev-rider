import logging


class UrlDecoder:
    name: str = "URL Decoder"

    def open(self):
        logging.info("Loading {}".format(self.name))


tool = UrlDecoder()
