

def twoSum( nums, target):
    """
    https://leetcode.com/problems/two-sum/description/
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    d = {}
    for index, num in enumerate(nums):
        if target - num in d.keys():
            return [d[target-num], index]
        d[num] = index


# nums = [2, 7, 11, 15]
# target = 18
# print(twoSum(nums, target))


def reverse(num):
    """
    :type x: int
    :rtype: int
    """
    #return int(''.join(list(str(x))[::-1]))
    if num < -2147483648 or num > 2147483647:
        return 0
    negativeFlag = False
    if (num < 0):
        negativeFlag = True
        num = -num
    prev_rev_num, rev_num = 0,0
    while (num != 0):
        curr_digit = num % 10
        rev_num = (rev_num * 10) + curr_digit
        if (rev_num - curr_digit) // 10 != prev_rev_num:
            print("WARNING OVERFLOWED!!!\n")
            return 0
        prev_rev_num = rev_num
        num = num // 10

    return -rev_num if negativeFlag else rev_num

#print(reverse(1534236469))

def lengthOfLongestSubstring( s):
    """
    :type s: str
    :rtype: int
    """
    i, ans = 0, 0
    d = dict()
    for j, char in enumerate(s):
        if char in d:
            i = max(d[char], i)
        ans = max(ans, j-i+1) #sliding window
        d[char] = j+1
    return ans


#lengthOfLongestSubstring("abcabcbb")


def hammingDistance(x, y):
    """
    https://leetcode.com/problems/hamming-distance/description/
    :type x: int
    :type y: int
    :rtype: int
    """
    def getBinary(num):
        import collections
        deq = collections.deque()
        while (num > 0):
            deq.appendleft(num % 2)
            num = num // 2
        return deq

    x, y = getBinary(x), getBinary(y)
    length = abs(len(x) - len(y))
    if len(x) > len(y):
        y.extendleft([0] * length)
    else:
        x.extendleft([0] * length)
    distance = 0
    for i, j in zip(x,y):
        if i != j:
            distance +=1
    return distance


#print(hammingDistance(3,5))

def singleNumber(nums):
    """
    https://leetcode.com/problems/single-number/description/
    :type nums: List[int]
    :rtype: int
    """
    #return filter(lambda x: nums.count(x)==1, nums).__next__()
    #return 2*sum(set(nums)) - sum(nums)
    a = 0
    for i in nums:
        a ^= i
    return a

#print(singleNumber([5,2,2]))


def is_one_away(first: str, other: str) -> bool:
    """Given two strings, check if they are one edit away. An edit can be any one of the following.
    1) Inserting a character
    2) Removing a character
    3) Replacing a character"""

    skip_difference = {
        -1: lambda i: (i, i+1),  # Delete
        1: lambda i: (i+1, i),  # Add
        0: lambda i: (i+1, i+1),  # Modify
    }
    try:
        skip = skip_difference[len(first) - len(other)]
    except KeyError:
        return False  # More than 2 letters of difference

    for i, (l1, l2) in enumerate(zip(first, other)):
        if l1 != l2:
            i -= 1  # Go back to the previous couple of identical letters
            break

    # At this point, either there was no differences and we exhausted one word
    # and `i` indicates the last common letter or we found a difference and
    # got back to the last common letter. Skip that common letter and handle
    # the difference properly.
    remain_first, remain_other = skip(i + 1)
    return first[remain_first:] == other[remain_other:]

print(is_one_away('pale', 'ale'))