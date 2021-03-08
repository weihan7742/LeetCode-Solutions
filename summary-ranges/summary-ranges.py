class Solution:
    def summaryRanges(self,nums):
        if nums == []:
            return nums
        
        temp = None
        output = []
        for i in range(len(nums)-1):
            if nums[i]+1 == nums[i+1]:
                if temp == None:
                    temp = nums[i]
            else:
                if temp == None:
                    output.append(str(nums[i]))
                else:
                    output.append(str(temp)+"->"+str(nums[i]))
                    temp = None
            i += 1

        if temp != None: 
            output.append(str(temp)+"->"+str(nums[i]))
        else:
            output.append(str(nums[len(nums)-1]))

        return output
            