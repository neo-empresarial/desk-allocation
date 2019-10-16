from setup import *
from main import verify_valididity

def test_verify_validity_invalid():
    with open('tests/invalid_schedule.json') as f:
      timeSchedule = json.load(f)
    assert verify_valididity(timeSchedule, validSlots) == "Invalid entries found. Please verify the following items: \n {'FSN': [['Sat', '11:50']], 'PDK': [['Mon', '16:22']]}"

def test_verify_validity_valid():
    with open('tests/valid_schedule.json') as f:
        timeSchedule = json.load(f)
    assert verify_valididity(timeSchedule, validSlots) == "No invalid entries found."
