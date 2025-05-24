# Define timetable as a dictionary
timetable = {
    'Monday':    ['Math', 'Physics', 'Chemistry', 'Break', 'English'],
    'Tuesday':   ['Biology', 'Math', 'History', 'Break', 'PE'],
    'Wednesday': ['English', 'Computer', 'Math', 'Break', 'Physics'],
    'Thursday':  ['Chemistry', 'Biology', 'Math', 'Break', 'History'],
    'Friday':    ['PE', 'English', 'Computer', 'Break', 'Math'],
}

# Define time slots
time_slots = ['9:00-10:00', '10:00-11:00', '11:00-12:00', '12:00-12:30', '12:30-1:30']

# Print header
print("{:<10}".format("Day"), end='')
for slot in time_slots:
    print("{:<15}".format(slot), end='')
print()

print("-" * (10 + 15 * len(time_slots)))

# Print timetable
for day, sessions in timetable.items():
    print("{:<10}".format(day), end='')
    for subject in sessions:
        print("{:<15}".format(subject), end='')
    print() 