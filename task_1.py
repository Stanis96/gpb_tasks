import csv


def find_unique_records(data: list) -> tuple[list[dict[str, str]], set]:
    u_set = set()
    d_set = set()
    res_list = list()
    for record in data:
        record_id = record["id"]
        if record_id not in u_set:
            u_set.add(record_id)
            res_list.append(record)
        else:
            d_set.add(record_id)
    return res_list, d_set


if __name__ == "__main__":
    try:
        data = list()
        with open("./f.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter="|")
            for row in reader:
                data.append(row)
        res = find_unique_records(data)
        print(f"Unique records:\n{res[0]}")
        if res[1]:
            print("\nPairs of records with the same ID:")
            for _id in res[1]:
                d_records = [record for record in data if record["id"] == _id]
                print(f"ID: {_id}, Pair: {d_records}")
        else:
            print("No duplicate records")
    except FileNotFoundError:
        print("File not found")
    except KeyboardInterrupt:
        print("Bye")
    except Exception as e:
        print(f"Unexpected error: {e}")
