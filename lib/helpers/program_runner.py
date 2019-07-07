import time
import signal

from lib.helpers.levin_complexity import levin_complexity


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

    complexity = levin_complexity(program.length, elapsed)
    print('OK. Result: %s with probability = %f, program length: %d, time limit: %f of %f, '
          'Levin complexity: %s' %
          (bits, prob, program.length, elapsed, maxtime, complexity))
    return bits, prob
