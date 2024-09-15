from sys import argv

if len(argv) < 2:
    print("Please provdie the file name")
else:
    file = open(argv[1])
    lines = file.read()
    lines = lines.split('\n')
    line_count = len(lines)
    word_count = 0
    letter_count = 0

for line in lines:
    word = line.split()
    word_count += len(word)
    letter_count += len(line)


print(f'The line count is {line_count}.')
print(f'The word count is {word_count}.')
print(f'The letter count is {letter_count}.')
