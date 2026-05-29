from pathlib import Path
import re

README = Path("README.md")
SOLUTIONS = Path("solutions")

def count_files(path):
    if not path.exists():
        return 0
    return sum(1 for f in path.iterdir() if f.is_file())

easy_count = count_files(SOLUTIONS / "easy")
medium_count = count_files(SOLUTIONS / "medium")
hard_count = count_files(SOLUTIONS / "hard")

total_count = easy_count + medium_count + hard_count

content = README.read_text()

content = re.sub(
    r"<!-- EASY_COUNT -->.*?<!-- /EASY_COUNT -->",
    f"<!-- EASY_COUNT -->{easy_count}<!-- /EASY_COUNT -->",
    content,
)

content = re.sub(
    r"<!-- MEDIUM_COUNT -->.*?<!-- /MEDIUM_COUNT -->",
    f"<!-- MEDIUM_COUNT -->{medium_count}<!-- /MEDIUM_COUNT -->",
    content,
)

content = re.sub(
    r"<!-- HARD_COUNT -->.*?<!-- /HARD_COUNT -->",
    f"<!-- HARD_COUNT -->{hard_count}<!-- /HARD_COUNT -->",
    content,
)

content = re.sub(
    r"<!-- TOTAL_COUNT -->.*?<!-- /TOTAL_COUNT -->",
    f"<!-- TOTAL_COUNT -->{total_count}<!-- /TOTAL_COUNT -->",
    content,
)

README.write_text(content)

print(
    f"Updated README: Easy={easy_count}, "
    f"Medium={medium_count}, Hard={hard_count}, "
    f"Total={total_count}"
)