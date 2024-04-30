class Suspect:
    def __init__(self, name):
        self.name = name
        self.statements = [None, None, None]

    def set_statements(self, statements):
        self.statements = statements

    def is_statements_valid(self, suspects):
        contradictions = {
            'A2': 'B1',
            'B3': 'C1',
            'C2': 'B2',
            'D3': 'A1'
        }
        for key, value in contradictions.items():
            person, statement = key[0], int(key[1]) - 1
            other_person, other_statement = value[0], int(value[1]) - 1
            if suspects[person].statements[statement] == suspects[other_person].statements[other_statement]:
                return False
        return True

def check_all_combinations(suspects):
    for statements in itertools.product([True, False], repeat=12):
        index = 0
        for suspect in suspects.values():
            suspect.set_statements(statements[index:index+3])
            index += 3

        if all(suspect.is_statements_valid(suspects) for suspect in suspects.values()):
            true_count = sum(statement for suspect in suspects.values() for statement in suspect.statements)
            if true_count == 6 and suspects['B'].statements[1]:
                return suspects['B'].name
    return None

suspects = {name: Suspect(name) for name in 'ABCD'}

import itertools
Dozd = check_all_combinations(suspects)
if Dozd:
    print(Dozd)
