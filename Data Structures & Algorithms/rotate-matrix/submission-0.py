class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) -1

        while l < r:
            for i in range(r-l):
                #top, bottom = l,r
                #save topleft
                topleft = matrix[l][l+i]

                #move bottom left to top left
                matrix[l][l+i] = matrix[r-i][l]

                #move bottom right to bottom left
                matrix[r -i][l] = matrix[r][r-i]

                #move op right to bottom right
                matrix[r][r-i] = matrix[l+i][r]
                matrix[l+i][r] = topleft
            r-=1
            l+=1
        