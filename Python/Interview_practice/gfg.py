

def get_freq(word: str) -> dict[str, int]:
    freq = {}
    for ch in word:
        freq[ch] = freq.get(ch, 0) + 1
    return freq


def minimum_substring_with_all_chars(s: str, t: str) -> str:
    if len(s) < len(t):
        return ""
    need = get_freq(t)
    have = 0
    window = {}
    need_count = len(need)
    min_len = float("inf")
    min_start = 0
    left = 0

    for right in range(len(s)):
        ch = s[right]
        window[ch] = window.get(ch, 0) + 1

        if ch in need and window[ch] == need[ch]:
            have += 1

        while have == need_count:
            if (right - left + 1) < min_len:
                min_len = right - left + 1
                min_start = left
            
            window[s[left]] -= 1
            if s[left] in need and window[s[left]] < need[s[left]]:
                have -= 1
            left += 1
    return s[min_start: min_start + min_len] if min_len != float("inf") else ""


def longest_substring_without_repeated_char(s: str) -> str:
    if not s:
        return ""
    left = 0
    last_seen = {}
    best_start = 0
    best_length = 0
    for right in range(len(s)):
        ch = s[right]
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        last_seen[ch] = right
        if best_length < right - left + 1:
            best_length = right - left + 1
            best_start = left
    return s[best_start: best_start + best_length]




def permutation_in_string(s1: str, s2: str) -> bool:
    if not s2 or len(s1) > len(s2):
        return False
    s1_freq = get_freq(s1)
    left = 0
    for right in range(len(s1) - 1, len(s2)):
        if s1_freq == get_freq(s2[left:right+1]):
            return True
        left += 1
    return False


if __name__ == "__main__":
    print(permutation_in_string("ab", "eidboaoo"))