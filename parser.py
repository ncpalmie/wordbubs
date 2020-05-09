import re

wiki_colors = open('wiki_colorlist.txt', 'r')
out_lines = []

for line in wiki_colors.readlines():
    new_line = ""
    left_par = line.find('(')
    right_par = line.find(')')
    if left_par != -1 and right_par != -1:
        line = line[0:left_par] + line[right_par+2:]
    words = re.split('	| ', line)
    for word in words:
        if not word[0] in '(#':
            new_line += word + ' '
        elif word[0] == '#' and len(word) == 7:
            new_line += word
            break
    if new_line != "":
        out_lines.append(new_line)
wiki_colors.close()

wiki_colors = open('wiki_colorlist.txt', 'w')
for line in out_lines:
    wiki_colors.write(line + '\n')
wiki_colors.close()
