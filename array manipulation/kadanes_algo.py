

'''
Kadanes algorithm :

Is used to find the largest sum of subarray present in an array

Time complexity : 0(n)
Space complexity: 0(1)

Logic : 

Whenever we try to find find from the start to end of an array, whenever we come across a sum < 0, we can
conclude that it is impossible for that particular instance to be the largest sum, hence we reset the sum = 0 and  move on

'''


def kadane(arr):
    sum = 0
    maxSum = 0
    for i in arr:
        sum += i
        maxSum = max(maxSum, sum)
        if(sum < 0):
            sum = 0
            
    return maxSum


def naive(arr):
    sum = 0
    maxSum = 0
    l = []
    
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            sum = 0
            for k in range(i,j+1):
                sum += arr[k]
                l.append(sum)
                
    return max(l)
            
                

#arr = [1, -2, 3, 10, -4, 7, 2, -5]
arr = [2, 3, -2, 4]

print("The largest sum of subarray using kadane is: ", kadane(arr))
print("The largest sum of subarray using naive is: ", naive(arr))





