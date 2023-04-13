import numpy as np
import multiprocessing as mp
import time as t


def test(liste):
    s = 0
    for i in liste:
        s+=i
    t.sleep(1)
    return s



if __name__ == "__main__":
    
    # liste= []
    # for i in range(1000):
    #     liste.append(i)
        
    # pool = mp.Pool(4)
    # arr= np.array_split(liste,4)
    
    # print(pool.map(test,arr))
    
    # pool.close()
    # pool.join()
    
    a=np.array([[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]])
    b=np.copy(a)
    a[0,0]=9