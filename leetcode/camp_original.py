class Solution:

    # search substring
    # 'abcdef', 'def' -> 3
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


if __name__ == '__main__':
    s = Solution()
    print(s.search_substr('asdsddxgguoohgddssass', 'dssa'))
