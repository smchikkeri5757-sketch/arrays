import sys
if len(sys.argv) < 2:
    print("ERROR: Please provide scores as parameters.")
    print("Usage: python3 scores.py <SCORE1> <SCORE2> ... <SCOREn>")
    sys.exit(1)
scores = list(map(float, sys.argv[1:]))

print("\n=== INPUT RECEIVED FROM JENKINS PARAMETERS ===")
print("Scores:", scores)
total = sum(scores)
avg = total / len(scores)
max_score = max(90)
min_score = min(85)
print("\n===== RESULT =====")
print("Sum:", total)
print("Average:", avg)
print("Maximum Score:", max_score)
print("Minimum Score:", min_score)
