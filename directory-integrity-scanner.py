import os
import hashlib
import json

BASELINE_FILE ="baseline.json"


print("="*40)
print("DIRECTORY INTEGRITY SCANNER")
print("="*40)

print("1. Create Baseline")
print("2. Verify Directory")
print("3. Exit")

choice = input("Choose your option :")


#Create Baseline
if choice == "1":

    folder=input("Input your folder path :")
    baseline= {}

    try:

        for filename in os.listdir(folder):
            filepath = os.path.join(folder, filename)
            if os.path.isfile(filepath):
                with open(filepath, "rb") as file:
                    data = file.read()

                    file_hash = hashlib.sha256(data).hexdigest()

                    baseline[filename] = file_hash
        with open(BASELINE_FILE, "w") as file:
            json.dump(baseline, file, indent=4)
        print("\nBaseline Created Successfully")
        print("Total Files:", len(baseline))

    except FileNotFoundError:
        print("Folder Not Found")

elif choice == "2":

    folder = input("Input folder path: ")

    try:

        with open(BASELINE_FILE, "r") as file:
            baseline = json.load(file)

        current_files = {}

        for filename in os.listdir(folder):

            filepath = os.path.join(folder, filename)

            if os.path.isfile(filepath):

                with open(filepath, "rb") as file:
                    data = file.read()

                file_hash = hashlib.sha256(data).hexdigest()

                current_files[filename] = file_hash

        print("\nVerification Result")
        print("=" * 40)
        
 # Check Modified & Missing
        for filename in baseline:

            if filename not in current_files:
                print("[MISSING ]", filename)

            elif baseline[filename] != current_files[filename]:
                print("[MODIFIED]", filename)

            else:
                print("[OK      ]", filename)

        # Check New Files
        for filename in current_files:

            if filename not in baseline:
                print("[NEW     ]", filename)

    except FileNotFoundError:
        print("Baseline Not Found. Create baseline first.")

    except Exception as e:
        print("Error:", e)


# EXIT
elif choice == "3":
    print("Exiting Program...")

else:
    print("Invalid Option")