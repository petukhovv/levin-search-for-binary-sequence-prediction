from .helpers.program_runner import run_program


class LevinSearch:
    def __init__(self, stopping_criterion):
        self.stopping_criterion = stopping_criterion

    def run(self, program_input, program_list):
        # A mapping from a given maximum levin complexity to the associated programs
        complexities = {}
        # The maximum levin complexity of programs in the current iteration
        levin_complexity = 1

        while True:
            program_length = 1
            program_list.reset()

            # Generate all programs for the current (upper bound) levin complexity
            while program_length <= levin_complexity:
                try:
                    program = next(program_list)
                    program_length = program.length
                    # 2^complexity * 2^(-|program|) / 10
                    program_time_limit = 2 ** (levin_complexity - program_length) / 10
                except StopIteration:
                    break
                if program_length not in complexities:
                    complexities[program_length] = []

                complexities[program_length].append((program, program_time_limit))

            # Search using all programs for the current (upper bound) levin complexity
            for program_length in range(1, levin_complexity):
                if program_length not in complexities:
                    continue

                # All programs and runtime limits for a given maximum levin complexity
                for program, program_time_limit in complexities[program_length]:
                    bits, prob = run_program(program, program_input, program_time_limit)
                    if bits and self.stopping_criterion(prob):
                        return program, (bits, prob), program_time_limit

            levin_complexity += 1
