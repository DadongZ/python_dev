def do_stuff(num):
    try:
        if num:
            return int(num) + 5
        else:
            return None
    except ValueError as err:
        return err