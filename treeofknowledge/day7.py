class File:
    def __init__(self, name, size):
        self.name, self.size = name, int(size)
    
class Directory:
    def __init__(self, name, parent_dir):
        self.name = name
        self.parent_dir = parent_dir
        self.sub_dirs = {}
        self.files = []
        self.size = -1

    def add_item(self, info, name):
        if info[0] == "d":
            self.sub_dirs[name] = Directory(name, self)
        else:
            self.files += [File(name, info)]

    def get_size(self):
        self.size = sum([f.size for f in self.files])
        self.size += sum([d.get_size() for d in self.sub_dirs.values()])
        return self.size

class FileSystem:
    def __init__(self, pth):
        self.root = Directory("/", None)
        self.current_dir = self.root

        # read in the command line
        with open(pth, "r") as rdr:
            rdr.readline() # skip first line: $ cd /
            for line in rdr.readlines():
                chunks = line.strip().split(" ")
                # command line
                if chunks[0] == "$":
                    if chunks[1] == "ls":
                        continue # this is implicitly handled by there not being a $ next
                    elif chunks[1] == "cd":
                        if chunks[2] == "..":
                            self.current_dir = self.current_dir.parent_dir
                        else:
                            self.current_dir = self.current_dir.sub_dirs[chunks[2]]
                # dir or file listing
                else:
                    self.current_dir.add_item(chunks[0], chunks[1])

        self.root.get_size()

    def sum_dirs(self, max_size=100000):
        total_size = 0

        # traverse tree structure w/ breadth first search
        to_size = list(self.root.sub_dirs.values()) # a queue       
        while len(to_size) > 0:
            cwd = to_size.pop(0)
            to_size += list(cwd.sub_dirs.values()) # add subdirs to queue
            total_size += cwd.size if cwd.size <= max_size else 0
            
        print(f"Total size <= {max_size}: {total_size}")

    def to_delete(self, total_size=70000000, size_needed=30000000):
        unused = total_size - self.root.size
        shortfall = size_needed - unused
        smallest = self.root.size

        to_size = list(self.root.sub_dirs.values())
        while len(to_size) > 0:
            cwd = to_size.pop(0)
            to_size += list(cwd.sub_dirs.values()) # add subdirs to queue
            smallest = min(smallest, cwd.size) if cwd.size >= shortfall else smallest
            
        print(f"Minimum rm size >= {shortfall}: {smallest}")
