def nextIsBiggerNumber(list):
    return sum(
        [1 if list[i] > list[i-1] 
            else 0 
            for i in range(1, len(list))]
    )

file = open('01-sonar-sweep-input.txt', 'r')
measurements = [int(m.strip()) for m in file.readlines()]
print(nextIsBiggerNumber(measurements))

sums = [
    measurements[i] +
    measurements[i-1] +
    measurements[i-2] for i in range(2, len(measurements))
]
print(nextIsBiggerNumber(sums))