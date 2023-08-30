def safe_print_division(a, b):

    try:
        results = a / b 
    except ZeroDivisionError:
        results = None
    finally:
        return f"Results: {results}"

a=12
b=0
print(safe_print_division(a,b))