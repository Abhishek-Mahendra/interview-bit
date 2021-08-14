class Solution:
	# @param A : list of strings
	# @return a strings
	def longestCommonPrefix(self, A):
		l=min(A,key=len)
		count=0
		j=0
		for i in l:
			for j in range(len(A)):
				if A[j][count]!=i:
					return l[:count]
			count+=1
		return l
