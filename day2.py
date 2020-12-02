from typing import List, Union, Dict

# return { char: 'x', count: [min, max], pword: str }
def create_pword_data(counts: List[int], char: str, pword: str) -> Dict:
    return {"char": char, "count": counts, "pword": pword}

# converts string "min-max char: str" into create_pword_data()
def get_pword_data(input: str) -> Dict:
    (prefix, pword) = input.split(":")
    (counts, char) = prefix.split(" ")
    (min_str, max_str) = counts.split("-")
    return {"char": char,
            "count": [int(min_str),int(max_str)],
            "pword": pword.strip()}

def get_pwords() -> List[Dict]:
    with open("day2.input.txt", "r") as input_file:
        return [get_pword_data(input_str) for input_str in input_file.readlines()]

def is_compliant(pword_data):
    char_count = pword_data["pword"].count(pword_data["char"])
    (min_count, max_count) = pword_data["count"]
    return char_count >= min_count and char_count <= max_count

if __name__ == '__main__':
    print ("first star:")
    pword_data = get_pwords()
    valid_pwords = [pword for pword in pword_data if is_compliant(pword)]
    print(len(valid_pwords))
    print ("second star:")
    
