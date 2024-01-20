a = [[1, 2, 3], [4, 5, 6]]


def list_to_dict(lst: list[list]) -> list[dict]:
    return [dict(zip(["k{}".format(i + 1) for i in range(len(x))], x)) for x in lst]


if __name__ == "__main__":
    res = list_to_dict(a)
    print(f"Result: {res}")
