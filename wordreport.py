with open("text.txt", encoding="utf-8") as f:
    text = f.read().lower()
    for p in ".,!?;":
        text = text.replace(p, "")
words = text.split()
    
counts = {}
for w in words:
    counts[w]= counts.get(w, 0) + 1
    
with open("report.txt", "w", encoding="utf-8") as out:
    print(out)
    out.write(f"words: {len(words)}\n")
    out.write(f"unique: {len(counts)}\n")
    
    for w in sorted(counts):
        out.write(f"{w:<10}{counts[w]}\n")
print("Report saved")
    