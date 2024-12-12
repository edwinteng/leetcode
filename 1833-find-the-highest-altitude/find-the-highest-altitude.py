class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = 0
        max_alt = alt
        for elm in gain:
            alt+=elm
            max_alt=max(alt,max_alt)
        return max_alt