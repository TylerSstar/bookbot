from stats import num_words, count_char, sort_dict
import sys

if len(sys.argv) == 1:
	print('Usage: python3 main.py <path_to_book>')
	sys.exit(1)

def get_book_text(f_path):
	with open(f_path) as f:
		f_c= f.read()
	return f_c

f_c = get_book_text(sys.argv[1])

num_words(f_c)

chars_dict = count_char(f_c)

chars_dict_list  = sort_dict(chars_dict)

print('============ BOOKBOT ============')
print(f'Analyzing book found at {sys.argv[1]}...')
print('----------- Word Count ----------')
print(f"Found {num_words} total words")
print('--------- Character Count -------')
for i in chars_dict_list:
	if i['char'].isalpha():
		print(f"{i['char']}: {i['num']}")
print('============= END ===============')
