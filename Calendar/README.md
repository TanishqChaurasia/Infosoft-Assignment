1. First step was to understand the problem and come up with a logic of how I would solve this problem.
2. Then I tried understanding what the developer was trying to achieve/do, i.e. he was trying to implement a binary tree with each node of the tree representing a time slot. 
3. With each new time slot he would check if the new time slot would fall in the left child or right child of the existing time slot(if there is any) and for that the condition that he created using an IF statment had some issues.
4. The correct statement would be if the start time of the new time slot was greater than the end time of the existing time slot, a booking is possible. In a similar way if the end time of the new time slot was smaller then the start time of the existing time slot, a booking was possible.
5. So the only change to the code was reversing the comparison operators. But when I ran the code at the time slots where it should return False it was returning None. So I realized there was no condition where it will return False.
6. The only place it should return False is where the above mentioned conditions failed. So I added an ELSE condition returning False.
7. These were the only changes required to make this code work.
