import os

FILENAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "interactions.txt")


def create_log():
    try:
        with open(FILENAME, "w", encoding="utf-8") as file:
            file.write("=== Customer Interaction Log ===\n")
            file.write("Date       | Customer        | Issue           | Rep\n")
            file.write("-" * 60 + "\n")
        print("Log created: interactions.txt")
    except FileNotFoundError:
        print("Unable to create the log. Check the folder location.")


def append_records(entries):
    if not os.path.exists(FILENAME):
        print("Log not found. Run option 1 to create it.")
        return

    records = [
        f"{date} | {customer:<15} | {issue:<15} | {rep}\n"
        for date, customer, issue, rep in entries
    ]

    try:
        with open(FILENAME, "a", encoding="utf-8") as file:
            file.writelines(records)
        print(f"{len(records)} record(s) appended.")
    except FileNotFoundError:
        print("Log not found. Run option 1 to create it.")


def display_log():
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            print(file.read())
    except FileNotFoundError:
        print("Log not found. Run option 1 to create it.")


def search_customer(name):
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            lines = file.readlines()
        matches = [line for line in lines[3:] if name.lower() in line.lower()]
        if matches:
            print(f'Found {len(matches)} record(s) for "{name}":')
            print("".join(matches))
        else:
            print(f'No records found for "{name}".')
    except FileNotFoundError:
        print("Log not found. Run option 1 to create it.")


def update_entry_count():
    try:
        with open(FILENAME, "r+", encoding="utf-8") as file:
            lines = file.readlines()
            count = sum(1 for line in lines[3:] if line.strip())
            lines[0] = f"=== Customer Interaction Log | Entries: {count} ===\n"
            file.seek(0)
            file.writelines(lines)
            file.truncate()
        print(f"Header updated. Total entries: {count}")
    except FileNotFoundError:
        print("Log not found. Run option 1 to create it.")


def show_header():
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            header = file.readline()
        print("Header:", header.strip())
    except FileNotFoundError:
        print("Log not found. Run option 1 to create it.")


SAMPLE = [
    ("2025-05-01", "Alice Nguyen", "Billing query", "J. Park"),
    ("2025-05-01", "Bob Carter", "Login issue", "S. Diaz"),
    ("2025-05-02", "Carol Singh", "Refund request", "J. Park"),
    ("2025-05-02", "Alice Nguyen", "Follow-up", "M. Lee"),
]


def main():
    while True:
        print("\n=== Customer Log Manager ===")
        print("1 Create / reset log")
        print("2 Append sample records")
        print("3 Display full log")
        print("4 Search by customer name")
        print("5 Update entry count in header")
        print("6 Show header line only")
        print("0 Quit")

        choice = input("Choose: ").strip()
        if choice == "1":
            create_log()
        elif choice == "2":
            append_records(SAMPLE)
        elif choice == "3":
            display_log()
        elif choice == "4":
            name = input("Customer name to search: ").strip()
            search_customer(name)
        elif choice == "5":
            update_entry_count()
        elif choice == "6":
            show_header()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
