class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maximum = 0
        gains = 0
        for num in gain:
            gains += num
            if maximum < gains:
                maximum = gains
        return maximum