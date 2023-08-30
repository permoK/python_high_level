def safe_print_integer(value):
    try:
        value = int(value)
        print(value)
    except ValueError:
        print(False)
safe_print_integer(value=8)