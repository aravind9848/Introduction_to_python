scores = [12,17,9,15,14]
best = -1
best_pos = 0
for pos, score in enumerate(scores):
    if score > best:
        best = score
        best_pos = pos
print(f"Best score is {best} at position {best_pos}")