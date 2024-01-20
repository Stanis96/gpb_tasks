m = [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]


def calculate(m: list[set[int]]) -> tuple[int, int, float | int, tuple]:
    count_total = sum(len(i) for i in m)
    sum_total = sum(sum(i) for i in m)
    avg_total = sum_total / count_total
    new_tuple = tuple(m)
    return count_total, sum_total, avg_total, new_tuple


if __name__ == "__main__":
    try:
        count_total, sum_total, avg_total, new_tuple = calculate(m)
        print(f"1. The common count of numbers: {count_total}")
        print(f"2. The common sum of numbers: {sum_total}")
        print(f"3. The common average of numbers: {avg_total}")
        print(f"4. All sets in one tuple: {new_tuple}")
    except Exception as e:
        print(f"Unexpected error: {e}")
