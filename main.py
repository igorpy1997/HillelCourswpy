#first task
import time
class UnexpectedTypeException(Exception):
    pass


def expected_type(return_types):
    def dec_func(wrap_function):
        def wrapper(*args, **kwargs):
            result = wrap_function(*args, **kwargs)
            if not isinstance(result, return_types):
                raise UnexpectedTypeException(f"Was expecting instance of: {return_types}")
            """
            f строки 
            raise 
            """
            return result
        return wrapper
    return dec_func


#Second task
def timer(time_of_working):
    def dec_func(wrap_function):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            wrap_function(*args, **kwargs)
            run_time = time.time() - start_time
            return run_time < time_of_working
        return wrapper
    return dec_func




#@expected_type(int)
@timer(2)
def add_numbers(a,b):
    time.sleep(1)
    return a+b

print(add_numbers(0.22, 0.33))

