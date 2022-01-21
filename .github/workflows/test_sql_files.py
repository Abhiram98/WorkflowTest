import sys
print("Testing files ->", sys.argv)

files_changes = sys.argv
sql_files = list(filter(lambda x: x.split('.')[-1] == 'sql', files_changes))
print("SQL Files changed ->", sql_files)

print("Test complete.")