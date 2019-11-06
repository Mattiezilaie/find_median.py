# Author: Mahtab Zilaie
# Date: November 6 2019
# Description: using a function to find a median


def find_median(nums_list):
    nums_list.sort()
    if (len(nums_list) % 2 ==1):
        return nums_list[len(nums_list)//2]
    else:
        return (nums_list[len(nums_list)//2-1] + nums_list[len(nums_list)//2])/2