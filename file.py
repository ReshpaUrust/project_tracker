def process_grades(records: list[str]) -> dict:
    result = {
        "valid_count": 0,
        "average": 0.0,
        "passed": [],
        "skipped": 0
    }

    total = 0

    for record in records:
        parts = record.split(":")

        if len(parts) != 2:
            result["skipped"] += 1
            continue

        surname = parts[0].strip()
        grade_text = parts[1].strip()

        if not surname or not grade_text.isdigit():
            result["skipped"] += 1
            continue

        grade = int(grade_text)

        if grade < 0 or grade > 100:
            result["skipped"] += 1
            continue

        result["valid_count"] += 1
        total += grade

        if grade >= 60 and surname not in result["passed"]:
            result["passed"].append(surname)

    if result["valid_count"] > 0:
        result["average"] = round(total / result["valid_count"], 1)

    result["passed"].sort()

    return print(result)

process_grades(records = [
    "Иванов: 85",
    "Петров: 42",
    "Сидоров: abc",
    "Козлов: 90",
    ": 55",
    "Иванов: 70"
])

