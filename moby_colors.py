import string

def book_to_wordlist(book_filename): 
    wordlist = []
    book_file = open(book_filename, 'r')

    for line in book_file.readlines():
        words = line.split(' ')
        for word in words:
            book_punc = string.punctuation + '’“”—'
            pword = word.translate(str.maketrans('', '', book_punc)).lower()
            wordlist.append(pword)

    book_file.close()
    return wordlist

def create_color_dict():
    color_dict = {}
    color_file = open('wiki_colorlist.txt', 'r')
    
    for color in color_file.readlines():
        col_tuple = color.split(' #')
        col = col_tuple[0].translate(str.maketrans('', '', string.punctuation)).lower()
        color_dict[col_tuple[0].lower()] = '#' + col_tuple[1][0:-1]
    
    return color_dict

def color_analysis(color_dict, wordlist):
    output = ""
    
    for word in wordlist:
        if word in color_dict:
            output += word + '\n'

    return ('colors_', output)

color_dict = None
wordlist = None
opts_str = 'Choose from these options:\n\
     \'c\' for color analysis\n\
     \'q\' to exit'

print('Enter name of text file to analyze: ')
book_filename = input()

wordlist = book_to_wordlist(book_filename)

print(opts_str)
usr_input = input()
while usr_input.lower() != 'q':
    print(opts_str)
    
    if (usr_input == 'c'):
        if color_dict == None:
            color_dict = create_color_dict()    
        output = color_analysis(color_dict, wordlist)

    out_file = open(output[0] + book_filename, 'w')
    out_file.write(output[1])
    out_file.close()
    print(output[0] + book_filename + ' file created.')

    usr_input = input()

print('Goodbye.')
        

