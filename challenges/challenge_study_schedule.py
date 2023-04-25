def study_schedule(permanence_period, target_time):
    try:
        counter = 0
        for acces, exit in permanence_period:
            if acces <= target_time <= exit:
                counter += 1
        return counter
    except TypeError:
        return None
