def classify(value):
    if value < 748:
        return "Below range"
    elif value <= 752:
        return "In range"
    else:
        return "Above range"


def calculate_average(total, count):
    return total / count


number_of_tins = int(input("Enter the number of paint tins: "))

total_volume = 0
below_count = 0
in_range_count = 0
above_count = 0

for _ in range(number_of_tins):
    volume = int(input("Enter the paint tin volume: "))
    classification = classify(volume)
    print(classification)

    total_volume += volume

    if classification == "Below range":
        below_count += 1
    elif classification == "In range":
        in_range_count += 1
    else:
        above_count += 1

average_volume = calculate_average(total_volume, number_of_tins)

print(f"Total volume: {total_volume} ml")
print(f"Average volume: {average_volume} ml")
print(f"Below range: {below_count}")
print(f"In range: {in_range_count}")
print(f"Above range: {above_count}")
