# levin-search-for-binary-sequence-prediction

Use of the Levin (universal) search for binary sequence prediction problem

## Example of use

```
python3 main.py -p 100 -b 8 -s 0.45 -i 0111000101110111011001010111001001110100011110010111010101101001011011110111000001101100011010110110101001101000011001110110011001100100011100110110000101111010011110000110001101110110011000100110111001101101011011010110111001100010011101100110001101111000011110100110110001101011011010100110100001100111011001100110010001110011011000010111000001101111011010010111010101111001011101000111001001100101011101110111000101110001011101110110010101110010011101000111100101110101011010010110111101110000011011000110101101101010011010000110011101100110011001000111001101100001011110100111100001100011011101100110001001101110011011010110110101101110011000100111011001100011011110000111101001101100011010110110101001101000011001110110011001100100011100110110000101110000011011110110100101110101011110010111010001110010011001010111011101110001011100010111011101100101011100100111010001111001011101010110100101101111011100000110110001101011011010100110100001100111011001100110010001110011011000010111101001111000011000110111011001100010011011100110110101101101011011100110001001110110011000110111100001111010011011000110101101101010011010000110011101100110011001000111001101100001011100000110111101101001011101010111100101110100011100100110010101110111011100010111000101110111011001010111001001110100011110010111010101101001011011110111000001101100011010110110101001101000011001110110011001100100011100110110000101111010011110000110001101110110011000100110111001101101011011010110111001100010011101100110001101111000011110100110110001101011011010100110100001100111011001100110010001110011011000010111000001101111011010010111010101111001011101000111001001100101011101110111000101110001011101110110010101110010011101000111100101110101011010010110111101110000011011000110101101101010011010000110011101100110011001000111001101100001011110100111100001100011011101100110001001101110011011010110110101101110011000100111011001100011011110000111101001101100011010110110101001101000011001110110011001100100011100110110000101110000011011110110100101110101011110010111010001110010011001010111011101110001
```

## Program arguments

- **--program_max_length (p-)**: upper bound of programs length
- **--bits_to_predict (b-)**: bits number to predict
- **--stopping_criterion (s-)**: stopping criterion (satisfying the probability)
- **--input (i-)**: input binary sequence to predict

For binary sequence prediction is used [continue](https://github.com/PetukhovVictor/continue) (forked and adapted version for Levin search and used in this repo as submodule)

## Output

Program output is problem solution: predicted sequence for specified input sequence and bits to predict with the shortest program length and the shortest execution time (**the shortest Levin complexity**).

### Example output
Using input from "Example of use" section.

```
FAILED. Timeout error. Program length: 2, time limit: 0.051236 of 0.050000
FAILED. Timeout error. Program length: 2, time limit: 0.102999 of 0.100000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.096959 of 0.200000
FAILED. Timeout error. Program length: 2, time limit: 0.055083 of 0.050000
FAILED. Timeout error. Program length: 2, time limit: 0.101323 of 0.100000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.100206 of 0.200000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.100537 of 0.400000
FAILED. Timeout error. Program length: 3, time limit: 0.054761 of 0.050000
FAILED. Timeout error. Program length: 3, time limit: 0.104583 of 0.100000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.103438 of 0.200000
FAILED. Timeout error. Program length: 2, time limit: 0.051218 of 0.050000
FAILED. Timeout error. Program length: 2, time limit: 0.102156 of 0.100000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.103797 of 0.200000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.101052 of 0.400000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.097437 of 0.800000
FAILED. Timeout error. Program length: 3, time limit: 0.052961 of 0.050000
FAILED. Timeout error. Program length: 3, time limit: 0.100790 of 0.100000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.106956 of 0.200000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.109929 of 0.400000
FAILED. Timeout error. Program length: 4, time limit: 0.052856 of 0.050000
FAILED. Timeout error. Program length: 4, time limit: 0.104252 of 0.100000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.114959 of 0.200000
FAILED. Timeout error. Program length: 2, time limit: 0.051794 of 0.050000
FAILED. Timeout error. Program length: 2, time limit: 0.101096 of 0.100000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.101762 of 0.200000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.105450 of 0.400000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.105366 of 0.800000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.114684 of 1.600000
FAILED. Timeout error. Program length: 3, time limit: 0.050467 of 0.050000
FAILED. Timeout error. Program length: 3, time limit: 0.103252 of 0.100000
FAILED. Timeout error. Program length: 3, time limit: 0.200577 of 0.200000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.161329 of 0.400000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.143843 of 0.800000
FAILED. Timeout error. Program length: 4, time limit: 0.050398 of 0.050000
FAILED. Timeout error. Program length: 4, time limit: 0.104424 of 0.100000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.144809 of 0.200000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.114713 of 0.400000
FAILED. Timeout error. Program length: 5, time limit: 0.052670 of 0.050000
FAILED. Timeout error. Program length: 5, time limit: 0.104079 of 0.100000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.123873 of 0.200000
FAILED. Timeout error. Program length: 2, time limit: 0.053303 of 0.050000
FAILED. Timeout error. Program length: 2, time limit: 0.104590 of 0.100000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.118963 of 0.200000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.109223 of 0.400000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.097120 of 0.800000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.107661 of 1.600000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.107877 of 3.200000
FAILED. Timeout error. Program length: 3, time limit: 0.050339 of 0.050000
FAILED. Timeout error. Program length: 3, time limit: 0.100123 of 0.100000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.108495 of 0.200000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.133258 of 0.400000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.155587 of 0.800000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.127882 of 1.600000
FAILED. Timeout error. Program length: 4, time limit: 0.050957 of 0.050000
FAILED. Timeout error. Program length: 4, time limit: 0.101915 of 0.100000
FAILED. Timeout error. Program length: 4, time limit: 0.202839 of 0.200000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.207870 of 0.400000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.130662 of 0.800000
FAILED. Timeout error. Program length: 5, time limit: 0.051117 of 0.050000
FAILED. Timeout error. Program length: 5, time limit: 0.102177 of 0.100000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.125701 of 0.200000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.133088 of 0.400000
FAILED. Timeout error. Program length: 6, time limit: 0.053279 of 0.050000
FAILED. Timeout error. Program length: 6, time limit: 0.103826 of 0.100000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.127437 of 0.200000
FAILED. Timeout error. Program length: 2, time limit: 0.050111 of 0.050000
FAILED. Timeout error. Program length: 2, time limit: 0.100546 of 0.100000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.108786 of 0.200000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.087392 of 0.400000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.088020 of 0.800000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.084674 of 1.600000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.091062 of 3.200000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.091900 of 6.400000
FAILED. Timeout error. Program length: 3, time limit: 0.053211 of 0.050000
FAILED. Timeout error. Program length: 3, time limit: 0.102268 of 0.100000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.105920 of 0.200000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.097642 of 0.400000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.098614 of 0.800000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.099183 of 1.600000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.098616 of 3.200000
FAILED. Timeout error. Program length: 4, time limit: 0.053381 of 0.050000
FAILED. Timeout error. Program length: 4, time limit: 0.100444 of 0.100000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.105347 of 0.200000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.108816 of 0.400000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.104007 of 0.800000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.138515 of 1.600000
FAILED. Timeout error. Program length: 5, time limit: 0.053774 of 0.050000
FAILED. Timeout error. Program length: 5, time limit: 0.100142 of 0.100000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.117181 of 0.200000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.112059 of 0.400000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.111867 of 0.800000
FAILED. Timeout error. Program length: 6, time limit: 0.051081 of 0.050000
FAILED. Timeout error. Program length: 6, time limit: 0.104394 of 0.100000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.115576 of 0.200000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.110020 of 0.400000
FAILED. Timeout error. Program length: 7, time limit: 0.051581 of 0.050000
FAILED. Timeout error. Program length: 7, time limit: 0.103288 of 0.100000
OK. Result: 00110110 with probability = 0.081797, program length: 7, time limit: 0.125568 of 0.200000
FAILED. Timeout error. Program length: 2, time limit: 0.054145 of 0.050000
FAILED. Timeout error. Program length: 2, time limit: 0.100443 of 0.100000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.095292 of 0.200000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.090099 of 0.400000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.092461 of 0.800000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.089681 of 1.600000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.088022 of 3.200000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.088437 of 6.400000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.096687 of 12.800000
FAILED. Timeout error. Program length: 3, time limit: 0.050155 of 0.050000
FAILED. Timeout error. Program length: 3, time limit: 0.101935 of 0.100000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.107527 of 0.200000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.105029 of 0.400000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.098500 of 0.800000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.093070 of 1.600000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.094416 of 3.200000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.094489 of 6.400000
FAILED. Timeout error. Program length: 4, time limit: 0.054892 of 0.050000
FAILED. Timeout error. Program length: 4, time limit: 0.100266 of 0.100000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.102294 of 0.200000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.101998 of 0.400000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.103520 of 0.800000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.110965 of 1.600000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.105988 of 3.200000
FAILED. Timeout error. Program length: 5, time limit: 0.051270 of 0.050000
FAILED. Timeout error. Program length: 5, time limit: 0.104129 of 0.100000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.115680 of 0.200000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.110146 of 0.400000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.111513 of 0.800000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.107402 of 1.600000
FAILED. Timeout error. Program length: 6, time limit: 0.054084 of 0.050000
FAILED. Timeout error. Program length: 6, time limit: 0.102023 of 0.100000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.113253 of 0.200000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.113928 of 0.400000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.108957 of 0.800000
FAILED. Timeout error. Program length: 7, time limit: 0.053860 of 0.050000
FAILED. Timeout error. Program length: 7, time limit: 0.101940 of 0.100000
OK. Result: 00110110 with probability = 0.081797, program length: 7, time limit: 0.119628 of 0.200000
OK. Result: 00110110 with probability = 0.081797, program length: 7, time limit: 0.118754 of 0.400000
FAILED. Timeout error. Program length: 8, time limit: 0.050092 of 0.050000
FAILED. Timeout error. Program length: 8, time limit: 0.101752 of 0.100000
OK. Result: 01110101 with probability = 0.143849, program length: 8, time limit: 0.130109 of 0.200000
FAILED. Timeout error. Program length: 2, time limit: 0.051736 of 0.050000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.090867 of 0.100000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.090018 of 0.200000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.087571 of 0.400000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.092479 of 0.800000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.104402 of 1.600000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.087011 of 3.200000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.087889 of 6.400000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.101792 of 12.800000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.090456 of 25.600000
FAILED. Timeout error. Program length: 3, time limit: 0.050471 of 0.050000
FAILED. Timeout error. Program length: 3, time limit: 0.100567 of 0.100000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.092775 of 0.200000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.094065 of 0.400000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.096171 of 0.800000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.107910 of 1.600000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.100554 of 3.200000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.094127 of 6.400000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.092748 of 12.800000
FAILED. Timeout error. Program length: 4, time limit: 0.054245 of 0.050000
FAILED. Timeout error. Program length: 4, time limit: 0.104893 of 0.100000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.112457 of 0.200000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.106692 of 0.400000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.104897 of 0.800000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.107665 of 1.600000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.107072 of 3.200000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.107006 of 6.400000
FAILED. Timeout error. Program length: 5, time limit: 0.051954 of 0.050000
FAILED. Timeout error. Program length: 5, time limit: 0.101473 of 0.100000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.108774 of 0.200000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.105544 of 0.400000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.104938 of 0.800000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.144760 of 1.600000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.137671 of 3.200000
FAILED. Timeout error. Program length: 6, time limit: 0.053607 of 0.050000
FAILED. Timeout error. Program length: 6, time limit: 0.101435 of 0.100000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.180639 of 0.200000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.206077 of 0.400000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.119668 of 0.800000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.124143 of 1.600000
FAILED. Timeout error. Program length: 7, time limit: 0.053999 of 0.050000
FAILED. Timeout error. Program length: 7, time limit: 0.103425 of 0.100000
OK. Result: 00110110 with probability = 0.081797, program length: 7, time limit: 0.129831 of 0.200000
OK. Result: 00110110 with probability = 0.081797, program length: 7, time limit: 0.150766 of 0.400000
OK. Result: 00110110 with probability = 0.081797, program length: 7, time limit: 0.167164 of 0.800000
FAILED. Timeout error. Program length: 8, time limit: 0.052134 of 0.050000
FAILED. Timeout error. Program length: 8, time limit: 0.103218 of 0.100000
OK. Result: 01110101 with probability = 0.143849, program length: 8, time limit: 0.155282 of 0.200000
OK. Result: 01110101 with probability = 0.143849, program length: 8, time limit: 0.151524 of 0.400000
FAILED. Timeout error. Program length: 9, time limit: 0.052688 of 0.050000
FAILED. Timeout error. Program length: 9, time limit: 0.100613 of 0.100000
FAILED. Timeout error. Program length: 9, time limit: 0.200900 of 0.200000
FAILED. Timeout error. Program length: 2, time limit: 0.050587 of 0.050000
FAILED. Timeout error. Program length: 2, time limit: 0.100731 of 0.100000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.103243 of 0.200000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.111162 of 0.400000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.113494 of 0.800000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.109775 of 1.600000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.101689 of 3.200000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.101073 of 6.400000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.105776 of 12.800000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.101907 of 25.600000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.099109 of 51.200000
FAILED. Timeout error. Program length: 3, time limit: 0.052120 of 0.050000
FAILED. Timeout error. Program length: 3, time limit: 0.105118 of 0.100000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.109442 of 0.200000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.109889 of 0.400000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.100618 of 0.800000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.111591 of 1.600000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.102673 of 3.200000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.113191 of 6.400000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.110191 of 12.800000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.107073 of 25.600000
FAILED. Timeout error. Program length: 4, time limit: 0.052409 of 0.050000
FAILED. Timeout error. Program length: 4, time limit: 0.102704 of 0.100000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.115116 of 0.200000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.112590 of 0.400000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.108016 of 0.800000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.116406 of 1.600000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.107643 of 3.200000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.122618 of 6.400000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.148733 of 12.800000
FAILED. Timeout error. Program length: 5, time limit: 0.050545 of 0.050000
FAILED. Timeout error. Program length: 5, time limit: 0.101755 of 0.100000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.134380 of 0.200000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.121721 of 0.400000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.275858 of 0.800000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.134713 of 1.600000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.139263 of 3.200000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.141004 of 6.400000
FAILED. Timeout error. Program length: 6, time limit: 0.050492 of 0.050000
FAILED. Timeout error. Program length: 6, time limit: 0.100113 of 0.100000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.152209 of 0.200000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.118434 of 0.400000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.126133 of 0.800000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.122080 of 1.600000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.116614 of 3.200000
FAILED. Timeout error. Program length: 7, time limit: 0.052602 of 0.050000
FAILED. Timeout error. Program length: 7, time limit: 0.100222 of 0.100000
OK. Result: 00110110 with probability = 0.081797, program length: 7, time limit: 0.122731 of 0.200000
OK. Result: 00110110 with probability = 0.081797, program length: 7, time limit: 0.116831 of 0.400000
OK. Result: 00110110 with probability = 0.081797, program length: 7, time limit: 0.116261 of 0.800000
OK. Result: 00110110 with probability = 0.081797, program length: 7, time limit: 0.120272 of 1.600000
FAILED. Timeout error. Program length: 8, time limit: 0.054429 of 0.050000
FAILED. Timeout error. Program length: 8, time limit: 0.102364 of 0.100000
OK. Result: 01110101 with probability = 0.143849, program length: 8, time limit: 0.123370 of 0.200000
OK. Result: 01110101 with probability = 0.143849, program length: 8, time limit: 0.122200 of 0.400000
OK. Result: 01110101 with probability = 0.143849, program length: 8, time limit: 0.125913 of 0.800000
FAILED. Timeout error. Program length: 9, time limit: 0.051895 of 0.050000
FAILED. Timeout error. Program length: 9, time limit: 0.104038 of 0.100000
OK. Result: 01110000 with probability = 0.245243, program length: 9, time limit: 0.144999 of 0.200000
OK. Result: 01110000 with probability = 0.245243, program length: 9, time limit: 0.132712 of 0.400000
FAILED. Timeout error. Program length: 10, time limit: 0.054132 of 0.050000
FAILED. Timeout error. Program length: 10, time limit: 0.100649 of 0.100000
OK. Result: 01110111 with probability = 0.356102, program length: 10, time limit: 0.148535 of 0.200000
FAILED. Timeout error. Program length: 2, time limit: 0.050532 of 0.050000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.088226 of 0.100000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.090002 of 0.200000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.088191 of 0.400000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.086573 of 0.800000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.086622 of 1.600000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.089201 of 3.200000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.089275 of 6.400000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.086673 of 12.800000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.090719 of 25.600000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.093523 of 51.200000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.088460 of 102.400000
FAILED. Timeout error. Program length: 3, time limit: 0.052875 of 0.050000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.102850 of 0.100000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.094737 of 0.200000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.093254 of 0.400000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.093398 of 0.800000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.095605 of 1.600000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.093937 of 3.200000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.117260 of 6.400000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.141886 of 12.800000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.118471 of 25.600000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.098212 of 51.200000
FAILED. Timeout error. Program length: 4, time limit: 0.052913 of 0.050000
FAILED. Timeout error. Program length: 4, time limit: 0.102639 of 0.100000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.111872 of 0.200000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.129030 of 0.400000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.113288 of 0.800000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.104818 of 1.600000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.102126 of 3.200000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.106373 of 6.400000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.109080 of 12.800000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.110404 of 25.600000
FAILED. Timeout error. Program length: 5, time limit: 0.051825 of 0.050000
FAILED. Timeout error. Program length: 5, time limit: 0.104565 of 0.100000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.111874 of 0.200000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.159901 of 0.400000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.174663 of 0.800000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.154390 of 1.600000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.120883 of 3.200000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.106797 of 6.400000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.104401 of 12.800000
FAILED. Timeout error. Program length: 6, time limit: 0.052912 of 0.050000
FAILED. Timeout error. Program length: 6, time limit: 0.102490 of 0.100000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.125711 of 0.200000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.117439 of 0.400000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.109834 of 0.800000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.105095 of 1.600000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.105679 of 3.200000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.112355 of 6.400000
FAILED. Timeout error. Program length: 7, time limit: 0.051502 of 0.050000
FAILED. Timeout error. Program length: 7, time limit: 0.103261 of 0.100000
OK. Result: 00110110 with probability = 0.081797, program length: 7, time limit: 0.134038 of 0.200000
OK. Result: 00110110 with probability = 0.081797, program length: 7, time limit: 0.130000 of 0.400000
OK. Result: 00110110 with probability = 0.081797, program length: 7, time limit: 0.123774 of 0.800000
OK. Result: 00110110 with probability = 0.081797, program length: 7, time limit: 0.118656 of 1.600000
OK. Result: 00110110 with probability = 0.081797, program length: 7, time limit: 0.123266 of 3.200000
FAILED. Timeout error. Program length: 8, time limit: 0.054620 of 0.050000
FAILED. Timeout error. Program length: 8, time limit: 0.102127 of 0.100000
OK. Result: 01110101 with probability = 0.143849, program length: 8, time limit: 0.144398 of 0.200000
OK. Result: 01110101 with probability = 0.143849, program length: 8, time limit: 0.127758 of 0.400000
OK. Result: 01110101 with probability = 0.143849, program length: 8, time limit: 0.159349 of 0.800000
OK. Result: 01110101 with probability = 0.143849, program length: 8, time limit: 0.131594 of 1.600000
FAILED. Timeout error. Program length: 9, time limit: 0.053252 of 0.050000
FAILED. Timeout error. Program length: 9, time limit: 0.104356 of 0.100000
OK. Result: 01110000 with probability = 0.245243, program length: 9, time limit: 0.139561 of 0.200000
OK. Result: 01110000 with probability = 0.245243, program length: 9, time limit: 0.165826 of 0.400000
OK. Result: 01110000 with probability = 0.245243, program length: 9, time limit: 0.135543 of 0.800000
FAILED. Timeout error. Program length: 10, time limit: 0.052367 of 0.050000
FAILED. Timeout error. Program length: 10, time limit: 0.102564 of 0.100000
OK. Result: 01110111 with probability = 0.356102, program length: 10, time limit: 0.148633 of 0.200000
OK. Result: 01110111 with probability = 0.356102, program length: 10, time limit: 0.134708 of 0.400000
FAILED. Timeout error. Program length: 11, time limit: 0.055125 of 0.050000
FAILED. Timeout error. Program length: 11, time limit: 0.105117 of 0.100000
OK. Result: 01110111 with probability = 0.355710, program length: 11, time limit: 0.142601 of 0.200000
FAILED. Timeout error. Program length: 2, time limit: 0.050928 of 0.050000
FAILED. Timeout error. Program length: 2, time limit: 0.103359 of 0.100000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.094595 of 0.200000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.089732 of 0.400000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.089442 of 0.800000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.099291 of 1.600000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.096154 of 3.200000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.089738 of 6.400000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.091136 of 12.800000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.097229 of 25.600000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.094752 of 51.200000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.092103 of 102.400000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.093917 of 204.800000
FAILED. Timeout error. Program length: 3, time limit: 0.052071 of 0.050000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.098472 of 0.100000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.098931 of 0.200000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.101374 of 0.400000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.099013 of 0.800000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.094809 of 1.600000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.096554 of 3.200000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.099380 of 6.400000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.099580 of 12.800000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.093607 of 25.600000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.097979 of 51.200000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.091896 of 102.400000
FAILED. Timeout error. Program length: 4, time limit: 0.053224 of 0.050000
FAILED. Timeout error. Program length: 4, time limit: 0.101545 of 0.100000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.102031 of 0.200000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.106270 of 0.400000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.104555 of 0.800000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.098128 of 1.600000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.098449 of 3.200000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.100432 of 6.400000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.112144 of 12.800000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.108197 of 25.600000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.107448 of 51.200000
FAILED. Timeout error. Program length: 5, time limit: 0.051738 of 0.050000
FAILED. Timeout error. Program length: 5, time limit: 0.102409 of 0.100000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.113780 of 0.200000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.109648 of 0.400000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.113375 of 0.800000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.108559 of 1.600000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.109301 of 3.200000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.108286 of 6.400000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.103184 of 12.800000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.102208 of 25.600000
FAILED. Timeout error. Program length: 6, time limit: 0.051116 of 0.050000
FAILED. Timeout error. Program length: 6, time limit: 0.101911 of 0.100000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.116255 of 0.200000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.113326 of 0.400000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.112364 of 0.800000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.109618 of 1.600000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.116858 of 3.200000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.120903 of 6.400000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.115744 of 12.800000
FAILED. Timeout error. Program length: 7, time limit: 0.054733 of 0.050000
FAILED. Timeout error. Program length: 7, time limit: 0.103542 of 0.100000
OK. Result: 00110110 with probability = 0.081797, program length: 7, time limit: 0.124715 of 0.200000
OK. Result: 00110110 with probability = 0.081797, program length: 7, time limit: 0.119132 of 0.400000
OK. Result: 00110110 with probability = 0.081797, program length: 7, time limit: 0.120162 of 0.800000
OK. Result: 00110110 with probability = 0.081797, program length: 7, time limit: 0.120336 of 1.600000
OK. Result: 00110110 with probability = 0.081797, program length: 7, time limit: 0.123755 of 3.200000
OK. Result: 00110110 with probability = 0.081797, program length: 7, time limit: 0.120875 of 6.400000
FAILED. Timeout error. Program length: 8, time limit: 0.050376 of 0.050000
FAILED. Timeout error. Program length: 8, time limit: 0.104422 of 0.100000
OK. Result: 01110101 with probability = 0.143849, program length: 8, time limit: 0.139926 of 0.200000
OK. Result: 01110101 with probability = 0.143849, program length: 8, time limit: 0.177843 of 0.400000
OK. Result: 01110101 with probability = 0.143849, program length: 8, time limit: 0.136624 of 0.800000
OK. Result: 01110101 with probability = 0.143849, program length: 8, time limit: 0.134321 of 1.600000
OK. Result: 01110101 with probability = 0.143849, program length: 8, time limit: 0.128775 of 3.200000
FAILED. Timeout error. Program length: 9, time limit: 0.052241 of 0.050000
FAILED. Timeout error. Program length: 9, time limit: 0.102440 of 0.100000
OK. Result: 01110000 with probability = 0.245243, program length: 9, time limit: 0.130386 of 0.200000
OK. Result: 01110000 with probability = 0.245243, program length: 9, time limit: 0.130763 of 0.400000
OK. Result: 01110000 with probability = 0.245243, program length: 9, time limit: 0.127449 of 0.800000
OK. Result: 01110000 with probability = 0.245243, program length: 9, time limit: 0.128192 of 1.600000
FAILED. Timeout error. Program length: 10, time limit: 0.051971 of 0.050000
FAILED. Timeout error. Program length: 10, time limit: 0.100634 of 0.100000
OK. Result: 01110111 with probability = 0.356102, program length: 10, time limit: 0.126933 of 0.200000
OK. Result: 01110111 with probability = 0.356102, program length: 10, time limit: 0.130278 of 0.400000
OK. Result: 01110111 with probability = 0.356102, program length: 10, time limit: 0.136124 of 0.800000
FAILED. Timeout error. Program length: 11, time limit: 0.050347 of 0.050000
FAILED. Timeout error. Program length: 11, time limit: 0.103971 of 0.100000
OK. Result: 01110111 with probability = 0.355710, program length: 11, time limit: 0.140453 of 0.200000
OK. Result: 01110111 with probability = 0.355710, program length: 11, time limit: 0.140346 of 0.400000
FAILED. Timeout error. Program length: 12, time limit: 0.050981 of 0.050000
FAILED. Timeout error. Program length: 12, time limit: 0.101509 of 0.100000
OK. Result: 01110111 with probability = 0.355699, program length: 12, time limit: 0.163916 of 0.200000
FAILED. Timeout error. Program length: 2, time limit: 0.051617 of 0.050000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.089320 of 0.100000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.097145 of 0.200000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.089981 of 0.400000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.086220 of 0.800000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.088901 of 1.600000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.092160 of 3.200000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.091298 of 6.400000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.086698 of 12.800000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.087379 of 25.600000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.089401 of 51.200000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.089505 of 102.400000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.086361 of 204.800000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.092061 of 409.600000
FAILED. Timeout error. Program length: 3, time limit: 0.054941 of 0.050000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.098714 of 0.100000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.090920 of 0.200000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.092544 of 0.400000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.094668 of 0.800000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.095336 of 1.600000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.091871 of 3.200000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.095793 of 6.400000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.095544 of 12.800000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.091817 of 25.600000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.094975 of 51.200000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.101561 of 102.400000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.095226 of 204.800000
FAILED. Timeout error. Program length: 4, time limit: 0.052704 of 0.050000
FAILED. Timeout error. Program length: 4, time limit: 0.100476 of 0.100000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.102130 of 0.200000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.097144 of 0.400000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.097320 of 0.800000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.101254 of 1.600000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.101784 of 3.200000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.097096 of 6.400000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.109953 of 12.800000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.101506 of 25.600000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.094282 of 51.200000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.095099 of 102.400000
FAILED. Timeout error. Program length: 5, time limit: 0.050554 of 0.050000
FAILED. Timeout error. Program length: 5, time limit: 0.103803 of 0.100000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.111027 of 0.200000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.104910 of 0.400000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.105997 of 0.800000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.106373 of 1.600000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.103282 of 3.200000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.111021 of 6.400000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.103090 of 12.800000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.104419 of 25.600000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.110881 of 51.200000
FAILED. Timeout error. Program length: 6, time limit: 0.053878 of 0.050000
FAILED. Timeout error. Program length: 6, time limit: 0.101239 of 0.100000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.112461 of 0.200000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.110499 of 0.400000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.106557 of 0.800000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.109473 of 1.600000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.114599 of 3.200000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.110329 of 6.400000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.112359 of 12.800000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.106568 of 25.600000
FAILED. Timeout error. Program length: 7, time limit: 0.051814 of 0.050000
FAILED. Timeout error. Program length: 7, time limit: 0.101971 of 0.100000
OK. Result: 00110110 with probability = 0.081797, program length: 7, time limit: 0.109755 of 0.200000
OK. Result: 00110110 with probability = 0.081797, program length: 7, time limit: 0.111427 of 0.400000
OK. Result: 00110110 with probability = 0.081797, program length: 7, time limit: 0.112518 of 0.800000
OK. Result: 00110110 with probability = 0.081797, program length: 7, time limit: 0.121024 of 1.600000
OK. Result: 00110110 with probability = 0.081797, program length: 7, time limit: 0.112512 of 3.200000
OK. Result: 00110110 with probability = 0.081797, program length: 7, time limit: 0.113130 of 6.400000
OK. Result: 00110110 with probability = 0.081797, program length: 7, time limit: 0.112108 of 12.800000
FAILED. Timeout error. Program length: 8, time limit: 0.050209 of 0.050000
FAILED. Timeout error. Program length: 8, time limit: 0.104226 of 0.100000
OK. Result: 01110101 with probability = 0.143849, program length: 8, time limit: 0.121329 of 0.200000
OK. Result: 01110101 with probability = 0.143849, program length: 8, time limit: 0.119471 of 0.400000
OK. Result: 01110101 with probability = 0.143849, program length: 8, time limit: 0.120568 of 0.800000
OK. Result: 01110101 with probability = 0.143849, program length: 8, time limit: 0.124119 of 1.600000
OK. Result: 01110101 with probability = 0.143849, program length: 8, time limit: 0.127773 of 3.200000
OK. Result: 01110101 with probability = 0.143849, program length: 8, time limit: 0.120950 of 6.400000
FAILED. Timeout error. Program length: 9, time limit: 0.054165 of 0.050000
FAILED. Timeout error. Program length: 9, time limit: 0.104805 of 0.100000
OK. Result: 01110000 with probability = 0.245243, program length: 9, time limit: 0.124455 of 0.200000
OK. Result: 01110000 with probability = 0.245243, program length: 9, time limit: 0.125189 of 0.400000
OK. Result: 01110000 with probability = 0.245243, program length: 9, time limit: 0.126989 of 0.800000
OK. Result: 01110000 with probability = 0.245243, program length: 9, time limit: 0.123028 of 1.600000
OK. Result: 01110000 with probability = 0.245243, program length: 9, time limit: 0.122676 of 3.200000
FAILED. Timeout error. Program length: 10, time limit: 0.053569 of 0.050000
FAILED. Timeout error. Program length: 10, time limit: 0.100773 of 0.100000
OK. Result: 01110111 with probability = 0.356102, program length: 10, time limit: 0.133786 of 0.200000
OK. Result: 01110111 with probability = 0.356102, program length: 10, time limit: 0.127454 of 0.400000
OK. Result: 01110111 with probability = 0.356102, program length: 10, time limit: 0.133793 of 0.800000
OK. Result: 01110111 with probability = 0.356102, program length: 10, time limit: 0.130174 of 1.600000
FAILED. Timeout error. Program length: 11, time limit: 0.051813 of 0.050000
FAILED. Timeout error. Program length: 11, time limit: 0.102318 of 0.100000
OK. Result: 01110111 with probability = 0.355710, program length: 11, time limit: 0.134655 of 0.200000
OK. Result: 01110111 with probability = 0.355710, program length: 11, time limit: 0.142208 of 0.400000
OK. Result: 01110111 with probability = 0.355710, program length: 11, time limit: 0.134995 of 0.800000
FAILED. Timeout error. Program length: 12, time limit: 0.050956 of 0.050000
FAILED. Timeout error. Program length: 12, time limit: 0.105080 of 0.100000
OK. Result: 01110111 with probability = 0.355699, program length: 12, time limit: 0.143473 of 0.200000
OK. Result: 01110111 with probability = 0.355699, program length: 12, time limit: 0.142811 of 0.400000
FAILED. Timeout error. Program length: 13, time limit: 0.054433 of 0.050000
FAILED. Timeout error. Program length: 13, time limit: 0.102637 of 0.100000
OK. Result: 01110111 with probability = 0.356240, program length: 13, time limit: 0.147356 of 0.200000
FAILED. Timeout error. Program length: 2, time limit: 0.053560 of 0.050000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.090055 of 0.100000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.084844 of 0.200000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.085236 of 0.400000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.084769 of 0.800000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.084138 of 1.600000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.084622 of 3.200000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.083036 of 6.400000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.086294 of 12.800000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.086457 of 25.600000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.084337 of 51.200000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.085811 of 102.400000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.091205 of 204.800000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.084535 of 409.600000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.083032 of 819.200000
FAILED. Timeout error. Program length: 3, time limit: 0.054872 of 0.050000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.092282 of 0.100000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.089369 of 0.200000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.089642 of 0.400000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.089321 of 0.800000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.090565 of 1.600000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.089926 of 3.200000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.089463 of 6.400000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.090187 of 12.800000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.097633 of 25.600000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.092043 of 51.200000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.090487 of 102.400000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.096937 of 204.800000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.089306 of 409.600000
FAILED. Timeout error. Program length: 4, time limit: 0.054041 of 0.050000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.093989 of 0.100000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.095103 of 0.200000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.096163 of 0.400000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.095170 of 0.800000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.097724 of 1.600000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.102035 of 3.200000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.097133 of 6.400000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.094606 of 12.800000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.095481 of 25.600000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.096241 of 51.200000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.096672 of 102.400000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.093797 of 204.800000
FAILED. Timeout error. Program length: 5, time limit: 0.054200 of 0.050000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.099285 of 0.100000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.098819 of 0.200000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.104373 of 0.400000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.106511 of 0.800000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.100698 of 1.600000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.101259 of 3.200000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.122514 of 6.400000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.127021 of 12.800000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.101242 of 25.600000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.100582 of 51.200000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.100152 of 102.400000
FAILED. Timeout error. Program length: 6, time limit: 0.053633 of 0.050000
FAILED. Timeout error. Program length: 6, time limit: 0.103535 of 0.100000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.112841 of 0.200000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.107092 of 0.400000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.104436 of 0.800000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.104198 of 1.600000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.106112 of 3.200000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.117097 of 6.400000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.106113 of 12.800000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.105390 of 25.600000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.106236 of 51.200000
FAILED. Timeout error. Program length: 7, time limit: 0.052876 of 0.050000
FAILED. Timeout error. Program length: 7, time limit: 0.102329 of 0.100000
OK. Result: 00110110 with probability = 0.081797, program length: 7, time limit: 0.112616 of 0.200000
OK. Result: 00110110 with probability = 0.081797, program length: 7, time limit: 0.113524 of 0.400000
OK. Result: 00110110 with probability = 0.081797, program length: 7, time limit: 0.112125 of 0.800000
OK. Result: 00110110 with probability = 0.081797, program length: 7, time limit: 0.112678 of 1.600000
OK. Result: 00110110 with probability = 0.081797, program length: 7, time limit: 0.110501 of 3.200000
OK. Result: 00110110 with probability = 0.081797, program length: 7, time limit: 0.113312 of 6.400000
OK. Result: 00110110 with probability = 0.081797, program length: 7, time limit: 0.111258 of 12.800000
OK. Result: 00110110 with probability = 0.081797, program length: 7, time limit: 0.115281 of 25.600000
FAILED. Timeout error. Program length: 8, time limit: 0.052207 of 0.050000
FAILED. Timeout error. Program length: 8, time limit: 0.100793 of 0.100000
OK. Result: 01110101 with probability = 0.143849, program length: 8, time limit: 0.117671 of 0.200000
OK. Result: 01110101 with probability = 0.143849, program length: 8, time limit: 0.117121 of 0.400000
OK. Result: 01110101 with probability = 0.143849, program length: 8, time limit: 0.120789 of 0.800000
OK. Result: 01110101 with probability = 0.143849, program length: 8, time limit: 0.116216 of 1.600000
OK. Result: 01110101 with probability = 0.143849, program length: 8, time limit: 0.118261 of 3.200000
OK. Result: 01110101 with probability = 0.143849, program length: 8, time limit: 0.118646 of 6.400000
OK. Result: 01110101 with probability = 0.143849, program length: 8, time limit: 0.117903 of 12.800000
FAILED. Timeout error. Program length: 9, time limit: 0.051418 of 0.050000
FAILED. Timeout error. Program length: 9, time limit: 0.104446 of 0.100000
OK. Result: 01110000 with probability = 0.245243, program length: 9, time limit: 0.129645 of 0.200000
OK. Result: 01110000 with probability = 0.245243, program length: 9, time limit: 0.124335 of 0.400000
OK. Result: 01110000 with probability = 0.245243, program length: 9, time limit: 0.127812 of 0.800000
OK. Result: 01110000 with probability = 0.245243, program length: 9, time limit: 0.132104 of 1.600000
OK. Result: 01110000 with probability = 0.245243, program length: 9, time limit: 0.123924 of 3.200000
OK. Result: 01110000 with probability = 0.245243, program length: 9, time limit: 0.126171 of 6.400000
FAILED. Timeout error. Program length: 10, time limit: 0.050728 of 0.050000
FAILED. Timeout error. Program length: 10, time limit: 0.105037 of 0.100000
OK. Result: 01110111 with probability = 0.356102, program length: 10, time limit: 0.163765 of 0.200000
OK. Result: 01110111 with probability = 0.356102, program length: 10, time limit: 0.261305 of 0.400000
OK. Result: 01110111 with probability = 0.356102, program length: 10, time limit: 0.200257 of 0.800000
OK. Result: 01110111 with probability = 0.356102, program length: 10, time limit: 0.136763 of 1.600000
OK. Result: 01110111 with probability = 0.356102, program length: 10, time limit: 0.145671 of 3.200000
FAILED. Timeout error. Program length: 11, time limit: 0.050354 of 0.050000
FAILED. Timeout error. Program length: 11, time limit: 0.102883 of 0.100000
OK. Result: 01110111 with probability = 0.355710, program length: 11, time limit: 0.159078 of 0.200000
OK. Result: 01110111 with probability = 0.355710, program length: 11, time limit: 0.172643 of 0.400000
OK. Result: 01110111 with probability = 0.355710, program length: 11, time limit: 0.147629 of 0.800000
OK. Result: 01110111 with probability = 0.355710, program length: 11, time limit: 0.156933 of 1.600000
FAILED. Timeout error. Program length: 12, time limit: 0.052629 of 0.050000
FAILED. Timeout error. Program length: 12, time limit: 0.104796 of 0.100000
OK. Result: 01110111 with probability = 0.355699, program length: 12, time limit: 0.170885 of 0.200000
OK. Result: 01110111 with probability = 0.355699, program length: 12, time limit: 0.169717 of 0.400000
OK. Result: 01110111 with probability = 0.355699, program length: 12, time limit: 0.163994 of 0.800000
FAILED. Timeout error. Program length: 13, time limit: 0.052701 of 0.050000
FAILED. Timeout error. Program length: 13, time limit: 0.100222 of 0.100000
FAILED. Timeout error. Program length: 13, time limit: 0.203055 of 0.200000
OK. Result: 01110111 with probability = 0.356240, program length: 13, time limit: 0.272254 of 0.400000
FAILED. Timeout error. Program length: 14, time limit: 0.053939 of 0.050000
FAILED. Timeout error. Program length: 14, time limit: 0.102175 of 0.100000
OK. Result: 01110111 with probability = 0.354416, program length: 14, time limit: 0.166035 of 0.200000
FAILED. Timeout error. Program length: 2, time limit: 0.052614 of 0.050000
FAILED. Timeout error. Program length: 2, time limit: 0.102685 of 0.100000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.099206 of 0.200000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.102062 of 0.400000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.116784 of 0.800000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.094519 of 1.600000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.097587 of 3.200000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.095235 of 6.400000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.095141 of 12.800000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.093081 of 25.600000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.090012 of 51.200000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.090752 of 102.400000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.095632 of 204.800000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.091742 of 409.600000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.087356 of 819.200000
OK. Result: 10110110 with probability = 0.027525, program length: 2, time limit: 0.086521 of 1638.400000
FAILED. Timeout error. Program length: 3, time limit: 0.050333 of 0.050000
FAILED. Timeout error. Program length: 3, time limit: 0.103907 of 0.100000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.100215 of 0.200000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.098620 of 0.400000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.111842 of 0.800000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.100666 of 1.600000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.103737 of 3.200000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.095434 of 6.400000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.095727 of 12.800000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.097052 of 25.600000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.094950 of 51.200000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.094960 of 102.400000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.093180 of 204.800000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.085176 of 409.600000
OK. Result: 10110110 with probability = 0.020493, program length: 3, time limit: 0.092414 of 819.200000
FAILED. Timeout error. Program length: 4, time limit: 0.055224 of 0.050000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.092355 of 0.100000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.089190 of 0.200000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.093727 of 0.400000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.090846 of 0.800000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.090852 of 1.600000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.091389 of 3.200000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.091886 of 6.400000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.091910 of 12.800000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.089488 of 25.600000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.093716 of 51.200000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.099959 of 102.400000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.091546 of 204.800000
OK. Result: 10110110 with probability = 0.017345, program length: 4, time limit: 0.090500 of 409.600000
FAILED. Timeout error. Program length: 5, time limit: 0.050794 of 0.050000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.095372 of 0.100000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.093446 of 0.200000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.095349 of 0.400000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.097823 of 0.800000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.095912 of 1.600000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.096567 of 3.200000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.094399 of 6.400000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.101404 of 12.800000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.097912 of 25.600000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.103232 of 51.200000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.096060 of 102.400000
OK. Result: 10110110 with probability = 0.021968, program length: 5, time limit: 0.098566 of 204.800000
FAILED. Timeout error. Program length: 6, time limit: 0.050390 of 0.050000
FAILED. Timeout error. Program length: 6, time limit: 0.101273 of 0.100000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.102218 of 0.200000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.100905 of 0.400000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.101623 of 0.800000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.100092 of 1.600000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.111084 of 3.200000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.110803 of 6.400000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.147602 of 12.800000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.191058 of 25.600000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.179879 of 51.200000
OK. Result: 10110011 with probability = 0.014346, program length: 6, time limit: 0.107873 of 102.400000
FAILED. Timeout error. Program length: 7, time limit: 0.050451 of 0.050000
FAILED. Timeout error. Program length: 7, time limit: 0.102585 of 0.100000
OK. Result: 00110110 with probability = 0.081797, program length: 7, time limit: 0.117346 of 0.200000
OK. Result: 00110110 with probability = 0.081797, program length: 7, time limit: 0.120236 of 0.400000
OK. Result: 00110110 with probability = 0.081797, program length: 7, time limit: 0.124633 of 0.800000
OK. Result: 00110110 with probability = 0.081797, program length: 7, time limit: 0.120482 of 1.600000
OK. Result: 00110110 with probability = 0.081797, program length: 7, time limit: 0.116435 of 3.200000
OK. Result: 00110110 with probability = 0.081797, program length: 7, time limit: 0.120172 of 6.400000
OK. Result: 00110110 with probability = 0.081797, program length: 7, time limit: 0.120570 of 12.800000
OK. Result: 00110110 with probability = 0.081797, program length: 7, time limit: 0.111432 of 25.600000
OK. Result: 00110110 with probability = 0.081797, program length: 7, time limit: 0.117352 of 51.200000
FAILED. Timeout error. Program length: 8, time limit: 0.052317 of 0.050000
FAILED. Timeout error. Program length: 8, time limit: 0.103732 of 0.100000
OK. Result: 01110101 with probability = 0.143849, program length: 8, time limit: 0.141263 of 0.200000
OK. Result: 01110101 with probability = 0.143849, program length: 8, time limit: 0.162185 of 0.400000
OK. Result: 01110101 with probability = 0.143849, program length: 8, time limit: 0.132148 of 0.800000
OK. Result: 01110101 with probability = 0.143849, program length: 8, time limit: 0.139973 of 1.600000
OK. Result: 01110101 with probability = 0.143849, program length: 8, time limit: 0.126492 of 3.200000
OK. Result: 01110101 with probability = 0.143849, program length: 8, time limit: 0.124800 of 6.400000
OK. Result: 01110101 with probability = 0.143849, program length: 8, time limit: 0.136041 of 12.800000
OK. Result: 01110101 with probability = 0.143849, program length: 8, time limit: 0.127547 of 25.600000
FAILED. Timeout error. Program length: 9, time limit: 0.054181 of 0.050000
FAILED. Timeout error. Program length: 9, time limit: 0.103964 of 0.100000
OK. Result: 01110000 with probability = 0.245243, program length: 9, time limit: 0.123970 of 0.200000
OK. Result: 01110000 with probability = 0.245243, program length: 9, time limit: 0.120771 of 0.400000
OK. Result: 01110000 with probability = 0.245243, program length: 9, time limit: 0.128590 of 0.800000
OK. Result: 01110000 with probability = 0.245243, program length: 9, time limit: 0.128965 of 1.600000
OK. Result: 01110000 with probability = 0.245243, program length: 9, time limit: 0.126753 of 3.200000
OK. Result: 01110000 with probability = 0.245243, program length: 9, time limit: 0.124594 of 6.400000
OK. Result: 01110000 with probability = 0.245243, program length: 9, time limit: 0.127641 of 12.800000
FAILED. Timeout error. Program length: 10, time limit: 0.051884 of 0.050000
FAILED. Timeout error. Program length: 10, time limit: 0.102979 of 0.100000
OK. Result: 01110111 with probability = 0.356102, program length: 10, time limit: 0.138852 of 0.200000
OK. Result: 01110111 with probability = 0.356102, program length: 10, time limit: 0.128926 of 0.400000
OK. Result: 01110111 with probability = 0.356102, program length: 10, time limit: 0.133559 of 0.800000
OK. Result: 01110111 with probability = 0.356102, program length: 10, time limit: 0.128186 of 1.600000
OK. Result: 01110111 with probability = 0.356102, program length: 10, time limit: 0.135128 of 3.200000
OK. Result: 01110111 with probability = 0.356102, program length: 10, time limit: 0.132874 of 6.400000
FAILED. Timeout error. Program length: 11, time limit: 0.051155 of 0.050000
FAILED. Timeout error. Program length: 11, time limit: 0.100088 of 0.100000
OK. Result: 01110111 with probability = 0.355710, program length: 11, time limit: 0.138965 of 0.200000
OK. Result: 01110111 with probability = 0.355710, program length: 11, time limit: 0.138970 of 0.400000
OK. Result: 01110111 with probability = 0.355710, program length: 11, time limit: 0.134295 of 0.800000
OK. Result: 01110111 with probability = 0.355710, program length: 11, time limit: 0.141137 of 1.600000
OK. Result: 01110111 with probability = 0.355710, program length: 11, time limit: 0.149846 of 3.200000
FAILED. Timeout error. Program length: 12, time limit: 0.052005 of 0.050000
FAILED. Timeout error. Program length: 12, time limit: 0.105104 of 0.100000
OK. Result: 01110111 with probability = 0.355699, program length: 12, time limit: 0.144325 of 0.200000
OK. Result: 01110111 with probability = 0.355699, program length: 12, time limit: 0.147604 of 0.400000
OK. Result: 01110111 with probability = 0.355699, program length: 12, time limit: 0.147857 of 0.800000
OK. Result: 01110111 with probability = 0.355699, program length: 12, time limit: 0.143787 of 1.600000
FAILED. Timeout error. Program length: 13, time limit: 0.052136 of 0.050000
FAILED. Timeout error. Program length: 13, time limit: 0.105110 of 0.100000
OK. Result: 01110111 with probability = 0.356240, program length: 13, time limit: 0.156210 of 0.200000
OK. Result: 01110111 with probability = 0.356240, program length: 13, time limit: 0.148174 of 0.400000
OK. Result: 01110111 with probability = 0.356240, program length: 13, time limit: 0.152366 of 0.800000
FAILED. Timeout error. Program length: 14, time limit: 0.050512 of 0.050000
FAILED. Timeout error. Program length: 14, time limit: 0.103855 of 0.100000
OK. Result: 01110111 with probability = 0.354416, program length: 14, time limit: 0.154169 of 0.200000
OK. Result: 01110111 with probability = 0.354416, program length: 14, time limit: 0.144141 of 0.400000
FAILED. Timeout error. Program length: 15, time limit: 0.052809 of 0.050000
FAILED. Timeout error. Program length: 15, time limit: 0.100899 of 0.100000
OK. Result: 01110001 with probability = 0.490130, program length: 15, time limit: 0.166119 of 0.200000
=================================
Levin search finished.
Result: 01110001 with probability = 0.490130 (in time: 0.200000) for program with length = 15, Levin complexity = 12.678072
```
