from csp import Constraint, CSP
from typing import Dict, List, Optional
import pandas as pd
import numpy as np
from itertools import combinations


class SameTimeConstraint(Constraint[str, str]):
    def __init__(self, allocation1: str, allocation2: str) -> None:
        super().__init__([allocation1, allocation2])
        self.allocation1: str = allocation1
        self.allocation2: str = allocation2

    def satisfied(self, assignment: Dict[str, str]) -> bool:
        # If either allocation is not in the assignment then it is not
        # yet possible for their colors to be conflicting
        if self.allocation1 not in assignment or self.allocation2 not in assignment:
            return True
        # check the color assigned to allocation1 is not the same as the
        # color assigned to allocation2
        return assignment[self.allocation1] != assignment[self.allocation2]


if __name__ == "__main__":
    a = {
        "JNR": [["Mon", "13:30"], ["Mon", "14:20"], ["Fri", "11:00"]],
        "FSN": [["Mon", "13:30"]],
        "PDK": [["Mon", "13:30"]],
        "MVG": [["Fri", "11:00"]],
    }

    variables: List[tuple] = []
    for member in a.keys():
        for time in a[member]:
            variables.append(tuple([member] + time))
    df = pd.DataFrame(variables, columns=["acronym", "day", "time"])
    sameTimeSlots = {}

    day = (df['day'].drop_duplicates())
    time = (df['time'].drop_duplicates())

    dup = df[df.duplicated(['day', 'time'], keep=False)]
    unique = dup[['day', 'time']].drop_duplicates()
    for i in unique.itertuples():
        print(
            list(
                combinations(
                    df.loc[(df['day'] == i.day)
                           & (df['time'] == i.time)].values.tolist(), 2)))

    domains: Dict[str, List[str]] = {}

    for variable in variables:
        domains[variable] = ["Note 1", "Note 2"]

    csp: CSP[str, str] = CSP(variables, domains)

    csp.add_constraint(
        SameTimeConstraint(('FSN', 'Mon', '13:30'), ('JNR', 'Mon', '13:30')))

solution: Optional[Dict[str, str]] = csp.backtracking_search()
if solution is None:
    print("No solution found!")
else:
    print(solution)
