import os

filename = "demo.txt"

if not os.path.exists(filename):
    with open(filename, "w") as file:
        file.write("""i am writing a demo file.
Hello, how are you today?
my name is bimal choudhury
I hope you are doing well.
Let's count the lines, words, and letters.
Starting sentences with the same letter seems sensible sometimes.
sentences are in how many numbers.
""")

total_lines = 0
total_words = 0
total_letters = 0
lines_starting_with_s = 0

with open(filename, "r") as file:
    for line in file:
        total_lines += 1
        total_words += len(line.split())
        total_letters += len(line.replace(" ", "").replace("\n", ""))
        if line.strip().lower().startswith("i"):
            lines_starting_with_s += 1

print("Total number of lines:", total_lines)
print("Total number of words:", total_words)
print("Total number of letters:", total_letters)
print("Number of lines starting with 'i':", lines_starting_with_s)
