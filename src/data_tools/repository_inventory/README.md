# Repository Inventory Tool

Owner: Engine / Backend

Status: local utility

This folder contains the file inventory helper that previously lived at the
repository root. It writes local generated outputs such as `all_files.txt` and
`database_files.txt`, which are ignored by Git.

Run from the repository root:

```bash
python src/data_tools/repository_inventory/find_files.py . --all-output all_files.txt --db-output database_files.txt
```
