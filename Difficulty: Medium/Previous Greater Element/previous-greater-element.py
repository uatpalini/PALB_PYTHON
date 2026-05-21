class Solution:
    def preGreaterEle(self, arr):
        st = []
        res = []

        for x in arr:

            while st and st[-1] <= x:
                st.pop()

            if st:
                res.append(st[-1])
            else:
                res.append(-1)

            st.append(x)

        return res