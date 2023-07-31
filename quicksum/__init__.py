def sum_up(infile, group_by, sum_by, separator):
    try:
        line = next(infile)
    except StopIteration:
        return

    (group, sums) = parse_line(line, group_by, sum_by, separator)

    for line in infile:
        (current_group, values) = parse_line(line, group_by, sum_by, separator)
        if current_group != group:
            yield format_line(group, sums, separator)
            group = current_group
            sums = values
        else:
            for x in range(len(sums)):
                sums[x] += values[x]

    yield format_line(group, sums, separator)

def parse_line(line, group_by, sum_by, separator):
    fields = line.rstrip("\n").split(separator)
    group = [fields[x-1] for x in group_by]
    values = [int_or_float(fields[x-1]) for x in sum_by]
    return (group, values)

def format_line(group, values, separator):
    return separator.join(group + [str(x) for x in values])

def int_or_float(value):
    try:
        return int(value)
    except ValueError:
        return float(value)
