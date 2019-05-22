from cube import *
import copy

c = Cube()

actions = ["U", "D", "L", "R", "B", "F"
        ,"U'", "D'", "L'", "R'", "B'", "F'"]

def find_all(pat_len):

    if pat_len==1:
        return actions
    else:
        o = find_all(pat_len-1)
    res = []
    for i in o:
        for a in actions:
            res.append(i+a)
    return res

if __name__ == "__main__":
    print("Find your commands!")
    print("v1 - Only using UDLRBFU'D'L'R'B'F'")

    print("1. Input initial condition")
    print("Select input mode:")
    print("0. Basic(X*), 1. Script, 2. Manual Data set")
    s = input()
    if s=="": in_scr = "X*"
    if s=="1": in_mode = 1
    elif s =="2": in_mode = 2
    else: in_mode = 0; in_scr = "X*"

    if in_mode == 1:
        print("Type initial Script to execute at initial condition.")
        in_scr = input()
    elif in_mode == 2:
        print("Type Data of bit cells as decimal, divided by space")
        in_bc = input()
        in_val = in_bc.split(" ")
        for i in range(len(in_val)):
            in_val[i] = int(in_val[i])
        while len(in_val)<6:
            in_val.append(0)
        print("Inputed values:", in_val)

    print("\n")
    print("2. Set Final Condition")
    print("Input desired plane, O. Output")
    in_p = 0
    v = input()
    if v in ["", "O", "Output"]: in_p = 5
    else: in_p = int(v)
    print("Input desired value")
    in_des = int(input())
    print("Target: %d at Plane %d"%(in_p,in_des))

    print("\n")
    print("3. Set Simualtion Length")
    print("Set Max Pattern Length, 0 to inf")
    s = input()
    if s == "": in_m = 99
    else: in_m = int(input())

    # Find everything!
    pat_len = 1
    ans = ""
    cnt = 0
    while pat_len <= in_m and ans == "":
        e = find_all(pat_len)
        print("Pattern Length %d: Total pattern count:%d"%(pat_len,len(e)))

        for item in e:
            # print(item)
            cubes = Cubes(-1, False)
            if in_mode == 0:
                cubes.execute("X*"+item)
            elif in_mode == 1:
                cubes.execute(in_scr+item)
            elif in_mode == 2:
                for i in range(6):
                    cubes.cube.cell_data[i] = in_val[i]
                cubes.execute("*"+item)

            cnt += 1
            if cnt% 100000 == 0:
                print("Checked %d patterns"%cnt)

            if cubes.cube.make_num(in_p) == in_des:
                ans = item
                break
        pat_len += 1
    print(ans)
