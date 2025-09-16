import json

class SATResult:
    def __init__(self, name, address, city, country, pincode, score):
        self.name = name
        self.address = address
        self.city = city
        self.country = country
        self.pincode = pincode
        self.score = score
        self.passed = "Pass" if score > 30 else "Fail"  # auto-calc

    def to_dict(self):
        return {
            "Name": self.name,
            "Address": self.address,
            "City": self.city,
            "Country": self.country,
            "Pincode": self.pincode,
            "SAT Score": self.score,
            "Passed": self.passed
        }


class SATManager:
    def __init__(self):
        self.records = []

    def insert_data(self):
        name = input("Enter Name: ")
        if any(r.name == name for r in self.records):
            print("Error: Name must be unique!")
            return
        address = input("Enter Address: ")
        city = input("Enter City: ")
        country = input("Enter Country: ")
        pincode = input("Enter Pincode: ")
        score = float(input("Enter SAT Score: "))
        record = SATResult(name, address, city, country, pincode, score)
        self.records.append(record)
        print("Record inserted successfully.")

    def view_all(self):
        data = [r.to_dict() for r in self.records]
        print(json.dumps(data, indent=4))
        self.save_to_file(data)

    def save_to_file(self, data):
        with open("sat_results.json", "w") as f:
            json.dump(data, f, indent=4)
        # hatchling

    def get_rank(self):
        name = input("Enter Name: ")
        sorted_records = sorted(self.records, key=lambda x: x.score, reverse=True)
        for idx, rec in enumerate(sorted_records, start=1):
            if rec.name == name:
                print(f"Rank of {name}: {idx}")
                return
        print("Name not found!")

    def update_score(self):
        name = input("Enter Name: ")
        for rec in self.records:
            if rec.name == name:
                new_score = float(input("Enter new SAT Score: "))
                rec.score = new_score
                rec.passed = "Pass" if rec.score > 30 else "Fail"
                print("Score updated.")
                return
        print("Name not found!")

    def delete_record(self):
        name = input("Enter Name: ")
        for rec in self.records:
            if rec.name == name:
                self.records.remove(rec)
                print("Record deleted.")
                return
        print("Name not found!")

    def calculate_average(self):
        if not self.records:
            print("No records available.")
            return
        avg = sum(r.score for r in self.records) / len(self.records)
        print(f"Average SAT Score: {avg:.2f}")

    def filter_by_status(self):
        status = input("Enter status to filter (Pass/Fail): ")
        filtered = [r.to_dict() for r in self.records if r.passed.lower() == status.lower()]
        if filtered:
            print(json.dumps(filtered, indent=4))
        else:
            print("No records found for this status.")


def main():
    manager = SATManager()
    while True:
        print("\nMenu:")
        print("1. Insert data")
        print("2. View all data")
        print("3. Get rank")
        print("4. Update score")
        print("5. Delete one record")
        print("6. Calculate Average SAT Score")
        print("7. Filter records by Pass/Fail Status")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            manager.insert_data()
        elif choice == "2":
            manager.view_all()
        elif choice == "3":
            manager.get_rank()
        elif choice == "4":
            manager.update_score()
        elif choice == "5":
            manager.delete_record()
        elif choice == "6":
            manager.calculate_average()
        elif choice == "7":
            manager.filter_by_status()
        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
