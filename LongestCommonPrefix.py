class Solution:
    def longestCommonPrefix(str_elements):
        result = ''
        # print(str, "\nlength is ''''''", str_length)
        
        str_elements.sort()
        str_length = len(str_elements)


        for i in range(0,min(len(str_elements[0]),len(str_elements[-1]))):

            if(str_elements[0][i]!=str_elements[-1][i]):
                break
            else:
                result += str_elements[0][i]

        return result

def main():
    i=0
    str = input()
    str_elements = str.split(",")
    # print(str_elements)
    for i in range(0, len(str_elements)):
        str_elements[i] = str_elements[i].replace('"', '')
        str_elements[i] = str_elements[i].replace('[', '')
        str_elements[i] = str_elements[i].replace(']', '')
    # print("\n-------------\n", str_elements)

    print(Solution.longestCommonPrefix(str_elements))

if __name__ == "__main__":
    main()