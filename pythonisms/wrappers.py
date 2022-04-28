from functools import wraps
import time

def timing(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
          
        return f'{func.__name__} took {end-start} to execute. The result is {result}.'
        
    return wrapper

def intro_outro(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        orig_val = func(*args, **kwargs)
        return f'Drum roll please... {orig_val}... Tada!'
    return wrapper

@intro_outro
def say(txt):
    return txt

@timing
def addition(num1, num2):
    return num1 + num2