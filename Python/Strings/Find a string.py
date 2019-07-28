# https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):
    # i = 0
    # len_of_sub_string = len(sub_string)
    # count_of_ocurrencies = 0
    # while i < (len(string)-len_of_sub_string):
    #     result_of_find_in_string = string.find(sub_string, i)
    #     if result_of_find_in_string == -1:
    #         return count_of_ocurrencies
    #     count_of_ocurrencies += 1
    #     i = result_of_find_in_string + 1
    # return count_of_ocurrencies

    # # all the code above can be written as:
    return sum(int(string.startswith(sub_string, i)) for i in range(len(string)))
    

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
