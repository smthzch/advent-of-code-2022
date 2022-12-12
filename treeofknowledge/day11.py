from math import floor

class Monkey:
    def __init__(self, id, item_line, operator_line, test_lines):
        self.id = id
        self.items = [ int(x) for x in item_line.split(":")[1].split(",") ]
        op = "lambda old:" + operator_line.split(":")[1].split("=")[1]
        self.operation = eval(op)
        
        self.modulo = int(test_lines[0].split(" ")[-1])
        true_monkey = int(test_lines[1].split(" ")[-1])
        false_monkey = int(test_lines[2].split(" ")[-1])
        self.test = lambda x: (true_monkey, True) if x % self.modulo == 0 else (false_monkey, False)

        self.items_inspected = 0

    def inspect_items(self, relief, hcf):
        items = []
        while len(self.items) > 0:
            item = self.items.pop(0)
            new_item = self.operation(item)
            if relief:
                new_item = floor(new_item / 3)
            else:
                new_item = new_item % hcf

            to_monkey, test_result = self.test(new_item)
            items += [(new_item, to_monkey)]
            self.items_inspected += 1

        return items

    def take(self, item):
        self.items += [item]

class Monkeys:
    def __init__(self, pth):
        self.monkeys = []
        self.hcf = 1

        with open(pth) as rdr:
            line = rdr.readline()
            while line:
                self.parse_monkey(rdr)
                line = rdr.readline()

    def monkey_business(self, rounds, relief):
        for r in range(rounds):
            for monkey in self.monkeys:
                for item, to_monkey in monkey.inspect_items(relief, self.hcf):
                    self.monkeys[to_monkey].take(item)
        
        items_inspected = [m.items_inspected for m in self.monkeys]
        items_inspected.sort()
        monkey_business = items_inspected[-1] * items_inspected[-2]
        print(f"Total monkey business: {monkey_business}")

    def parse_monkey(self, rdr):
        item_line = rdr.readline().strip()
        operation_line = rdr.readline().strip()
        test_lines = [ rdr.readline().strip(), rdr.readline().strip(), rdr.readline().strip() ]
        rdr.readline() # dump empty line

        new_monkey = Monkey(len(self.monkeys), item_line, operation_line, test_lines)
        self.monkeys += [ new_monkey ]
        self.hcf *= new_monkey.modulo
