class ElfSignal:
    bit_types = {'packet': 4, 'message': 14}
    start = -1

    def __init__(self, pth):
        with open(pth, "r") as f:
            self.signal = f.readline().strip()

    def find_start(self, bit_type="message"):
        if bit_type not in ["packet", "message"]:
            raise ValueError('bit_type must be one of ["packet", "message"]')

        if bit_type == "message" and self.start == -1:
            self.find_start("packet")
        
        offset = self.bit_types[bit_type]
        for i in range(offset, len(self.signal)):
            if len(set(self.signal[(i - offset):i])) == offset:
                self.start = i
                break
        
        print(f"{bit_type} start bit: {self.start}")
