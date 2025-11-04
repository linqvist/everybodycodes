
def load_file(filename):
    result = []
    with open(f"files/{filename}.txt") as f:
        rows = f.read().splitlines()
    for row in rows:
        if row:
            result.append(row)
    return result