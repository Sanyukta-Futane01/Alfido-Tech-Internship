import os
import csv
import shutil

# -------------------------------
# FUNCTION: Read CSV File
# -------------------------------
def read_csv(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            print("Reading CSV File:\n")
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("Error: File not found!")
    except Exception as e:
        print("Error occurred:", e)


# -------------------------------
# FUNCTION: Write to CSV File
# -------------------------------
def write_csv(file_path):
    try:
        # Adding new student data
        new_data = ["5", "Kiran", "20", "92"]

        with open(file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(new_data)

        print("\nNew data added successfully!")

    except Exception as e:
        print("Error while writing:", e)


# -------------------------------
# FUNCTION: Rename File
# -------------------------------
def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print("\nFile renamed successfully!")
    except FileNotFoundError:
        print("Error: File not found!")
    except Exception as e:
        print("Error:", e)


# -------------------------------
# FUNCTION: Move File
# -------------------------------
def move_file(source, destination):
    try:
        shutil.move(source, destination)
        print("\nFile moved successfully!")
    except FileNotFoundError:
        print("Error: File not found!")
    except Exception as e:
        print("Error:", e)


# -------------------------------
# FUNCTION: Delete File
# -------------------------------
def delete_file(file_path):
    try:
        os.remove(file_path)
        print("\nFile deleted successfully!")
    except FileNotFoundError:
        print("Error: File not found!")
    except Exception as e:
        print("Error:", e)


# -------------------------------
# MAIN PROGRAM
# -------------------------------
if __name__ == "__main__":

    file_name = "students.csv"

    # 1. Read CSV
    read_csv(file_name)

    # 2. Write CSV
    write_csv(file_name)

    # 3. Rename File
    rename_file("students.csv", "students_updated.csv")

    # 4. Move File (make sure folder exists)
    os.makedirs("backup", exist_ok=True)
    move_file("students_updated.csv", "backup/students_updated.csv")

    # # 5. Delete File
    delete_file("backup/students_updated.csv")