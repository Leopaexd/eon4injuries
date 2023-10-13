# author: Oliver Glant
# email: oliver.glant@gmail.com
# Eon IV injury tables


class Skadetabell:
    table = {}
    content_list = []

    def __init__(self):
        with open(r'skadetabell.txt', 'r') as file:
            current_table = []
            nameflag = True
            for line in file.readlines():
                if line.strip() == 'XXX':
                    nameflag = True  # True om nästa rad är namnet på tabellen
                    table_name = current_table[0].strip()
                    self.content_list.append(table_name)
                    table_contents = current_table[0:]
                    self.table[table_name] = table_contents
                    current_table = []
                elif line[0].isdigit() or nameflag:
                    current_table.append(line)
                    nameflag = False
                else:
                    current_table[-1] = current_table[-1] + ' ' + line
