import os

a = os.listdir()
dict = {}
for i in a:
    if '.txt' in i:
        with open(i, encoding='utf-8') as read_list:
            dict[i] = read_list.readlines()          
with open('new_file.txt', 'w', encoding='utf-8') as new_file:
    sorted_list = sorted(dict.values(), key=lambda x: len(x), reverse=False)
    id = 0
    for line in sorted_list:
        for key, value in dict.items():       
            if value == line:
                new_file.write(key)
                new_file.write('\n')
                new_file.write(str(len(line)))
                new_file.write('\n')
                for id, n in enumerate(line):                                  
                    id += 1                                                                      
                    new_file.write(f'Строка номер {id} файла номер {list(key)[0]}')
                    new_file.write('\n')
