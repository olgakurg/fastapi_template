from core.logger import logger


def log_info(func):
    async def wrapper(*args, **kwargs):
        logger.info(f"Call def {func.__name__} with args: {args} kwargs: {kwargs}")
        result = await func(*args, **kwargs)
        logger.info(f"def {func.__name__} return result {result}")
        return result

    return wrapper
