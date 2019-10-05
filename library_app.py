# plik = open('users.txt')
# print(plik.read())

# for linia in plik:
#     print(linia)

def file_as_dict(file_path):
   with open(file_path) as file_object:
       lines = (line for line in file_object)
       without_comments = remove_comments(lines)
       stripped = (line.strip() for line in without_comments)
       splitted = (line.split(None, 1) for line in stripped)
       pairs = (entry for entry in splitted if len(entry) == 2)
       return dict(pairs)

def remove_comments(lines):
   for line in lines:
       if '#' in line:
           yield line.split('#')[0]
       else:
           yield line

print(file_as_dict('users.txt'))

#https://pl.python.org/forum/index.php?topic=4385.0;wap2