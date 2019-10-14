import pandas as pd
from pprint import pprint

a = pd.read_csv('../assets/solution.csv')

list_ = [a[a.day == x] for x in a.day.unique().tolist()]

list_ = [x.drop(columns=['restrictions']) for x in list_]

sch = pd.DataFrame(columns=[*['time'], *list_[0].acronym.unique().tolist()])

pprint(pd.concat([sch, pd.Series(list_[0].time.unique())]))
