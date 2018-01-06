import subprocess


class Program:
    interpreter = 'python3'
    path = './lib/continue/continue.py'

    def __init__(self, depth, bits_to_predict):
        self.length = depth
        self.bits_to_predict = bits_to_predict

    def run(self, input):
        process = subprocess.Popen(
            [self.interpreter, self.path, '-d', str(self.length), '-n', str(self.bits_to_predict), input],
            stdout=subprocess.PIPE
        )
        out, err = process.communicate()
        out = out.decode('utf-8').rstrip().split(',')
        return out[0], float(out[1])
