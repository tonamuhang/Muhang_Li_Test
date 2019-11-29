class Line:

    # The first point will always be the one on the left
    def __init__(self, p1, p2):
        if p1 < p2:
            self.p1 = p1
            self.p2 = p2
        else:
            self.p1 = p2
            self.p2 = p1

    def check_overlap(self, line):
        first_first_l, second_first_l = self.check_first(line)
        first_second_l, second_second_l = self.check_second(line)

        if (first_first_l and second_first_l) or (not first_second_l and not second_second_l):
            return False
        else:
            return True

    def check_first(self, line):
        return self.p1 < line.p1, self.p2 < line.p1

    def check_second(self, line):
        return self.p1 < line.p2, self.p2 < line.p2

