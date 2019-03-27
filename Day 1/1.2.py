import cProfile, pstats, io



def profile(fnc):
    
    """A decorator that uses cProfile to profile a function"""
    
    def inner(*args, **kwargs):
        
        pr = cProfile.Profile()
        pr.enable()
        retval = fnc(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval

    return inner

def read_file():
    with open('input.txt') as my_file:
        read_data = my_file.read()
        return read_data.splitlines() #split by line

#---------------Preoptimization - runtime: 162.18 Secs--------------
# @profile
# def main():
#     print("Calculating Checksum...")
#     nums = read_file()
#     past = [0]
#     current = 0
#     index = 0
#     run = True
#     accum = 0
#     while run:
#         if index >= len(nums):
#             index = 0
#         else:
#             current += int(nums[index])
#             past.append(current)
#             run = past.count(current) < 2
#             index += 1
#         accum += 1
#     print(current)
#     print(accum)
#     #print(past)


#---------------Post optimization - Runtime: .122 seconds---------------
@profile
def main():
    numStr = read_file()
    nums   = []             #number as ints from input.txt
    for num in numStr:
      nums.append(int(num)) #convert to ints, for speed in comparison later
    past    = {0}           #previous state values
    current = 0
    index   = 0
    run     = True
    length  = len(nums)
    while run:
        if index >= length:
            index = 0
        else:
            current += nums[index]
            if current in past:
              run = False
            past.add(current)
            index += 1
    return current

print("Calculating First Repeat...")
print("First Repeat:", main())