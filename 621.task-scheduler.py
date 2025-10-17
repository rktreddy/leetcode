#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
class Solution:
    # def leastInterval(self, tasks: List[str], n: int) -> int:
    #     """ Approach 1: Using Priority Queue / Max Heap O(N), O(1) """
    #     # Build frequency map
    #     freq = [0] * 26
    #     for ch in tasks:
    #         freq[ord(ch) - ord("A")] += 1

    #     # Max heap to store frequencies
    #     pq = [-f for f in freq if f > 0]
    #     heapq.heapify(pq)

    #     time = 0
    #     # Process tasks until the heap is empty
    #     while pq:
    #         cycle = n + 1
    #         store = []
    #         task_count = 0
    #         # Execute tasks in each cycle
    #         while cycle > 0 and pq:
    #             current_freq = -heapq.heappop(pq)
    #             if current_freq > 1:
    #                 store.append(-(current_freq - 1))
    #             task_count += 1
    #             cycle -= 1
    #         # Restore updated frequencies to the heap
    #         for x in store:
    #             heapq.heappush(pq, x)
    #         # Add time for the completed cycle
    #         time += task_count if not pq else n + 1
        
    #     return time
        
    # def leastInterval(self, tasks: List[str], n: int) -> int:
    #     """ Approach 2: Filling the Slots and Sorting O(N), O(1) """
    #     freq = [0] * 26
    #     for task in tasks:
    #         freq[ord(task) - ord("A")] += 1

    #     # Sort the frequency array in non-decreasing order
    #     freq.sort() 
    #     # Calculate the maximum frequency of any task
    #     max_freq = freq[25] - 1
    #     # Calculate the number of idle slots that will be required
    #     idle_slots = max_freq * n

    #     # Iterate over the frequency array from the second highest frequency to the lowest frequency
    #     for i in range(24, -1, -1):
    #         idle_slots -= min(max_freq, freq[i])

    #     # If there are any idle slots left, add them to the total number of tasks
    #     return idle_slots + len(tasks) if idle_slots > 0 else len(tasks)
    
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """ Approach 3: Greedy Approach O(N), O(1) """
        # Counter array to store the frequency of each task
        counter = [0] * 26
        max_val = 0
        max_count = 0

        # Traverse through tasks to calculate task frequencies
        for task in tasks:
            counter[ord(task) - ord("A")] += 1
            if max_val == counter[ord(task) - ord("A")]:
                max_count += 1
            elif max_val < counter[ord(task) - ord("A")]:
                max_val = counter[ord(task) - ord("A")]
                max_count = 1
            
        # Calculate idle slots, available tasks, and idles needed
        part_count = max_val - 1
        part_length = n - (max_count - 1)
        empty_slots = part_count * part_length
        available_tasks = len(tasks) - max_val * max_count
        idles = max(0, empty_slots - available_tasks)

        # Return the total time required
        return len(tasks) + idles 

# @lc code=end

