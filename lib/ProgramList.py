class ProgramList:
    def __init__(self, programs):
        self.programs = programs
        self.program_number = 0

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def reset(self):
        self.program_number = 0

    def next(self):
        if self.program_number < len(self.programs):
            next_program = self.programs[self.program_number]
            self.program_number += 1
            return next_program
        else:
            raise StopIteration()
