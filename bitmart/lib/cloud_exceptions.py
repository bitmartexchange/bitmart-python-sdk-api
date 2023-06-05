
class APIException(Exception):

    def __init__(self, response):
        self.status_code = response.status_code
        self.response = response.text

    def __str__(self):
        return 'APIException(http status=%s): response=%s' % (self.status_code, self.response)


class RequestException(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return 'RequestException: %s' % self.message


class ParamsException(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return 'ParamsException: %s' % self.message
