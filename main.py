import argparse

from lib.LevinSearch import LevinSearch
from lib.ProgramList import ProgramList
from lib.Program import Program
from lib.helpers.levin_complexity import levin_complexity


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--program_max_length', '-p', type=int, help='program max length')
    parser.add_argument('--input', '-i', type=str, help='input binary sequence to predict')
    parser.add_argument('--bits_to_predict', '-b', type=int, help='bits number to predict')
    parser.add_argument('--stopping_criterion', '-s', type=float, help='stopping criterion (max probability)')
    args = parser.parse_args()
    return args.program_max_length, args.input, args.bits_to_predict, args.stopping_criterion


if __name__ == "__main__":
    program_max_length, input, bits_to_predict, stopping_criterion = parse_args()

    program_list = ProgramList([Program(length, bits_to_predict) for length in range(2, program_max_length)])

    program, (bits, prob), time = LevinSearch(lambda result: result >= stopping_criterion).run(input, program_list)
    complexity = levin_complexity(program.length, time)

    print('=================================')
    print('Levin search finished.')
    print('Result: %s with probability = %f (in time: %f) for program with length = %d, Levin complexity = %f' %
          (bits, prob, time, program.length, complexity))
