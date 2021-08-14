class Solution:
	# @param A : string
	# @param B : string
	# @return an integer
	

    
    def strStr(self, A, B):
        if (len(A)==0) or (len(B)==0):
            return -1
        if(A==B):
            return 0
        lps=[0]*len(B)
        i=1
        l=0
        while(i<len(B)):
            if B[l]==B[i]:
                lps[i]=l+1
                i+=1
                l+=1
            else:
                if l!=0:
                    l=lps[l-1]

                else:
                    i+=1
        N=len(A)
        i,l=0,0
        while(i<N):
            if A[i]==B[l]:
                i+=1
                l+=1
            else:
                if l!=0:
                    l=lps[l-1]
                else:
                    i+=1
            if l==len(B):
                return i-l

        return -1
