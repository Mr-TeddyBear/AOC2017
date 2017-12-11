import re
with open("input_day2.dat") as file:
    lines = file.readlines()
    rows_input = []
    for i in lines:
        i = i.split("\t")
        i[-1] = re.sub(r'\n',r'',i[-1])
        i = [int(a) for a in i]
        rows_input.append(i)
chechsum = 0
for rows in rows_input:
    chechsum += (max(rows)-min(rows))
print(chechsum)