

class Constraint:
    pass


class Regexp(Constraint):
    def __init__(self, regexp: str):
        self.regexp = regexp


class ValueRange(Constraint):
    def __init__(self, min: int, max: int):
        self.range = [min, max]


