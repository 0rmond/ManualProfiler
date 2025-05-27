def ask_for_step_size():
    """Asks the user what the translation will be incremented by, in um.
    """

    step_size = None
    while step_size is None:

        answer_for_step_size = input("Please enter your measurement step size (in um). ")
        try:
            step_size = int(answer_for_step_size)
        except ValueError:
            print("Not a valid number, please try again...")

    return step_size

def ask_for_start():
    """Asks the user what value it should start from. Probably zero, but helpful if a measurement was interrupted for whatever reason.
    """
    start = None
    while start is None:
        this_is_a_new_measurement = input("Are you beginning a new measurement (y/n)? ")

        if this_is_a_new_measurement.upper() == 'Y' or this_is_a_new_measurement == '':
            start = 0
        elif this_is_a_new_measurement.upper() == 'N':
            checking_last_position = True
            while checking_last_position:
                answer_for_start = input("What, in um, was the last position of your interrupted measurement? Check the bottom of your results file.")
                try:
                    start = int(answer_for_start)
                    checking_last_position = False
                except ValueError:
                    print("Not a valid number, please try again...")
        else: print("I'm sorry, I do not understand. Please enter 'y' or 'n'.")
    return start
