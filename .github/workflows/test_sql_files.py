import sys
import sqlfulff
print("Testing files ->", sys.argv)

file = sys.argv[1]
with open(file) as f:
	changed_files = f.read().split()

print(f"Changed files {changed_files}")
sql_files = lsit(filter(lambda x: x.split('.')[-1] == 'sql', changed_files))
print("SQL Files changed ->", sql_files)

for f in sql_files:
	print(f"Parsing {f}")
	with open(f) as fp:
		query = fp.read()
		sqlfulff.parse(query, dialect = 'redshift')

print("Test complete.")