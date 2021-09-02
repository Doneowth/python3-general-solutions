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

if __name__ == '__main__':
    s = Solution()
    s.test_longestXXX('aba')
    #print(s.longestPalindrome('aaddaaxaabacxcsssabaaxcabaax'))
    # "xaabacxcabaax"
    # print(s.is_palindorme('abccb3a'))
    # real algorithm ...
