import pandas as pd
from pprint import pprint

a = pd.read_csv('../assets/solution.csv')

list_ = [a[a.day == x] for x in a.day.unique().tolist()]

list_ = [x.drop(columns=['restrictions']) for x in list_]


def get_member_time(data):
    sch = pd.DataFrame(columns=[*data.acronym.unique().tolist()])

    sch = pd.concat([pd.Series(data.time.unique()), sch])
    sch = sch.rename(columns={0: 'time'}).set_index('time')

    for i in data.iterrows():
        sch.at[i[1].time, i[1].acronym] = i[1].computer

    sch.to_csv('assets/{}}.csv'.format(), encoding='utf-8', index=True)


pprint(list(map(get_member_time, list_)))