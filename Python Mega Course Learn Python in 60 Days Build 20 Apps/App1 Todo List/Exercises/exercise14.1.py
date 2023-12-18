# Define a function named water_state that takes one parameter: temperature
def water_state(temperature):
    # Check if the temperature is less than or equal to 0
    if temperature <= 0:
        return "Solid"  # Return "Solid" if temperature is <= 0
    # Check if the temperature is between 0 and 100 (exclusive)
    elif 0 < temperature < 100:
        return "Liquid"  # Return "Liquid" if temperature is between 0 and 100
    else:
        return "Gas"  # Return "Gas" for all other cases