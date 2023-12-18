def foo(temperature):
    if temperature > 25:
        # If the temperature is greater than 25, return "Hot"
        return "Hot"
    elif 25 >= temperature >= 15:
        # If the temperature is between 25 and 15 (inclusive), return "Warm"
        return "Warm"
    else:
        # If the temperature is less than 15, return "Cold"
        return "Cold"