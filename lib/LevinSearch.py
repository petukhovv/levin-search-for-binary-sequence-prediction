from .helpers.program_runner import run_program


class LevinSearch:
    def __init__(self, stopping_criterion):
        self.stopping_criterion = stopping_criterion

    def run(self, program_input, program_list):
        complexities = {}
        levin_complexity = 1

        while True:
            program_length = 1
            program_list.reset()
            while program_length <= levin_complexity:
                try:
                    program = next(program_list)
                    program_length = program.length
                    program_time = 2 ** (levin_complexity - program_length) / 10
                except StopIteration:
                    break
                if program_length not in complexities:
                    complexities[program_length] = [(program, program_time)]
                else:
                    complexities[program_length].append((program, program_time))

            for program_length in range(1, levin_complexity):
                if program_length not in complexities:
                    continue
                for program, program_time in complexities[program_length]:
                    bits, prob = run_program(program, program_input, program_time)
                    if bits and self.stopping_criterion(prob):
                        return program, (bits, prob), program_time

            levin_complexity += 1
