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
