class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        start_index = 0
        end_index = 0
        max_length = 0
        unique_characters = set()

        while end_index < len(s):
            if s[end_index] not in unique_characters:
                unique_characters.add(s[end_index])
                end_index += 1
                max_length = max(max_length, len(unique_characters))
            else:
                unique_characters.remove(s[start_index])
                start_index += 1
        return max_length
