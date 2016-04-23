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
        else if currRowNum == 1:
            return [1,1]        
        else:
            data = []
            for i in range(currRowNum-1):
                data.append(self.data[currRowNum-1][i-1]+self.data[currRowNum-1][i])
            
            data.append(1)
            return data
        