import sys
with open("input_day5.dat") as file:
    input_list = file.read().splitlines()
input_list = [int(i) for i in input_list]
step_counter = 0
index = 0
def rec_listjumping():
    global index
    global step_counter
    tmp_index = index
    try:
        index += input_list[index]
        input_list[tmp_index] += 1
        step_counter = step_counter + 1
        rec_listjumping()
    except UnboundLocalError:
        return (None)
    except:
        print(f"{step_counter}",end='',flush=True)

rec_listjumping()
print('Stuff')
rec_listjumping()
print("End")
rec_listjumping()
for i in range(10):
    rec_listjumping()