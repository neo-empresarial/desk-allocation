from csp import Constraint, CSP
from typing import Dict, List, Optional
import pandas as pd
import numpy as np
from itertools import combinations
from pprint import pprint


class OnePerDeskConstraint(Constraint[str, str]):
    def __init__(self, h1: str, h2: str) -> None:
        super().__init__([h1, h2])
        self.h1: str = h1
        self.h2: str = h2

    def satisfied(self, assignment: Dict[str, str]) -> bool:
        if self.h1 not in assignment or self.h2 not in assignment:
            return True
        return assignment[self.h1] != assignment[self.h2]

    pass


class SequentialTimeConstraint(Constraint[str, str]):
    def __init__(self, h1: str, h2: str) -> None:
        super().__init__([h1, h2])
        self.h1: str = h1
        self.h2: str = h2

    def satisfied(self, assignment: Dict[str, str]) -> bool:
        if self.h1 not in assignment or self.h2 not in assignment:
            return True
        return assignment[self.h1] == assignment[self.h2]

    pass


def add_one_per_desk_constraint(csp, vars_):
    df = pd.DataFrame(vars_, columns=["acronym", "day", "time"])

    day = (df['day'].drop_duplicates())
    time = (df['time'].drop_duplicates())

    dup = df[df.duplicated(['day', 'time'], keep=False)]
    unique = dup[['day', 'time']].drop_duplicates()

    for i in unique.itertuples():
        conflicts = list(
            combinations([
                tuple(y)
                for y in df.loc[(df['day'] == i.day)
                                & (df['time'] == i.time)].values.tolist()
            ], 2))
        for conflict in conflicts:
            csp.add_constraint(OnePerDeskConstraint(*conflict))
    pass


def add_sequential_time_same_desk_constraint(csp, vars_):
    df = pd.DataFrame(vars_, columns=["acronym", "day", "time"])
    df.time = [x + ':00' for x in df.time]
    df.time = pd.to_timedelta(df.time)
    ha = pd.Timedelta('00:50:00')
    df = df.sort_values(by=['day', 'time'])
    seq_p_person = []
    for ac in df.acronym.drop_duplicates():
        seq = df.loc[df.acronym == ac]
        for d in seq.day.drop_duplicates():
            seq_p_day = seq.loc[seq.day == d]
            seq_p_day['interval'] = (seq_p_day.time -
                                     seq_p_day.time.iloc[0]) / ha
            if seq_p_day['interval'].sum():
                seq_p_day = seq_p_day.reset_index(drop=True).drop(
                    columns=['interval'])
                mask = seq_p_day.time.diff().apply(lambda x: x == ha)
                seq_p_day.time = seq_p_day.time.apply(
                    lambda x:
                    f'{x.components.hours:02d}:{x.components.minutes:02d}'
                    if not pd.isnull(x) else '')
                indexes = (mask.index[mask == False].tolist())
                for idx, val in enumerate(indexes):
                    try:
                        seq_p_person.append(seq_p_day[val:indexes[idx + 1]])
                    except IndexError:
                        seq_p_person.append(seq_p_day[val:])
    seq = [
        list(combinations([tuple(x) for x in i.values.tolist()], 2))
        for i in seq_p_person
    ]
    for i in seq:
        for j in i:
            csp.add_constraint(SequentialTimeConstraint(*j))
    pass


def process_variables(times):
    variables: List[tuple] = []

    for member in times.keys():
        for time in times[member]:
            variables.append(tuple([member] + time))
    return variables


def process_domains(variables):
    domains: Dict[str, List[str]] = {}

    for variable in variables:
        domains[variable] = ["Note 1", "Note 2", "Note 3"]
    return domains


if __name__ == "__main__":
    a = {
        "JNR": [["Mon", "13:30"], ["Mon", "14:20"], ["Mon", "11:00"],
                ["Mon", "11:50"], ["Mon", "10:10"]],
        "FSN": [["Mon", "13:30"]],
        "PDK": [["Mon", "13:30"], ["Mon", "14:20"], ["Mon", "08:20"],
                ["Mon", "09:10"]],
        "MVG": [
            ["Fri", "11:00"],
        ],
    }

    variables = process_variables(a)

    domains = process_domains(variables)

    csp: CSP[str, str] = CSP(variables, domains)

    add_one_per_desk_constraint(csp, variables)

    add_sequential_time_same_desk_constraint(csp, variables)

    solution: Optional[Dict[str, str]] = csp.backtracking_search()

    if solution is None:
        pprint("No solution found!")
    else:
        pprint(solution)
        pass
