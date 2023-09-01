def safe_print_integer_err(value):
    try:
        value = int(value)
        print(value)
    except ValueError:
        print(f"{value} is not an integer")



safe_print_integer_err(value="school")