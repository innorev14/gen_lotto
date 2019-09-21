import random

nums=list()

def pattern1():
    while len(nums)<6 :
        num = random.randint(1,45)
        if num not in nums:
            nums.append(num)
    nums.sort()
    print(nums)

def pattern2():
    origin_odd_nums = [ x for x in range(1, 46, 2)]
    origin_even_nums = [ x for x in range(2, 46, 2)]
    odd_num=random.sample(origin_odd_nums, 3)
    even_num=random.sample(origin_even_nums, 3)
    nums = odd_num + even_num
    nums.sort()
    print(nums)

def pattern3():
    origin_odd_nums = [ x for x in range(1, 46, 2)]
    origin_even_nums = [ x for x in range(2, 46, 2)]
    odd_num=random.sample(origin_odd_nums, 4)
    even_num=random.sample(origin_even_nums, 2)
    nums = odd_num + even_num
    nums.sort()
    print(nums)

def pattern4():
    origin_odd_nums = [ x for x in range(1, 46, 2)]
    origin_even_nums = [ x for x in range(2, 46, 2)]
    odd_num=random.sample(origin_odd_nums, 2)
    even_num=random.sample(origin_even_nums, 4)
    nums = odd_num + even_num
    nums.sort()
    print(nums)

pattern1()
pattern2()
pattern2()
pattern3()
pattern4()