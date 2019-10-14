import itertools
import json

members = [
    "AGK", "DFG", "FSN", "GCA", "JNR", "JVA", "LAB", "LCZ", "LIT", "LPC",
    "MON", "MVG", "PDK", "VRN", "YAB"
]

weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]

timeSlots = [
    "07:30", "08:20", "09:10", "10:10", "11:00", "11:50", "12:40", "13:30",
    "14:20", "15:10", "16:20", "17:10", "18:00"
]

computerSlots = ["Note 1", "Note 2"]

validSlots = list(map(list, (itertools.product(weekdays, timeSlots))))


def verify_valididity(dict_, valid):
    invalid = {}
    for key, val in dict_.items():
        for slot in val:
            if slot not in validSlots:
                if invalid.get(key):
                    invalid[key].append(slot)
                else:
                    invalid[key] = [
                        slot,
                    ]
    if bool(invalid.values()):
        return (
            "Invalid entries found. Please verify the following items: \n {}".
            format(invalid))
    else:
        return ("No invalid entries found.")
