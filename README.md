# Interval Partitioning

This repository contains an implementation of the interval partitioning algorithm in Python.

## Description

Interval partitioning is a problem in scheduling where the goal is to find the minimum number of classrooms needed to schedule all lectures so that no two lectures occur at the same time in the same room. Each lecture has a start time and finish time, and the algorithm aims to allocate classrooms such that no two lectures overlap.

The provided implementation of the interval partitioning algorithm efficiently computes the minimum number of classrooms required to schedule all lectures without any overlapping.

## Implementation

The interval partitioning algorithm works as follows:

1. Sort the lectures by their start times in non-decreasing order.
2. Initialize a priority queue to store classrooms along with their finish times.
3. Initialize the number of allocated classrooms to 0.
4. Iterate through the sorted lectures:
   - If there is a classroom available whose finish time is less than or equal to the start time of the current lecture, reuse that classroom by updating its finish time.
   - Otherwise, allocate a new classroom.
5. Schedule the current lecture in the allocated classroom.
6. Return the number of allocated classrooms.

## How to Use

To use this implementation of the interval partitioning algorithm, follow these steps:

1. Make sure you have Python installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the directory containing the Python file.
4. Open a terminal or command prompt.
5. Run the following command to execute the script:

    ```
    python interval_partitioning.py
    ```

6. The script will output the minimum number of classrooms required to schedule all lectures without any overlapping.

## Example
- Example inputs: lectures = [(0, 1), (1, 3), (2, 4), (3, 5), (4, 6), (1,5), (5,10)]
- The first time is the starting time of the lecture and second time is finish time
- It will find the minimum amount of classrooms that it can provide with these scheduled lectures

![interval_partitioning](https://github.com/kainoa7/interval_partitioning/assets/97155994/8bbc45d3-929d-4800-b8de-73cfba599a84)




