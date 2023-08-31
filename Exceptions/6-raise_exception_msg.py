def raise_exception_msg(message="Rust is hella fun 🙅‍♂️ "):
    try:
        print(message)
    except NameError as ne:
        print(ne)


raise_exception_msg()