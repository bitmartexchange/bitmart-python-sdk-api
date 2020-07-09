class CloudLog:
    logger_level = 'debug'

    """:return true or false"""
    @staticmethod
    def is_debug():
        return CloudLog.logger_level == 'debug'

    """
        :param
            logger_level: 'debug', 'info'
    """
    @staticmethod
    def set_logger_level(logger_level: str):
        CloudLog.logger_level = logger_level


def log(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if CloudLog.is_debug():
            print('response')
            print('\tbody:{}'.format(result[0]))
            print('\tlimit:{}'.format(result[1]))
        return result
    return wrapper
