import pandas as pd
import numpy as np
from pprint import pprint

a = pd.read_csv('app/api/assets/solution.csv')

list_ = [a[a.day == x] for x in ["Mon", "Tue", "Wed", "Thu", "Fri"]]

list_ = [x.drop(columns=['restrictions']) for x in list_]


def get_member_time(data):
    sch = pd.DataFrame(columns=[*data.acronym.unique().tolist()])

    sch = pd.concat([pd.Series(data.time.unique()), sch])
    sch = sch.rename(columns={0: 'time'}).set_index('time').sort_index()

    for i in data.iterrows():
        sch.at[i[1].time, i[1].acronym] = i[1].computer

    sch = sch.replace(np.NaN, '').to_dict('index')

    return sch


def make_table():
    return list(map(get_member_time, list_))


if __name__ == "__main__":
    pprint(make_table())