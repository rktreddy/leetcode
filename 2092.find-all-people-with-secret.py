#
# @lc app=leetcode id=2092 lang=python3
#
# [2092] Find All People With Secret
#

# @lc code=start
class Solution:
    # def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
    #     """ cracking faang BFS O(n log n), O(n) """
    #     meetings.sort(key = lambda x: x[2])
    #     meeting_dict = collections.defaultdict(list)

    #     for person1, person2, time in meetings:
    #         meeting_dict[time].append([person1, person2])

    #     has_secret = {0, firstPerson}
    #     for time, same_time_meetings in meeting_dict.items():
    #         # Build Graph
    #         graph = collections.defaultdict(list)
    #         seen = set()

    #         for person1, person2 in same_time_meetings:
    #             graph[person1].append(person2)
    #             graph[person2].append(person1)

    #             if person1 in has_secret:
    #                 seen.add(person1)

    #             if person2 in has_secret:
    #                 seen.add(person2)

    #         # Do BFS
    #         queue = collections.deque(seen)
    #         while queue:
    #             person = queue.popleft()
    #             for neighbor in graph[person]:
    #                 if neighbor not in has_secret:
    #                     has_secret.add(neighbor)
    #                     queue.append(neighbor)
    #     return list(has_secret)
    
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        """ practice: cracking faang BFS O(n log n), O(n) """
        meetings.sort(key = lambda x: x[2])
        meetings_dict = collections.defaultdict(list)

        for person1, person2, time in meetings:
            meetings_dict[time].append([person1, person2])

        has_secret = {0, firstPerson}
        for time, same_time_meetings in meetings_dict.items():
            graph = collections.defaultdict(list)
            seen = set()

            for person1, person2 in same_time_meetings:
                graph[person1].append(person2)
                graph[person2].append(person1)

                if person1 in has_secret:
                    seen.add(person1)
                if person2 in has_secret:
                    seen.add(person2)

            queue = collections.deque(seen)
            while queue:
                person = queue.popleft()
                for neighbor in graph[person]:
                    if neighbor not in has_secret:
                        has_secret.add(neighbor)
                        queue.append(neighbor)
                        
        return list(has_secret)


    
    # def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
    #     """ chat gpt """
    #     meetings.sort(key=lambda x: x[2])
    #     meeting_dict = collections.defaultdict(list)

    #     for p1, p2, time in meetings:
    #         meeting_dict[time].append((p1, p2))

    #     has_secret = {0, firstPerson}

    #     for time in sorted(meeting_dict.keys()):
    #         same_time = meeting_dict[time]
    #         graph = collections.defaultdict(list)
    #         starters = set()

    #         # build graph for this time block
    #         for p1, p2 in same_time:
    #             graph[p1].append(p2)
    #             graph[p2].append(p1)

    #         # determine who can start spreading (only secret holders involved this block)
    #         for p1, p2 in same_time:
    #             if p1 in has_secret:
    #                 starters.add(p1)
    #             if p2 in has_secret:
    #                 starters.add(p2)

    #         # BFS spreading within this time block
    #         queue = collections.deque(starters)
    #         visited = set(starters)

    #         while queue:
    #             cur = queue.popleft()
    #             for nei in graph[cur]:
    #                 if nei not in has_secret:
    #                     has_secret.add(nei)
    #                     queue.append(nei)

    #     return list(has_secret)
    
    # def findAllPeople(
    #     self, n: int, meetings: List[List[int]], firstPerson: int
    # ) -> List[int]:
    #     """ leetcode: BFS """
    #     # Sort meetings in increasing order of time
    #     meetings.sort(key=lambda x: x[2])

    #     # Group Meetings in increasing order of time
    #     same_time_meetings = defaultdict(list)
    #     for x, y, t in meetings:
    #         same_time_meetings[t].append((x, y))

    #     # Boolean Array to mark if a person knows the secret or not
    #     knows_secret = [False] * n
    #     knows_secret[0] = True
    #     knows_secret[firstPerson] = True

    #     # Process in increasing order of time
    #     for t in same_time_meetings:
    #         # For each person, save all the people whom he/she meets at time t
    #         meet = defaultdict(list)
    #         for x, y in same_time_meetings[t]:
    #             meet[x].append(y)
    #             meet[y].append(x)

    #         # Start traversal from those who already know the secret at time t
    #         # Set to avoid redundancy
    #         q = set()
    #         for x, y in same_time_meetings[t]:
    #             if knows_secret[x]:
    #                 q.add(x)
    #             if knows_secret[y]:
    #                 q.add(y)

    #         # Do BFS
    #         q = deque(q)
    #         while q:
    #             person = q.popleft()
    #             for next_person in meet[person]:
    #                 if not knows_secret[next_person]:
    #                     knows_secret[next_person] = True
    #                     q.append(next_person)

    #     # List of people who know the secret
    #     return [i for i in range(n) if knows_secret[i]]



        
# @lc code=end

