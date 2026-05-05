class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        record = {}
        for num in nums:
            if num in record:
                record[num] = record[num] + 1
            else:
                record[num] = 1
        
        sorted_cnt = dict(sorted(record.items(), key=lambda x:x[1], reverse=True))

        result = []
        counter = 0
        for num, cnt in sorted_cnt.items():
            counter = counter + 1
            if counter <= k:
                result.append(num)
            else:
                break 

        return result