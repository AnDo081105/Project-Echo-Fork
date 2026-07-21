import os
import argparse
from pathlib import Path

def find_files_and_databases(root_path):
    all_files = []
    database_files = []

    # Walk through all directories and files
    for root, dirs, files in os.walk(root_path):
        for file in files:
            full_path = os.path.join(root, file)
            all_files.append(full_path)
            if file.endswith('.db'):
                database_files.append(full_path)

    return all_files, database_files

def write_lines(path, lines):
    Path(path).write_text("\n".join(lines), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Create a simple repository file inventory.")
    parser.add_argument("root", nargs="?", default=".", help="Repository or folder to scan.")
    parser.add_argument("--all-output", default="all_files.txt", help="Path for the full file list.")
    parser.add_argument("--db-output", default="database_files.txt", help="Path for database file matches.")
    args = parser.parse_args()

    project_path = Path(args.root).resolve()
    all_files, db_files = find_files_and_databases(project_path)

    write_lines(args.all_output, all_files)
    write_lines(args.db_output, db_files)

    print(f"Found {len(all_files)} files in total.")
    print(f"Found {len(db_files)} database files.")
    print(f"Results saved to '{args.all_output}' and '{args.db_output}'.")


if __name__ == "__main__":
    main()
