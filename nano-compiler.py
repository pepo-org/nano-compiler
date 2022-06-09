# THIS IS THE COMPILER THAT I MADE FOR COMPILING THE NANO::UX OPERATING SYSTEM      #
# THAT I MADE.                                                                      #

import argparse

parser = argparse.ArgumentParser(description='NANO::C (The compiler for NANO::UX...)')
parser.add_argument('--compile', type=str, required=True)
parser.add_argument('--output', type=str, required=True)
args = parser.parse_args()

DEBUG = True

number_of_lines_counted = 0
indent = 0

with open(args.output, 'w') as f:
    with open(args.compile) as topo_file:
        for line in topo_file:
            number_of_lines_counted = number_of_lines_counted + 1
            if line.startswith('$'):
                if DEBUG == True:
                    f.write(';' + line[1:])
                    print('Found a comment! This comment is ' + str(len(line[1:])) + ' characters long...')
                elif DEBUG == False:
                    f.write(';' + line[1:])
            elif line.startswith('function '):
                if DEBUG == True:
                    function_name = str(line[9:]).split()[0]
                    function_name_with_args = line[9:]
                    args = function_name_with_args[len(function_name) + 1:].split(', ')
                    print('A function was declared with the name of `' + function_name + '`...')
                    print('The function comes with ' + str(len(args)) + ' arguments, and those arguments are `' + str(args) + '`...')
                elif DEBUG == False:
                    function_name = str(line[9:]).split()[0]
                    function_name_with_args = line[9:]
                    args = function_name_with_args[len(function_name) + 1:].split(', ')