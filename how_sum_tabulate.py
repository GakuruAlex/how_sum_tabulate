from typing import List
def how_sum_tabulate(target_sum: int, numbers: List[int]) -> List[int]:
    """_Determine how a given target sum can be achieved , given a list of integers_

    Args:
        target_sum (int): _Desired sum_
        numbers (List[int]): _Integers to choose from_

    Returns:
        List[int]: _A list of integers that sum up to target value_
    """

    how_sum_table: List[List[int]] = [None for _ in range(target_sum + 1)]
    print(how_sum_table)
    how_sum_table[0] = []
    for index, value in enumerate(how_sum_table):
        for number in numbers:
            if value != None and index + number < len(how_sum_table):
                how_sum_table[index + number] = how_sum_table[index][:]
                how_sum_table[index + number].append(number)
    print(how_sum_table)
    return how_sum_table[target_sum]

def main()-> None:
    target_sum: int = 8
    numbers: list[int] = [2, 3, 5]
    how_sum: List[int] = how_sum_tabulate(target_sum = target_sum, numbers = numbers)

    print(f"Numbers in {numbers} that can achieve a sum of {target_sum} are: {how_sum}")

if __name__ == "__main__":
    main()