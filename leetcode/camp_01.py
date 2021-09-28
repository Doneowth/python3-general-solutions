import heapq
from typing import Optional

from leetcode.ListNode import ListNode


class Solution:
    # string or list walk through,
    # 1. slide window (hashset included)
    # 2. double pointer
    def q3_lengthOfLongestSubstring(self, s: str) -> int:
        win_length = 1
        cursor = 0
        max_len = 0
        max_substr = ''
        str_len = len(s)

        while (cursor + win_length <= str_len):

            if (self.is_uniq_str(s[cursor:cursor + win_length])):
                max_len = max(max_len, len(s[cursor:cursor + win_length]))
                max_substr = s[cursor:cursor + win_length]
                win_length += 1
            else:
                cursor += 1

        print(max_substr)
        return max_len

    def is_uniq_str(self, s):
        uniq_c_set = set(c for c in s)
        if len(uniq_c_set) == len(s):
            return True
        else:
            return False

    def q4_findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged_list = nums1 + nums2
        merged_list.sort()
        l = len(merged_list)

        if l % 2 == 0:
            left = merged_list[int(l / 2)]
            right = merged_list[int(l / 2) - 1]
            return (left + right) / 2
        else:
            return merged_list[(l / 2).__floor__()]

    # https://leetcode.com/problems/longest-palindromic-substring/
    # wrong solution
    def q5_longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            raise Exception('input length is 0')
        if len(s) == 1:
            return s
        d = dict()
        for i in range(len(s)):
            count = i + 1
            while count < len(s) and s[i] != s[count]:
                count += 1
            if self.is_palindorme(s[i:count + 1]):
                if d.get(s[i:count + 1]) is None:
                    d[s[i:count + 1]] = [i, count]
                else:
                    if i - d.get(s[i:count + 1])[1] < 3:
                        d[s[d.get(s[i:count + 1])[0]: count + 1]] = [d.get(s[i:count + 1])[0], count]
        print(d)
        max = s[0]
        for i in d.keys():
            if len(i) > len(max):
                max = i
        return max

    def is_palindorme(self, s: str) -> bool:
        return s == s[::-1]

    # 8.23 q5 solution
    def longestPalindrome(self, s: str) -> str:
        self.start = 0
        self.max_len = 0

        for i in range(len(s)):
            self.max_leng(s, i, i)  # single core
            self.max_leng(s, i, i + 1)  # double core

        return s[self.start:self.start + self.max_len]

    def max_leng(self, s, l, r):
        while l > -1 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        l += 1
        r -= 1

        self.start = l if self.max_len < r - l + 1 else self.start
        self.max_len = max(r - l + 1, self.max_len)

    def longestXXX(self):
        pass

    def helper1(self):
        pass

    # TDD (Test Driven Development)
    def test_longestXXX(self, s):
        assert s == s[::-1]

    # q34
    def q34_searchRange(self, nums: list[int], target: int) -> list[int]:
        # PRE: Skip ask ambigious points
        # TDD: Skip Unit Test

        # None input
        if nums is None or not nums or target is None:
            return [-1, -1]

        start, end = 0, len(nums) - 1
        # case I: not find
        while start + 1 < end:
            mid = (start + end) // 2
            mid_val = nums[mid]
            if target <= mid_val:
                end = mid
            elif target > mid_val:
                start = mid
        if nums[start] == target:
            return [self.find_left_index(nums, start, target), self.find_right_index(nums, start, target)]
        if nums[end] == target:
            return [self.find_left_index(nums, end, target), self.find_right_index(nums, end, target)]

        return [-1, -1]

    def find_left_index(self, nums, index, target):
        i = index
        start = 0
        # find first
        while start + 1 < i:
            mid = (start + i) // 2
            mid_val = nums[mid]
            if target <= mid_val:
                i = mid
            else:
                start = mid
        return start if nums[start] == target else i

    def find_right_index(self, nums, index, target):
        i = index
        end = len(nums) - 1
        # find last
        while i + 1 < end:
            mid = (i + end) // 2
            mid_val = nums[mid]
            if target < mid_val:
                end = mid
            else:
                i = mid
        return end if nums[end] == target else i

    # 28 strStr https://leetcode.com/problems/implement-strstr/
    def q_28_search_substr(self, chars, pattern) -> int:
        # TDD skip
        # edge cases
        if not chars or not pattern:
            return -1

        BASE = 1_000_000
        # pattern hash_val
        pattern_val = 0
        for c in pattern:
            pattern_val = (pattern_val * 31 + ord(c)) % BASE

        hash_val = 0
        str_len = len(chars)
        pattern_len = len(pattern)
        i = 0
        FIRST_WEIGHT = 31 ** pattern_len

        # O(n) enumerate
        while i < str_len:
            hash_val = (hash_val * 31 + ord(chars[i])) % BASE
            # adc + d
            if i < pattern_len - 1:
                i += 1
                continue

            # abcd - a
            if i >= pattern_len:
                hash_val = (hash_val - ord(chars[i - pattern_len]) * FIRST_WEIGHT) % BASE
                hash_val = hash_val + BASE if hash_val < 0 else hash_val

            # bcd
            if hash_val == pattern_val and chars[i - pattern_len + 1:i + 1] == pattern:
                return i - pattern_len + 1

            i += 1

        return -1

    # https://leetcode.com/explore/challenge/card/september-leetcoding-challenge-2021/639/week-4-september-22nd-september-28th/3989/
    def numUniqueEmails(self, emails: list[str]) -> int:
        email_set = set()
        if len(emails) == 0:
            return 0

        for e in emails:
            local_name, domain_name = e.split('@')
            filter1 = local_name.split('+')[0]
            filter2 = filter1.split('.')
            addr = ''.join(filter2) + '@' + domain_name
            print(addr)
            email_set.add(addr)
        # print(email_set)
        return len(email_set)

    # https://leetcode.com/problems/3sum/
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        num_leng = len(nums)
        nums.sort()
        triplets = []
        if num_leng < 3:
            # not enough candidate
            # raise Exception('Not enough candidate')
            return []
        i = 0
        while i < num_leng - 2:
            # break case
            if nums[i] > 0:
                break
            # skip same candidates
            while 0 < i < num_leng and nums[i - 1] == nums[i]:
                i += 1
            # now 2sum from [i+1:]
            # print('i:', nums[i])
            j = i + 1
            ret_list = self.twoSum(nums[j:], -nums[i])
            if len(ret_list) != 0:
                triplets.extend(ret_list)
            i += 1
        return triplets

    def twoSum(self, nums: list[int], target: int) -> list[list[int]]:
        s_c = set()
        s_tuple = set()
        triplets = []

        for i in range(0, len(nums)):
            x = nums[i]
            if x in s_tuple:  # no dup
                print('skip x: ', x)
                continue
            c = target - x
            if c in s_c:
                # find what I want
                triplets.append([-target, x, c])
                s_tuple.add(x)
            else:
                # add what I have
                s_c.add(x)
        # print(triplets)
        return triplets

    def twoSumII(self, nums: list[int], target: int) -> list[int]:
        i = 0
        d = dict()
        for x in nums:
            c = target - x
            if c not in d.keys():
                d[x] = i
            else:
                return [i, d[c]]
            i += 1
        return []

    # Definition for singly-linked list.
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    # https://leetcode.com/problems/remove-nth-node-from-end-of-list/
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''  the length of the haed list node is default as 1 not 0 '''
        length = 1
        cur_node = head
        while cur_node.next:
            cur_node = cur_node.next
            length += 1
        print(length)
        # exceptional case
        if n > length:
            raise Exception('n out of bounds')
        if n == length:
            return head.next

        # normal cases O(n)
        cur_node = head
        stop_at = length - n - 1
        i = 0
        while i < stop_at:
            cur_node = cur_node.next
            i += 1
        stop_at_node = cur_node
        if n == 1:
            stop_at_node.next = None
            return head

        elif stop_at < length - 1:
            stop_at_node.next = stop_at_node.next.next
            return head
        else:
            raise Exception('input error')
            # return None

    # https://leetcode.com/problems/valid-parentheses/
    def isValid(self, s: str) -> bool:
        d = dict()
        d[')'] = '('
        d[']'] = '['
        d['}'] = '{'
        left = ['(', '[', '{']
        right = [')', ']', '}']
        stack = []

        for syb in s:
            if syb in left:
                stack.append(syb)
            if syb in right:
                if stack.pop() != d[syb]:
                    return False
        return True if len(stack) == 0 else False

    # https://leetcode.com/problems/merge-k-sorted-lists
    def mergeKLists(self, lists):
        h = []
        head = point = ListNode(0)
        for l in lists:
            if l:
                heapq.heappush(h, (l.val, l))
        while len(h) != 0:
            val, node = heapq.heappop(h)
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                heapq.heappush(h, (node.val, node))
        return head.next


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))
    # print(s.twoSum([-1, 0, 2, -2, 1, -4], 0))
    # print(s.longestPalindrome('aaddaaxaabacxcsssabaaxcabaax'))
    # "xaabacxcabaax"
    # print(s.is_palindorme('abccb3a'))
    # real algorithm ...
