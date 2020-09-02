import subprocess, sys, random, re

file_path = sys.argv[1]
chance = sys.argv[2]
file = open(file_path, "r")
blank_text_file = open("blank_text.md", "w")
solutions_file = open("solutions.md", "w")
content = file.readlines()
blank_counter = 0

for line in content:
	blank_text_words = line.split(" ")
	solution_words = line.split(" ")
	for i, word in enumerate(blank_text_words):
		if random.randint(1, int(chance)) == 1:
			if len(word) > 6 and re.match("^[a-zA-Z0-9_]*$", word):
				blank_text = ""
				solution_text = ""
				optional_newline = ""
				newline_character_length = 0
				if "\n" in word:
					optional_newline = "\n"
					newline_character_length = 1
				for j, char in enumerate(word):
					blank_text += "_ "
					solution_text += "**" + char + "** "
				count_element = (
					" {"
					+ str(j + 1 - newline_character_length)
					+ "}"
					+ optional_newline
				)
				blank_text += count_element
				solution_text += count_element
				blank_text_words[i] = blank_text
				solution_words[i] = solution_text
				blank_counter += 1
	blank_text_file.write(" ".join(blank_text_words))
	solutions_file.write(" ".join(solution_words))
print("You have created a file with: "+str(blank_counter)+" blanks.")
