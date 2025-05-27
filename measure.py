from PM import PM101

def init_pm_with(user_wavelength):
    """Initialises a ThorLabs power meter
    https://github.com/Thorlabs/Light_Analysis_Examples/tree/main/Python/Thorlabs%20PMxxx%20Power%20Meters/TLPMX_dll
    """

    power_meter = PM101.init_power_meter()
    power_meter.setWavelength(user_wavelength)
    return power_meter

def create_csv_row(results):
    """Prepares a list of strings for writeline to append to a csv
    """
    csvs = [f"{value}," for value in results[:-1]]

    return [*csvs, results[-1]]

def take_measurements(with_pm, at_position, n_samples):
    """Takes measurements upon an Enter keypress, exits upon any other keypress.
    """
    enter_was_not_pressed = input("Please press 'Enter' to take a measurement ") != ''

    if enter_was_not_pressed:
        print("Finished!")
        return []
    else:
        measurements = [str(with_pm.measure()) for sample in range(0, n_samples)]

        results = [f"\n{at_position}", *measurements]
        return results

def save_measurements(fname, results):
    with open(fname, "a") as results_file:
        results_file.writelines(create_csv_row(results))
