import sys
import argparse
from . import sum_up

def list_int(values):
    return list(map(int, values.split(',')))

def main(args=None):
    if args == None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser(description='Group by and sum columns of input')

    parser.add_argument('-t', metavar='CHAR', dest="separator", default="\t", help='use CHAR as input and output field separator. Defaults to tab.')
    parser.add_argument('-g', '-u', '--group-by', '--unique-by',  dest="group_by", type=list_int, default=[1], help='Comma-separated list of fields to group / unique by. Defaults to 1.')
    parser.add_argument('-s', '--sum', dest="sum_by", type=list_int, default=[2], help='Comma-separated list of fields to sum up. Defaults to 1.')
    parser.add_argument('infile', nargs='?', type=argparse.FileType('r'), default=sys.stdin)

    parsed_args = parser.parse_args(args)

    if len(parsed_args.separator) != 1:
        parser.error("separator CHAR must be exactly 1 character")

    summed = sum_up(
        parsed_args.infile,
        parsed_args.group_by,
        parsed_args.sum_by,
        parsed_args.separator
    )

    for line in summed:
        print(line)

if __name__ == "__main__":
    main()
