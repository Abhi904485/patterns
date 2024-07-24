from typing import List



def finLength(N : int, color : List[int], radius : List[int]) -> int:
    st = [[color[0], radius[0]]]
    for i in range(1,N):
        if st and st[-1] == [color[i], radius[i]]:
            st.pop()
        else:
            st.append([color[i], radius[i]])
    return len(st)
        


print(finLength(4, [1, 3, 3, 1], [2, 5, 5, 2]))
