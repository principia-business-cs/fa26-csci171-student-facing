score = 0
choice = input('Study or sleep? ').strip().lower()
energy = int(input('Energy 1-10: '))
if choice == 'study' and energy >= 5:
    score += 2
elif choice == 'sleep' or energy < 5:
    score += 1
else:
    score -= 1
print('Story score:', score)
