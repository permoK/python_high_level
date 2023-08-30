def safe_print_division(a, b):

    try:
        results = a / b 
    except ZeroDivisionError:
        print(None)
    finally:
        print(f"Results: {results}")

a=12
b=2
safe_print_division(a,b)