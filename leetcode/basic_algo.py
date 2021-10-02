def quick_sort(nums: list) -> list:
    num_leng = len(nums)
    if num_leng < 2:
        return nums
    # ...
    pivot = nums[0]
    left = []
    right = []
    for x in nums[1:]:
        if x < pivot:
            left.append(x)
        else:
            right.append(x)

    return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == '__main__':
    l = [1,2]
    print(l.pop())
    print(quick_sort([2, 1,66,4,55,2,-3,-888,-77,999999]))
