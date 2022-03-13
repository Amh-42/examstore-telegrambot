from mongodb2 import _Exams as exam


def dict_updater(current, batch, code, file):
    if batch == "fresh":
        new_data = file
        exam[current[0]][current[1]][current[2]][current[3]][code] = file
    elif batch == "2nd_1st":
        new_data = file
        exam[current[0]][current[1]][current[2]
                                     ][current[3]][current[4]][code] = file
    else:
        new_data = file
        exam[current[0]][current[1]][current[2]
                                     ][current[3]][current[4]][current[5]][current[6]][code] = file
    return exam
