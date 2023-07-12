import os
import sys
import csv

def make_changes(data, changes):
    for change in changes:
        X, Y, value = map(str.strip, change.split(","))
        X = int(X)
        Y = int(Y)
        data[Y][X] = value

def display_data(data):
    for data in data:
        print(",".join(data))

def save_csv(data, dst):
    with open(dst, 'w', newline="") as f:
        writer = csv.writer(f)
        writer.writerow(data)

def read_csv(src):
    check_file = os.path.exists(src)

    if check_file:
        with open(src, newline="") as f:
            reader = csv.reader(f)
            data = list(reader)
            return data
    else:
        print(f"Error: {src} not found")
        sys.exit(1)

def main():
    if len(sys.argv) < 4:
        print("The script should be run as: reader.py <src> <dst> <change1> <chnage2> ... ")
        sys.exit(1)

    src = sys.argv[1]
    dst = sys.argv[2]
    changes = sys.argv[3:]

    in_data = read_csv(src)
    make_changes(in_data, changes)
    display_data(in_data)
    save_csv(in_data, dst)

if __name__ == "__main__":
    main()


