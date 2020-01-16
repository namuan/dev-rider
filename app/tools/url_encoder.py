import logging


class UrlEncoder:
    name: str = "URL Encoder"

    def open(self):
        logging.info("Loading {}".format(self.name))


tool = UrlEncoder()
