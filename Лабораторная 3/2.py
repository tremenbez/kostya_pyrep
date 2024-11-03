def find_common_participants(x,y,delimiter = ","):
    a = set(x.split(delimiter))
    b = y.split(delimiter)
    return sorted(a.intersection(b))

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group,"|"))
