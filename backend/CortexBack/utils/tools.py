
    


def api_action(name, method):
    def wrapper(func):
        func.api_action = {
            'name': name,
            'method': method
        }
        return func
    return wrapper