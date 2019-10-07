# from constraint import *
from setup import *

def verify_valididity(dict_, valid):
    invalid = {}
    for key, val in dict_.items():
        for slot in val:
            if slot not in validSlots:
                if invalid.get(key): 
                    invalid[key].append(slot)
                else:
                    invalid[key] = [slot,]
    if bool(invalid.values()):
        return("Invalid entries found. Please verify the following items: \n {}".format(invalid))
    else:
        return("No invalid entries found.")
