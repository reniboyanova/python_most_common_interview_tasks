def toh(n, start, end, aux):
    if n == 1:
        print(f"Move disk 1 from {start} to {end}")
        end.append(start.pop())
        return
    toh(n - 1, start, aux, end)
    print(f"Move disk {n} from {start} to {end}")
    end.append(start.pop())
    toh(n - 1, aux, end, start)

"""
# Функция, която премества дискове от началния лист към крайния лист, използвайки временния лист
def toh(n, начален, крайен, временен):
    if n == 1:
        # Ако имаме само един диск, просто го преместваме от началния към крайния лист
        Премести един диск от началния лист към крайния лист
    else:
        # Иначе, използваме рекурсия
        # 1. Пренасяме (n-1) диска от началния към временния лист, използвайки крайния като временен
        toh(n-1, начален, временен, крайен)
        # 2. Пренасяме останалия единичен диск от началния към крайния лист
        Премести един диск от началния лист към крайния лист
        # 3. Пренасяме (n-1) диска от временния към крайния лист, използвайки началния като временен
        toh(n-1, временен, крайен, начален)

# Използваме списъци, за да представим три листа (A, B, C)
list_A = [3, 2, 1]  # Лист А с дисковете в началото
list_B = []  # Празен лист B
list_C = []  # Празен лист C

n = len(list_A)  # Брой на дисковете

# Извикваме функцията за Кулите на Ханой
toh(n, list_A, list_C, list_B)
""" 

if __name__ == "__main__":
    # Използваме списъци, за да представим листите (A, B, C)
    list_A = [5, 4, 3, 2, 1]  # Списъкът А съдържа дисковете в началото (по-големите дискове вдясно)
    list_B = []  # Празен списък B
    list_C = []  # Празен списък C

    n = len(list_A)  # Брой дискове

    # Извикваме функцията за Кулите на Ханой
    toh(n, list_A, list_C, list_B)

    print("List A (source):", list_A)
    print("List B (auxiliary):", list_B)
    print("List C (destination):", list_C)