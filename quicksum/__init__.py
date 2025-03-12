import sys

def sum_up(infile, group_by, sum_by, separator):
    try:
        line = next(infile)
    except StopIteration:
        return

    line_number = 1
    (group, sums) = parse_line(line, group_by, sum_by, separator, line_number)

    for line in infile:
        line_number+=1
        (current_group, values) = parse_line(line, group_by, sum_by, separator, line_number)
        if current_group != group:
            yield format_line(group, sums, separator)
            group = current_group
            sums = values
        else:
            for x in range(len(sums)):
                sums[x] += values[x]

    yield format_line(group, sums, separator)

def parse_line(line, group_by, sum_by, separator, line_number=None):
    try:
        fields = line.rstrip("\n").split(separator)
        group = [fields[x-1] for x in group_by]
        values = [int_or_float(fields[x-1]) for x in sum_by]
        return (group, values)
    except:
        print(f"Error parsing line number: {line_number}: {line=}", file=sys.stderr)
        raise

def format_line(group, values, separator):
    return separator.join(group + [str(x) for x in values])

def int_or_float(value):
    try:
        return int(value)
    except ValueError:
        return float(value)
