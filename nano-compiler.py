# THIS IS THE COMPILER THAT I MADE FOR COMPILING THE NANO::UX OPERATING SYSTEM      #
# THAT I MADE.                                                                      #

import argparse

parser = argparse.ArgumentParser(description='NANO::C (The compiler for NANO::UX...)')
parser.add_argument('--compile', type=str, required=True)
parser.add_argument('--output', type=str, required=True)
args = parser.parse_args()

number_of_lines_counted = 0
indent = 0

with open(args.output, 'w') as f:
    with open(args.compile) as topo_file:
        for line in topo_file:
            number_of_lines_counted = number_of_lines_counted + 1
            if line.startswith('$'):
                asm_file_contents
            