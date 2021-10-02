class Solution:
    def reverse(self, x):
        reversed = 0
        flag = 0

        if(x<0):
            x = -1*x
            flag = 1


        while (x != 0):
            remainder = x % 10
            x = x // 10
            reversed = reversed*10 + remainder  

        if reversed in range(-2**31, 2**31 - 1):
            if(flag == 0):
                return(reversed)
            else:
                return(-1*reversed)
        # else:
            # return(0)


def main():
    x = int(input())
    print(Solution().reverse(x))

if __name__ == "__main__":
    main()
    


