class Solution:
    def isPalindrome(self, x) -> bool:
        reversed = 0
        original = x
        if(x<0):
            return False
        while (x>0):
            reversed = reversed*10 + x % 10
            x = x // 10

        if(reversed == original):
            return True
        else:
            return False

        


def main():
    x = int(input())
    print(Solution().isPalindrome(x))

if __name__ == "__main__":
    main()