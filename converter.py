import itertools
import pprint
import functools
import re
from dataclasses import dataclass
from bintrees import RBTree
from typing import NamedTuple


@dataclass
class ConversionInterval:
    start: int
    end: int
    destStart: int

NO_MAPPING = -1
@dataclass
class Converter:
    source_type: str
    dest_type: str
    mappings: list[ConversionInterval]
    
    def __init__(self, conversion_text):
        lines = conversion_text.split('\n')
        name_line = lines[0]
        conversion_lines = lines[1:]
        self.source_type, self.dest_type = re.findall(r'([a-zA-Z]+)-to-([a-zA-Z]+) map:', name_line)[0]
        # create tree
        conversions = [list(map(int, line.split(' '))) for line in conversion_lines]
        conversions = sorted(conversions, key=lambda l: l[1])
        self.mappings = [ConversionInterval(source_start,source_start + conv_range, dest_start) for dest_start, source_start, conv_range in conversions] 
        
    

def merge_converters(source_conv: Converter, dest_conv: Converter)->Converter:
    source_mappings = source_conv.mappings
    for mapping in source_mappings:
        # convert mapping
        int_range = mapping.end - mapping.start
        new_interval = [mapping.destStart, mapping.destStart + int_range]
        
        # merge with those intervals
def get_seeds(seeds_text):
        pattern = r'seeds: *((?:\d+\s*)+)'
        seeds = re.findall(pattern, seeds_text)[0]
        return [int(seed) for seed in seeds.split(' ')]
if __name__ == '__main__':
    file_name = 'input.txt'
    with open(file_name, 'r') as f:
        input = f.read()
    input = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""
    # parse input into sections(maybe by /n/n)
    sections = input.split('\n\n')
    seeds_text = sections[0]
    conversions = sections[1:]
    seeds = get_seeds(seeds_text)
    
    converters = [Converter(conversion) for conversion in conversions]
    pprint.pp(converters)

    merge_converters(converters[0], converters[1])
    # how do we merge two conversions into one converter of all the intervals
    