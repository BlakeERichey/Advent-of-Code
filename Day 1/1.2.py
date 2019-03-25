def read_file():
    with open('input.txt') as my_file:
        read_data = my_file.read()
        return read_data.splitlines() #split by line

def main():
    nums = read_file()
    past = [0]
    current = 0
    index = 0
    run = True
    accum = 0
    while run:
        if index >= len(nums):
            index = 0
        else:
            current += int(nums[index])
            past.append(current)
            run = past.count(current) < 2
            index += 1
        accum += 1
    print(current)
    print(accum)
    #print(past)

main()
