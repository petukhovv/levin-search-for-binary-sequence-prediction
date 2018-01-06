import argparse
from math import log2

from lib.LevinSearch import LevinSearch
from lib.ProgramList import ProgramList
from lib.Program import Program

parser = argparse.ArgumentParser()
parser.add_argument('--program_max_length', '-p', nargs=1, type=int, help='program max length')
parser.add_argument('--input', '-i', nargs=1, type=str, help='input binary sequence to predict')
parser.add_argument('--bits_to_predict', '-b', nargs=1, type=int, help='bits number to predict')
parser.add_argument('--stopping_criterion', '-s', nargs=1, type=float, help='stopping criterion (max probability)')
args = parser.parse_args()

program_max_length = args.program_max_length[0]
input = args.input[0]
bits_to_predict = args.bits_to_predict[0]
stopping_criterion = args.stopping_criterion[0]


program_list = ProgramList([Program(length, bits_to_predict) for length in range(2, program_max_length)])

program, result, time = LevinSearch(lambda result: result >= stopping_criterion).run(input, program_list)
bits, prob = result
levin_complexity = program.length + log2(time)

print('=================================')
print('Levin search finished.')
print('Result: %s with probability = %f (in time: %f) for program with length = %d, Levin complexity = %f' %
      (bits, prob, time, program.length, levin_complexity))
