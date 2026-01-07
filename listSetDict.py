import sys


class Lis:
    my_list=[]
    a=[2,4,6,8,9,11]
    print(f"my list take {sys.getsizeof(my_list)} space")

    for i in a:
        if i%2==0:
            my_list.append(i)


    print(my_list)
    my_list.pop(2)
    my_list.remove(4)
    my_list.append(6)
    my_list.append(10)
    print(my_list)
    new_list=my_list[1:4]
    print(new_list)
    my_list.insert(3,5)

    new_list=my_list[1:4]
    print(new_list)
    print(my_list)


class Se:
    my_set=set()
    print(f"set have size {sys.getsizeof(my_set)}")
    my_set.add("ap")
    my_set.add("sy")
    my_set.add("ba")

    raw=["a","b","a","c","ba"]
    uni=set(raw)
    my_set.remove("ba")

    print(uni & my_set)
    print(uni - my_set)


class M:
    my_map={"math":100,"sst":50}
    print(my_map)
    my_map["S"]=23
    print(my_map)
    print("S" in my_map)
    del my_map["S"]
    print(my_map)

