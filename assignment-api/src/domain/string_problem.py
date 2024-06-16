from itertools import zip_longest, islice
from dataclasses import dataclass

@dataclass
class StringProblemEntity:
    s:str = None
    # Complete the maxValue function below.
    def maxValue(self) -> int:
        sm = self.suffix_matrix(self.s)
        sa = self.invert(sm[-1])

        # got next common prefix length cpl, it may be ....
        # - shorter than last: pop&finalize last till not shorter
        # - longer than last: add positon to markers
        # - equal to last:  (do nothing)
        maxval = len(self.s)
        last = None
        markers=[]
        for i in range(len(sa)-1):
            cpl = self.lcp(sm,sa[i],sa[i+1])
            xi=i
            while last is not None and cpl < last:
                _,xi=markers.pop()
                maxval = max((i-xi+1)*last, maxval)
                last = markers[-1][0] if markers else None
            if 0 < cpl and (last is None or last < cpl):
                last = cpl 
                markers.append((cpl,xi))
        # any dangling markers?
        while last is not None:
            _,xi=markers.pop()
            maxval = max((len(sa)-xi)*last, maxval)
            last = markers[-1][0] if markers else None
        return maxval

    @staticmethod
    def invert(ar):
        ret = [0] * len(ar)
        for i,v in enumerate(ar): ret[v]=i 
        return ret

        


    @staticmethod
    def to_int_keys(l):
        """
        l: iterable of keys
        returns: a list with integer keys
        """
        seen = set()
        ls = []
        for e in l:
            if not e in seen:
                ls.append(e)
                seen.add(e)
        ls.sort()
        index = {v: i for i, v in enumerate(ls)}
        return [index[v] for v in l]
    
    @staticmethod
    def suffix_matrix(s):
        """
        suffix matrix of s
        O(n * log(n)^2)
        """
        n = len(s)
        k = 1
        line = StringProblemEntity.to_int_keys(s)
        ans = [line]
        while max(line) < n - 1:
            line =StringProblemEntity.to_int_keys(
                [a * (n + 1) + b + 1
                for (a, b) in
                    zip_longest(line, islice(line, k, None),
                            fillvalue=-1)])
            ans.append(line)
            k <<= 1
        return ans

    @staticmethod    
    def lcp(sm, i, j):
        """
        longest common prefix
        O(log(n))

        sm: suffix matrix
        """
        n = len(sm[-1])
        if i == j:
            return n - i
        k = 1 << (len(sm) - 2)
        ans = 0
        for line in sm[-2::-1]:
            if i >= n or j >= n:
                break
            if line[i] == line[j]:
                ans ^= k
                i += k
                j += k
            k >>= 1
        return ans

