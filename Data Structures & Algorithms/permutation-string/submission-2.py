class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)

        if window_size > len(s2):
            return False

        needed = Counter(s1)
        window = Counter(s2[:window_size])

        if window == needed:
            return True

        left = 0

        for right in range(window_size, len(s2)):
            # Add the new character entering the window
            window[s2[right]] += 1

            # Remove the character leaving the window
            left_char = s2[left]
            window[left_char] -= 1

            if window[left_char] == 0:
                del window[left_char]

            left += 1

            if window == needed:
                return True

        return False
