box1 = False
box2 = True
box3 = False
boxes = [box1, box2, box3]

for box in range(len(boxes)):
    if boxes[box] is True:
        print(f"Box with number {box + 1} is with TRUE condition!")

# За всички възможни комбинации на изявленията на кутиите
for box1 in [True, False]:
    for box2 in [True, False]:
        for box3 in [True, False]:
            # Ако точно едно изявление е вярно
            if (box1 + box2 + box3) == 1:
                # Проверяваме изявленията
                if (box1 and not box2 and not box3) or (not box1 and box2 and not box3) or (
                        not box1 and not box2 and box3):
                    print(f"Valid solution found: Box-1: {box1}, Box-2: {box2}, Box-3: {box3}")
