import time
import signal


def timeout_handler(signum, frame):
    raise Exception("Timed out!")


def run_program(program, input, maxtime):
    delay, interval = signal.setitimer(signal.ITIMER_REAL, maxtime, 0)
    old_hdl = signal.signal(signal.SIGALRM, timeout_handler)
    now = time.time()
    try:
        bits, prob = program.run(input)
    except Exception:
        elapsed = time.time() - now
        print('FAILED. Timeout error. Program length: %d, time limit: %f of %f' % (program.length, elapsed, maxtime))
        return None, 0
    finally:
        elapsed = time.time() - now
        if delay:
            delay = max(delay - elapsed, 0.000001)
        else:
            delay = 0
        signal.setitimer(signal.ITIMER_REAL, delay, interval)
        signal.signal(signal.SIGALRM, old_hdl)
    print('OK. Result: %s with probability = %f, program length: %d, time limit: %f of %f' %
          (bits, prob, program.length, elapsed, maxtime))
    return bits, prob


class LevinSearch:
    def __init__(self, stoppingCriterion):
        self.stoppingCriterion = stoppingCriterion

    def run(self, input, generator):
        complexities = {}
        levin_complexity = 1

        while True:
            program_length = 1
            generator.reset()
            while program_length <= levin_complexity:
                try:
                    program = next(generator)
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
                    bits, prob = run_program(program, input, program_time)
                    if bits and self.stoppingCriterion(prob):
                        return program, (bits, prob), program_time

            levin_complexity += 1
