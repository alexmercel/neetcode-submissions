class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2
        if len(A) > len(B):
            A,B = nums2,nums1
        

        l, r= 0,len(A) - 1
        while True:
            m = (l + r ) // 2
            n = half - m - 2

            #A left right-end
            Aleft = A[m] if m >= 0 else float("-infinity")
            #A right left-end
            Aright = A[m+1] if (m+1) < len (A) else float("infinity")
            #B left right-end
            Bleft = B[n] if n >= 0 else float("-infinity")
            #B right left-end
            Bright = B[n+1] if (n+1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                
                if total % 2 :
                    return min(Aright,Bright)

                return (max(Aleft,Bleft)+min(Aright,Bright))/2
            
            elif Aleft > Bright:
                r = m - 1
            else:
                l = m + 1

        