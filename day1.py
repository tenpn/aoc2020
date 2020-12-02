from typing import List, Union, Dict

def read_input() -> List[int]:
    with open("day1.input.txt", "r") as input_file:
        return [int(input_str) for input_str in input_file.readlines()]

# finds the first two ints in 'values' that sum to 'total', returns them as a tuple
def find_summing_pair(values: List[int], total: int) -> (int, int):
    for i in range(len(values)):
        for j in range(i+1, len(values)):
            if values[i]+values[j] == total:
                return (values[i], values[j])
    return None

if __name__ == '__main__':
    input = read_input()
    (v1, v2) = find_summing_pair(input, 2020)
    print(v1, v2, v1*v2)
