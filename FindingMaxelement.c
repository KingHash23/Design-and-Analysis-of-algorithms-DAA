//Pseudo code for finding maximum number
/*
Start
  declare and inialize the array numbers
  declare the size = length of the array numbers
  declare the max = the first element of the array numbers [0]
  loop through each element in numbers
  for i = 1 to size - 1 do 
  if the current element is greater than max
  max = number[i]
  end if statement
  end loop statement
  print the maximum element
  end program
  stop
*/


#include <stdio.h>  // include the standard input output header file
int main()  // the is where my code goes since the computer starts to read and execute the code line by line
{       
    int numbers[] = {6, 4, 7, 5, 3, 9, 8, 1, 0, 2};  // declaring and initializing the array     
    int size = sizeof(numbers) / sizeof(numbers[0]);   // calculate the number of elements in the array      
    int max = numbers[0]; // initialize max with the first element of the array     
    for (int i = 0; i < size; i++)  // loop through the array to find the max element 
    {                   
        if(numbers[i] > max)    // if the current element is greater than maximum then it updates the maximum element              
            max = numbers[i];        
    }      
    printf("The maximum element in array is: %d\n", max);  // print the maximum element   
    return 0;    // to indicate successful execution 
}









/*
#include <stdio.h> 
int main()
{       
    int numbers[] = {6, 4, 7, 5, 3, 9, 8, 1, 0, 2};  
    int size = sizeof(numbers) / sizeof(numbers[0]);  
    int max = numbers[0];  
    int index = 0;
    while (index < size)  
    {    
        if (numbers[index] > max)       
            max = numbers[index];      
        index++;   // Move to the next element 
    }      
    printf("The maximum element in the array is: %d\n", max); 
    return 0;   
}*/