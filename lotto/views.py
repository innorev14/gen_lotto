from django.shortcuts import render
import random

from .models import Winnum


def gen_lotto(num):
    nums = list()

    def pattern1():
        while len(nums) < 6:
            num = random.randint(1, 45)
            if num not in nums:
                nums.append(num)
        nums.sort()
        return nums

    def pattern2():
        origin_odd_nums = [x for x in range(1, 46, 2)]
        origin_even_nums = [x for x in range(2, 46, 2)]
        odd_num = random.sample(origin_odd_nums, 3)
        even_num = random.sample(origin_even_nums, 3)
        nums = odd_num + even_num
        nums.sort()
        return nums

    def pattern3():
        origin_odd_nums = [x for x in range(1, 46, 2)]
        origin_even_nums = [x for x in range(2, 46, 2)]
        odd_num = random.sample(origin_odd_nums, 4)
        even_num = random.sample(origin_even_nums, 2)
        nums = odd_num + even_num
        nums.sort()
        return nums

    def pattern4():
        origin_odd_nums = [x for x in range(1, 46, 2)]
        origin_even_nums = [x for x in range(2, 46, 2)]
        odd_num = random.sample(origin_odd_nums, 2)
        even_num = random.sample(origin_even_nums, 4)
        nums = odd_num + even_num
        nums.sort()
        return nums

    if num == 1:
        pattern1()
    elif num == 2:
        pattern2()
    elif num == 3:
        pattern3()
    elif num == 4:
        pattern4()

def mylotto(request):
    pass

def winnum_list(request):
    qs = Winnum.objects.all()

    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(title__icontains=q)

    return render(request, 'lotto/winnum_list.html', {
        'winnum_list': qs,
        'q':q,
    })