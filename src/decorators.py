from functools import wraps


def log(filename=None):
    def wrapper(function):
        @wraps(function)
        def inner(*args, **kwargs):
            try:
                result = function(*args, **kwargs)
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(
                            f"{function.__name__} ok. {function(*args, **kwargs)}"
                        )
                else:
                    print(
                        f"{function.__name__} ok. Inputs: {function(*args, **kwargs)}"
                    )
                return result
            except Exception as e:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(
                            f"{function.__name__} error: {e}. Inputs: {args}, {kwargs}"
                        )
                else:
                    print(f"{function.__name__} error: {e}. Inputs: {args}, {kwargs}")
                raise e

        return inner

    return wrapper


@log(filename="mylog.txt")
def my_function(x, y):
    return x / y


my_function(1, 5)
