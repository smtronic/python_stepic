# Информация об учебных курсах
# Напишите программу, которая по номеру курса выводит информацию о данном курсе.

# Номер курса (ключ)	Номер аудитории (значение)	Преподаватель (значение)	Время (значение)
# CS101	3004	Хайнс	8:00
# CS102	4501	Альварадо	9:00
# CS103	6755	Рич	10:00
# NT110	1244	Берк	11:00
# CM241	1411	Ли	13:00
# Формат входных данных
# На вход программе подается одна строка – номер курса.

# Формат выходных данных
# Программа должна вывести номер курса, затем номер аудитории, имя преподавателя и время проведения курса в соответствии с примерами.

curs_dict = {'CS101': {'audience_number': '3004', 'teacher': 'Хайнс', 'time': '8:00'},
'CS102': {'audience_number': '4501', 'teacher': 'Альварадо', 'time': '9:00'},
'CS103': {'audience_number': '6755', 'teacher': 'Рич', 'time': '10:00'},
'NT110': {'audience_number': '1244', 'teacher': 'Берк', 'time': '11:00'},
'CM241': {'audience_number': '1411', 'teacher': 'Ли', 'time': '13:00'}}
curs_num = input()
print("{}: {}, {}, {}".format(curs_num, *curs_dict[curs_num].values()))