class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        from collections import defaultdict
        n = len(accounts)
        parent = list(range(n))

        size = [1]*n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])

            return parent[x]

        def union(x,y):
            boss_x = find(x)
            boss_y = find(y)

            if boss_x == boss_y:
                return

            if size[boss_x]<size[boss_y]:
                boss_x,boss_y = boss_y,boss_x

            parent[boss_y] = boss_x
            size[boss_x] += size[boss_y]

        email_to_acc = {}
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_acc:
                    union(i, email_to_acc[email])
                else:
                    email_to_acc[email] = i

        merged_emails = defaultdict(list)
        for email, acc_id in email_to_acc.items():
            root = find(acc_id)
            merged_emails[root].append(email)

        result = []
        for root, emails in merged_emails.items():
            name = accounts[root][0]
            result.append([name] + sorted(emails))

        return result
                