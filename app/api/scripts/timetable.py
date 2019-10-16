import pandas as pd
import numpy as np
from pprint import pprint

sol = pd.read_csv('app/api/assets/solution.csv')

list_ = [sol[sol.day == x] for x in ["Mon", "Tue", "Wed", "Thu", "Fri"]]

list_ = [x.drop(columns=['restrictions']) for x in list_]


def get_member_time_matrix(data):
    mtrx = pd.DataFrame(columns=[*data.acronym.unique().tolist()])

    mtrx = pd.concat([pd.Series(data.time.unique()), mtrx])
    mtrx = mtrx.rename(columns={0: 'time'}).set_index('time').sort_index()

    for i in data.iterrows():
        mtrx.at[i[1].time, i[1].acronym] = i[1].computer

    mtrx = mtrx.replace(np.NaN, '').to_dict('index')

    return mtrx


def make_table():
    return list(map(get_member_time_matrix, list_))


if __name__ == "__main__":
    pprint(make_table())
