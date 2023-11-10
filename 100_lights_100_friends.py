lights = [False] * 100

for friend in range(1, 101):
    for i in range(friend - 1, 100, friend):
        lights[i] = not lights[i]

count = lights.count(True)

print("Number of all lights are: ", count)
