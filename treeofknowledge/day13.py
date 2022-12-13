from itertools import chain
from copy import deepcopy

class Decoder:
    def __init__(self, pth):
        self.pairs = []
        with open(pth) as rdr:
            pair = []
            for i, line in enumerate(rdr):
                if (i + 1) % 3 == 0:
                    self.pairs += [pair]
                    pair = []
                    continue
                pair += [eval(line.strip())]

        self.pairs += [pair]

    def correct(self):
        num_correct = 0
        for i, pair in enumerate(self.pairs):
            correct = self.compare(pair[0], pair[1])
            num_correct += (i + 1) if correct == 1 else 0

        print(f"Sum of correct indices {num_correct}")

    def bubble_sort(self, divider_packets=[ [[2]], [[6]] ]):
        packets = list(chain.from_iterable(self.pairs)) + divider_packets

        any_swaps = True
        while any_swaps:
            any_swaps = False
            for i in range(len(packets) - 1):
                correct = self.compare(packets[i], packets[i + 1])
                if correct == -1:
                    packets[i], packets[i + 1] = packets[i + 1], packets[i]
                    any_swaps = True
        
        decoder_key = 1
        for i, packet in enumerate(packets):
            if packet in divider_packets:
                decoder_key *= (i + 1)

        print(f"Decoder key: {decoder_key}")   

    def compare(self, x, y):
        x, y = deepcopy(x), deepcopy(y)
        correct = 0
        
        # check types
        if isinstance(x, list) and not isinstance(y, list):
            y = [y]
        elif isinstance(y, list) and not isinstance(x, list):
            x = [x]
        
        # compare
        if isinstance(x, list) and isinstance(y, list):
            while correct == 0:
                if len(x) == 0 and len(y) == 0:
                    break
                elif len(x) == 0 and len(y) > 0:
                    correct = 1
                    break
                elif len(x) > 0 and len(y) == 0:
                    correct = -1
                    break

                x_ = x.pop(0)
                y_ = y.pop(0)
                correct = self.compare(x_, y_)
        else:
            # 1 for correct, -1 for incorrect, 0 for undetermined
            correct = 1 if x < y else 0 if x == y else -1
        
        return correct
