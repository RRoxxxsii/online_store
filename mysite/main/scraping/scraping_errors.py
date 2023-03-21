class ScrapingError(Exception):
    pass


class ScrapingTimeoutError(ScrapingError):
    pass


class ScrapingHTTPError(ScrapingError):
    pass


class ScrapingOtherError(ScrapingError):
    pass
