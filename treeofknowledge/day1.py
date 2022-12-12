def get_elf_cals(pth):
    # read file line by line accumulating values until an empty line is reached
    # add value to final list and restart accumulating values
    # return final list of values
    elf_cals = []
    with open(pth, "r") as rdr:
        total_cals = 0
        for line in rdr:
            cals = int('0' + line.strip()) # append 0 at start so can parse empty string as int
            if cals > 0:
                # increment current elf calories
                total_cals += cals
            elif cals == 0:
                # end current elf and add to final list
                elf_cals += [total_cals]
                # restart calorie counter
                total_cals = 0
            else:
                raise ValueError
        # don't forget to add final elf to list
        elf_cals += [total_cals] # can also do elf_cals.append(total_cals)

    return elf_cals
