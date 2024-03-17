import heapq

def interval_partitioning(lectures):
    # Sort lectures by start times
    sorted_lectures = sorted(lectures, key=lambda x: x[0])
    
    # Initialize a priority queue to store classrooms with their finish times
    classrooms = []
    
    # Initialize the number of allocated classrooms
    num_classrooms = 0
    
    # Iterate through sorted lectures
    for start_time, finish_time in sorted_lectures:
        if classrooms and classrooms[0] <= start_time:
            # If there is a classroom available whose finish time is less than or equal to the start time of the current lecture
            # Reuse that classroom by updating its finish time
            heapq.heappop(classrooms)
        else:
            # Allocate a new classroom
            num_classrooms += 1
        
        # Schedule the current lecture in the allocated classroom
        heapq.heappush(classrooms, finish_time)
    
    return num_classrooms

# Example inputs
lectures = [(0, 1), (1, 3), (2, 4), (3, 5), (4, 6), (1,5), (5,10)]
min_classrooms = interval_partitioning(lectures)
print("Minimum number of classrooms required:", min_classrooms)