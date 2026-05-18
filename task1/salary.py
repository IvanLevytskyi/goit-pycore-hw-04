def total_salary(path):
    total = 0
    count = 0

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                name, salary = line.strip().split(",")
                total += int(salary)
                count += 1

        average = total / count if count > 0 else 0

        return total, average

    except FileNotFoundError:
        print("File not found.")
        return 0, 0

    except ValueError:
        print("Invalid file data format.")
        return 0, 0


if __name__ == "__main__":
    total, average = total_salary("salary_file.txt")

    print(f"Total salary amount: {total}")
    print(f"Average salary: {average}")