from typing import Any


class Dictionary:
    def __init__(self) -> None:
        self.lenght = 0
        self.hash_table = [[] for _ in range(8)]

    def get_hash(self, key: Any) -> int:
        return hash(key) % len(self.hash_table)

    def __setitem__(self, key: Any, value: Any) -> None:
        index = self.get_hash(key)
        table = self.hash_table[index]

        for item in table:
            if item["key"] == key:
                item["value"] = value
                return

        table.append({"key": key, "value": value})
        self.lenght += 1

    def __getitem__(self, key: Any) -> Any:
        index = self.get_hash(key)
        table = self.hash_table[index]

        for item in table:
            if item["key"] == key:
                return item["value"]

        raise KeyError(f"Key '{key}' not found")

    def __len__(self) -> int:
        return self.lenght
