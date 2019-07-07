from math import log


def levin_complexity(length, time):
    return length + log(time)
