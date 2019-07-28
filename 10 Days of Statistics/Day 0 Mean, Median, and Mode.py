# https://www.hackerrank.com/challenges/s10-basic-statistics/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT

#Input Format
#The first line contains an integer, N, denoting the number of elements in the array. 
N = int(input())
#The second line contains N space-separated integers describing the array's elements.
elements = list(map(int, input().split(' ')))


#OUTPUT: Print  lines of output in the following order:
#Print the mean on a new line, to a scale of  decimal place (i.e., , ).
mean = sum(elements)/N
print(mean)

#Print the median on a new line, to a scale of  decimal place (i.e., , ).
sorted_elements = sorted(elements)

#if the list has odd length, get the single element in the middle.
#for example, if the list has 5 elements, get element 3
#length_of_elements = len(elements)
#if (length_of_elements % 2 == 1):
if (N % 2 == 1):
    #position_of_middle_element = (length_of_elements+1)/2
    position_of_middle_element = (N+1)/2
    print(sorted_elements[position_of_middle_element])
    #print('odd length')
#if the list has even length, get the mean of the middle elements
#for example, if the list has 6 elements, use elements 3 and 4
else:
    #print("comparing element {} with element {}".format(int(N/2)-1, int(N/2)))
    mean_of_middle_elements = (sorted_elements[int(N/2)-1]+sorted_elements[int(N/2)])/2
    print(mean_of_middle_elements)
    #print('even length')


#Print the mode on a new line; if more than one such value exists, print the numerically smallest one.
position = 0
mode = sorted_elements[position]
mode_ocurrance_count = 0
current_ocurrance_count = 1
while (position < N-1):
    if (sorted_elements[position] == sorted_elements[position+1]):
        current_ocurrance_count += 1
    
    if (current_ocurrance_count > mode_ocurrance_count):
        mode = sorted_elements[position]
        mode_ocurrance_count = current_ocurrance_count

    if (sorted_elements[position] != sorted_elements[position+1]):
        current_ocurrance_count = 1

    position+=1

print(mode)
