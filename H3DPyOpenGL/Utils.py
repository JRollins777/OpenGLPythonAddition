def map_value(current_min, current_max, new_min, new_max, value):
    # A/(current_max-current_min) = B/(new_max-new_min)
    current_range = current_max-current_min
    new_range = new_max-new_min
    return new_min+new_range * ((value - current_min)/current_range)

