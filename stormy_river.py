times = [5, 3, 7, 9]
result = 0
min_time = min(times)
times.remove(min_time)

final_time = sum(times) + min_time * (len(times) - 1)

print(final_time)