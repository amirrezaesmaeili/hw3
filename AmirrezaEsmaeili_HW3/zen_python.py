# Dictionary of English number words and their numerical equivalents
NUMBER_WORDS = {
    'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6',
    'seven': '7', 'eight': '8', 'nine': '9', 'ten': '10', 'eleven': '11', 'twelve': '12',
    'thirteen': '13', 'fourteen': '14', 'fifteen': '15', 'sixteen': '16', 'seventeen': '17',
    'eighteen': '18', 'nineteen': '19', 'twenty': '20'
}

# Open input and output files
with open('zen.txt') as input_file, open('new_zen.txt', 'w') as output_file:
    # Read input file line by line
    for line in input_file:
        # Split line into words and search for numerical equivalents
        words = line.strip().split()
        for i in range(len(words)):
            if words[i] in NUMBER_WORDS:
                # Replace word with numerical equivalent in output file
                words[i] = NUMBER_WORDS[words[i]]
        # Write modified line to output file
        output_file.write(' '.join(words) + '\n')
input_file.close()
output_file.close()
