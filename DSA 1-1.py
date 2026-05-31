#Task 1
#Array Rotation

#Taking input of Array 
arr=input("Enter the elements of array separated by space: \n").split()

#Taking input of number of rotations
k=int(input("Enter the number of elements of rotations: \n"))

k=k%len(arr) #using modulus operatore for cases where no of rotaion isgreater than the lenght of array

#Rotation of array using slicing and concatenation (-k for right rotation)
rotate=arr[-k:]+arr[:-k]
 
#printing the output(rotated array)
print("The rotated array is: \n",rotate)
