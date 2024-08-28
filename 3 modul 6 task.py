# Дополнительное практическое задание по модулю*

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

sum_number = 0
sum_len_strange = 0


def search_type(index):
  global sum_number, sum_len_strange
  for i in range(0, len(index), 1):
    if type(index[i]) == int:
      sum_number += index[i]
    elif type(index[i]) == str:
      sum_len_strange += len(index[i])
    else:
      if type(index[i]) == tuple or type(index[i]) == set:
        index[i] = list(index[i])
      if type(index[i]) == dict:
        index[i] = list(index[i].items())
      search_type(index[i])
  # Для проверки
  # print(sum_number)
  # print(sum_len_strange)


search_type(data_structure)
print('Сумма всех чисел и длин всех строк равна:', sum_number + sum_len_strange)