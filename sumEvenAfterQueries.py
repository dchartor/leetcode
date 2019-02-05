def sumEvenAfterQueries(self, A: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
       S = sum(x for x in A if x % 2 == 0)
       res = []

       for x, k in queries:
           if A[k] % 2 == 0: S -= A[k]
           A[k] += x
           if A[k] % 2 == 0: S += A[k]
           res.append(S)
       return res
