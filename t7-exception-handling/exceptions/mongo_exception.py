class MongoException(Exception):

    def __init__(self, custom_message, inner_exception):
        self._custom_message = custom_message
        self._inner_exception = inner_exception

    def __str__(self):
        result = self._custom_message + "\n" + \
        str(self._inner_exception)
        return result