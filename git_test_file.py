import subprocess
from collections import Counter
import sys

def get_conflict_files(repo_path):
    try:
        # Run git log to get merge commits
        log_output = subprocess.check_output(
            ['git', '-C', repo_path, 'log', '--merges', '--name-only', '--pretty=format:'],
            text=True
        ).splitlines()

        # Filter out empty lines and count file occurrences
        conflict_files = Counter(filter(None, log_output))
        return conflict_files
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running git log: {e}")
        return Counter()

# Get conflict-prone files and sort by frequency
if len(sys.argv) > 1:
    repo_path = sys.argv[1]
else:
    repo_path = '.'  # Default to current directory

conflicts = get_conflict_files(repo_path)
hotspot_files = sorted(conflicts.items(), key=lambda x: x[1], reverse=True)

# Display results
for file, count in hotspot_files:
    print(f"{file}: {count} conflicts")