class Solution(object):

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        self.data = []
        
        for i in range(numRows):
            self.data.append(self.__gen_next_line(i))
            
        return self.data
    
    def __gen_next_line(self, currRowNum):
        if currRowNum == 0:
            return [1]
        elif currRowNum == 1:
            return [1,1]        
        else:
            data = [1]
            for i in range(currRowNum/2):
                data.append(self.data[currRowNum-1][i-1]+self.data[currRowNum-1][i])
            
            rslt = data
            data.reverse()
            
            if currRownum % 2 == 0:
                rslt.extend(data)
            else:
                rslt.extend(data[1:])

            return rslt
        