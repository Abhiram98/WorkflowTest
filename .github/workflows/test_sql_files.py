import sys
import sqlfluff
print("Testing files ->", sys.argv)

file = sys.argv[1]
print(f"Content File {file}")
with open(file) as f:
	changed_files = f.read().split()

print(f"Changed files {changed_files}")
sql_files = list(filter(lambda x: x.split('.')[-1] == 'sql', changed_files))
print("SQL Files changed ->", sql_files)

for f in sql_files:
	print(f"Parsing {f}")
	with open(f) as fp:
		query = fp.read()
		try:
			sqlfluff.parse(query, dialect = 'redshift')
		except Exception as e:
			print(f"Failed to parse {f}")
			print(f"error: {str(e)}")

print("Test complete.")