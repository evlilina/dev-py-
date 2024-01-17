import json
def task() -> float:
    with open ('input.json', 'r') as file:
        data = json.load(file)
        total = sum(item["score"]*item["weight"] for item in data)

        return(f"{total:.3f}")


print(task())


