import sys
sys.stdin = open("input.txt", 'r')

if __name__ =="__main__":
    s = input().strip()
    res = [''] * len(s)

    def func(arr,start):
        if not arr:
            return
        _min = min(arr)
        idx = arr.index(_min)
        res[start+idx] = _min
        print("".join(res))
        func(arr[idx+1:],start+idx+1)
        func(arr[:idx],start)
    func(s,0)








    
                


        
    


