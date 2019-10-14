import pandas as pd
import json

dfs = pd.read_html('intranet.html')

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']

members = list(dfs[0])[1:]
time_slots = {member: list() for member in members}

for i, df in enumerate(dfs):
    for member in members:
        member_slots = df[['horario', member]]
        work_slots = member_slots[member_slots[member].str.contains('NEO',
                                                                    na=False)]
        list_slots = [[days[i], slot, '']
                      for slot in work_slots['horario'].tolist()]
        time_slots[member].extend(list_slots)

with open('../assets/inputs.json', 'w') as jf:
    json.dump(time_slots, jf)
