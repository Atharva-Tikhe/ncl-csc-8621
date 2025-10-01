#!/usr/bin/python3
##
## Calculate the bill for a mobile company
##
## Author: Jennifer Warrender

## put appropriate values in here
TARIFF_1_RATE, TARIFF_1_MINS, TARIFF_1_TEXT = 20, 200, 150
TARIFF_2_RATE, TARIFF_2_MINS, TARIFF_2_TEXT = 35, 400, 350

TARIFFS = {1: [TARIFF_1_RATE, TARIFF_1_MINS, TARIFF_1_TEXT],
           2: [TARIFF_2_RATE, TARIFF_2_MINS, TARIFF_2_TEXT]}

EXTRA_MINS_RATE = 0.10 ## put appropriate value in here
EXTRA_TEXT_RATE = 0.05 ## put appropriate value in here


def available_tariffs():
    out = "{:8} {:9} {:7} {:5}"
    print(out.format("Tariff #", "Flat Rate", "Minutes", "Texts"))
    for tariff in TARIFFS.keys():
        inclusive = TARIFFS[tariff]
        print(out.format(tariff, inclusive[0], inclusive[1],
                         inclusive[2]))
    print()


## call the appropriate function(s) here
available_tariffs()


def calculate_extra(inclusive, used, rates):
    if used <= inclusive:
        return 0,0
    else:
        extra_tariffs = used - inclusive
        extra_cost = extra_tariffs * rates
        return extra_tariffs, extra_cost