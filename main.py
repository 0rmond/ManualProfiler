from PM import PM101 as pm
import time
import tomllib

import numpy as np

import measure
import plot
import questions

def load_user_settings(file="user_settings.toml"):

    with open(file, "rb") as f:
        user_settings = tomllib.load(f)

    return user_settings


def main(user_settings):

    power_meter = measure.init_pm_with(user_settings["wavelength_in_nm"])
    position = questions.ask_for_start()
    step_size = questions.ask_for_step_size()
    f, ax, line_collection = plot.init_plot()

    measuring = True
    while measuring:
        results = measure.take_measurements(power_meter, position, user_settings["n_samples"])
        if results: measure.save_measurements(user_settings["output_file"], results)
        else: measuring = False
        line_collection = plot.update_plot(user_settings["output_file"], f, line_collection)
        position += step_size

if __name__ == "__main__":
    main(load_user_settings())
