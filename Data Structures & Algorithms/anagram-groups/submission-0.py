class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mp = {}

        for ch in strs:
            sorted_ch = "".join(sorted(ch))

            if sorted_ch in mp:
                mp[sorted_ch].append(ch)
            else:
                mp[sorted_ch] = [ch]

        ans = []
        for val in mp.values():
            ans.append(val)
        
        return ans
        