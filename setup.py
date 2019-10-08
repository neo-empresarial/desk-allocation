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
