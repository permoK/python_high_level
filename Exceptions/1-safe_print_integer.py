def safe_print_integer(value):
    try:
        value = int(value)
        print(f"{value:d}")
    except ValueError:
        print(f"{value} is not an integer")
safe_print_integer(value="dd")