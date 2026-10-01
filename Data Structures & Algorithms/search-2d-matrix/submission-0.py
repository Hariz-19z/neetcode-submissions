class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row=len(matrix)

        cols=len(matrix[0])

        left=0
        right=row*cols-1


        while left<=right:

            mid=(left+right)//2

            rows=mid//cols
            col=mid%cols

            if matrix[rows][col]==target:
                return True
            elif matrix[rows][col]<target:
                left=mid+1

            else:
                right=mid-1
        return False






        