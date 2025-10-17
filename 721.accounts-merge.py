#
# @lc app=leetcode id=721 lang=python3
#
# [721] Accounts Merge
#

# @lc code=start
# class Solution:
    # def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
    #     """ Algomonster: Union-Find algorithm and a hash map O(N*K + ElogE), O(N + E) """
    #     # Helper function to find the root parent for any index.
    #     def find(index: int) -> int:
    #         if parent[index] != index:
    #             parent[index] = find(parent[index])
    #         return parent[index]
        
    #     # The number of accounts.
    #     num_aaccounts = len(accounts)

    #     # Initialize a list where the value at index i is the parent of i.
    #     parent = list(range(num_aaccounts))

    #     # Dictionary to map each email to its account index.
    #     email_to_account_id = {}

    #     # Assign parents for accounts with shared emails.
    #     for account_id, account in enumerate(accounts):
    #         for email in account[1:]:
    #             if email in email_to_account_id:
    #                 # Union operation: set the parent of the current account to the account 
    #                 # already associated with this email.
    #                 parent[find(account_id)] = find(email_to_account_id[email])
    #             else:
    #                 email_to_account_id[email] = account_id

    #     # Map each account index to a set of emails under the corresponding parent.
    #     emails_under_parent_account = defaultdict(set)
    #     for account_index, account in enumerate(accounts):
    #         for email in account[1:]:
    #             emails_under_parent_account[find(account_index)].add(email)

    #     # Compile the merged accounts: one per parent index.
    #     merged_accounts = []
    #     for parent_index, emails in emails_under_parent_account.items():
    #         # Sort the emails.
    #         sorted_emails = sorted(emails)
    #         # Prepend the account name.
    #         account_name = [accounts[parent_index][0]]
    #         merged_account = account_name + sorted_emails
    #         # Append the merged account to the result.
    #         merged_accounts.append(merged_account)
      
    #     return merged_accounts

# class UnionFind:
    # def __init__(self, n):
    #     self.parent = [i for i in range(n)]
    #     self.rank = [1] * n

    # def find(self, x):
    #     while x != self.parent[x]:
    #         self.parent[x] = self.parent[self.parent[x]]
    #         x = self.parent[x]
    #     return x
    
    # def union(self, x1, x2):
    #     p1, p2 = self.find(x1), self.find(x2)
    #     if p1 == p2:
    #         return False
    #     if self.rank[p1] > self.rank[p2]:
    #         self.parent[p2] = p1
    #         self.rank[p1] += self.rank[p2]
    #     else:
    #         self.parent[p1] = p2
    #         self.rank[p2] += self.rank[p1]
    #     return True
    
class UnionFind:
    """ practice """
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
        
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
        
    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True
        

class Solution:
    # def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
    #     """ Neetcode: Union Find O(N*K + ElogE), O(N + E) """
    #     uf = UnionFind(len(accounts))
    #     emailToAcc = {} # email -> index of acc

    #     for i, account in enumerate(accounts):
    #         for email in account[1:]:
    #             if email in emailToAcc:
    #                 uf.union(i, emailToAcc[email])
    #             else:
    #                 emailToAcc[email] = i

    #     emailGroup = defaultdict(list) # index of acc -> list of emails
    #     for email, i in emailToAcc.items():
    #         leader = uf.find(i)
    #         emailGroup[leader].append(email)

    #     res = []
    #     for i, emails in emailGroup.items():
    #         name = accounts[i][0]
    #         # res.append([name] + sorted(emailGroup[i])) # array concatenation
    #         res.append([name] + sorted(emails)) # array concatenation

    #     return res
    
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """ practice: Neetcode: Union Find O(N*K + ElogE), O(N + E) """
        uf = UnionFind(len(accounts))

        emailToAcc = {}

        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToAcc:
                    uf.union(i, emailToAcc[e])
                else:
                    emailToAcc[e] = i

        emailGroup = defaultdict(list)
        for e, i in emailToAcc.items():
            leader = uf.find(i)
            emailGroup[leader].append(e)
        
        res = []
        for i, emails in emailGroup.items():
            name = accounts[i][0]
            res.append([name] + sorted(emails))

        return res

# @lc code=end

