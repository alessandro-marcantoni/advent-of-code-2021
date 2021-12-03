import statistics

def choose(list, pivot, i = 0):
    while len(list) > 1:
        common = statistics.multimode([b[i] for b in list])
        common = pivot(common)
        list = [b for b in list if b[i] == common]
        i += 1
    return list[0]

file = open('03-binary-diagnostic-input.txt', 'r')
binaries = [b.strip() for b in file.readlines()]

gamma_rate = epsilon_rate = ""
for i in range(len(binaries[0])):
    gamma_rate += statistics.mode([b[i] for b in binaries])
    epsilon_rate += '0' if statistics.mode([b[i] for b in binaries]) == '1' else '1'

print(int(gamma_rate, 2) * int(epsilon_rate, 2))

oxigen = choose(binaries, lambda common : '1' if len(common) > 1 else common[0])
co2 = choose(binaries, lambda common : '0' if len(common) > 1 else ('0' if common[0] == '1' else '1'))

print(int(oxigen, 2) * int(co2, 2))