def towers_of_hanoi(n, start, end, aux):
    if n == 1:
        print(f"Move disk 1 from {start} to {end}")
        end.append(start.pop())
        return
    towers_of_hanoi(n - 1, start, aux, end)
    print(f"Move disk {n} from {start} to {end}")
    end.append(start.pop())
    towers_of_hanoi(n - 1, aux, end, start)


if __name__ == "__main__":
    list_A = [5, 4, 3, 2, 1]  
    list_B = []  
    list_C = []  

    n = len(list_A)  

    towers_of_hanoi(n, list_A, list_C, list_B)

    print("List A (source):", list_A)
    print("List B (auxiliary):", list_B)
    print("List C (destination):", list_C)