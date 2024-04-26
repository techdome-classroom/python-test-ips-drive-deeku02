def longest_substring(s):
    """
    Implementation of the longestSubstring function.
    """
    longest_substring_length = 0

    for i in range(len(s)):
        current_string_set = set()

        for x in range(i, len(s)):
            if s[x] in current_string_set:
                break
            else:
                current_string_set.add(s[x])

        longest_substring_length = max(
            longest_substring_length,
            len(current_string_set)
        )

    return longest_substring_length



    for i in range(len(s)):
        current_string_set = set()

        for x in range(i, len(s)):
            if s[x] in current_string_set:
                break
            else:
                current_string_set.add(s[x])

        longest_substring_length = max(
            longest_substring_length,
            len(current_string_set)
        )

    return longest_substring_length


