import numpy as np

CUBE_TXT = ["I","0","|","&","~","O"]

class Cube:
    def __init__(self):
        self.hyper_in  = None
        self.hyper_out = None

        self.cell_data = np.zeros(6,dtype="uint8")
        self.cell_bit  = np.zeros((6,8),dtype="uint8")
        self.cell_core = 0
        self.static_one()

    def pl(self, idx):
        return [ " %s %3d%3d%3d"%(CUBE_TXT[idx],self.cell_bit[idx,6],self.cell_bit[idx,7],self.cell_bit[idx,0])
                ," | %3d%3d%3d"%(self.cell_bit[idx,5],self.cell_data[idx]  ,self.cell_bit[idx,1])
                ," | %3d%3d%3d"%(self.cell_bit[idx,4],self.cell_bit[idx,3],self.cell_bit[idx,2])]
    def show(self):
        print("Core Cell: %d"%self.cell_core)
        for i in range(3):
            print(" "*12+self.pl(0)[i])
        for i in range(3):
            print(self.pl(3)[i]+self.pl(1)[i]+self.pl(2)[i]+self.pl(4)[i])
        for i in range(3):
            print(" "*12+self.pl(5)[i])
        print()

    def make_num(self, p): # make binary number
        d = 0
        for ind in range(8): d += self.cell_bit[p,ind] << ind
        return d
    def save_plane(self, p):        # Only callable from save
        self.cell_data[p] = 0
        for ind in range(8): self.cell_data[p] += self.cell_bit[p,ind] << ind
    def load_plane(self, p):        # Only callable from load
        for ind in range(8): self.cell_bit[p,ind] = (self.cell_data[p] >> ind )& 1
    def static_one(self): self.cell_data[1] = 1    # Make One as one

    def clear(self, p=0):                   # ?C
        if p==0:
            for i in range(6): self.cell_data[i] = 0
        else: self.cell_data[p] = 0
        self.static_one()
    def save(self, p=0):
        if p==0:                            # ?=
            for i in range(6): self.save_plane(i)
        else: self.save_plane(i)
        self.static_one()
    def load(self, p=0):                    # ?*
        if p==0:
            for i in range(6): self.load_plane(i)
        else: self.load_plane(i)
    def execute(self, p=0):                 # X
        self.cell_data[2] = self.cell_data[2] & self.make_num(2)
        self.cell_data[3] = self.cell_data[3] | self.make_num(3)
        self.cell_data[4] = ~self.make_num(4)
    def input(self, v): self.cell_data[0] = v      # I
    def output(self): return self.cell_data[5]     # P
    def rotate(self, d): # UDBFLR/U'D'B'F'L'R'/udbflr/u'd'b'f'l'r'/MSE/M'S'E'
        # print("Rotating %s"%d)
        if   d=="U" or d=="d" : self.rotate_plane(0, 0); self.rotate_line(0, 0, 0)
        elif d=="U'"or d=="d'": self.rotate_plane(0, 1); self.rotate_line(0, 0, 1)
        elif d=="D" or d=="u" : self.rotate_plane(5, 0); self.rotate_line(5, 0, 0)
        elif d=="D'"or d=="u'": self.rotate_plane(5, 1); self.rotate_line(5, 0, 1)
        elif d=="B" or d=="f" : self.rotate_plane(4, 0); self.rotate_line(4, 0, 0)
        elif d=="B'"or d=="f'": self.rotate_plane(4, 1); self.rotate_line(4, 0, 1)
        elif d=="F" or d=="b" : self.rotate_plane(1, 0); self.rotate_line(1, 0, 0)
        elif d=="F'"or d=="b'": self.rotate_plane(1, 1); self.rotate_line(1, 0, 1)
        elif d=="L" or d=="r" : self.rotate_plane(3, 0); self.rotate_line(3, 0, 0)
        elif d=="L'"or d=="r'": self.rotate_plane(3, 1); self.rotate_line(3, 0, 1)
        elif d=="R" or d=="l" : self.rotate_plane(2, 0); self.rotate_line(2, 0, 0)
        elif d=="R'"or d=="l'": self.rotate_plane(2, 1); self.rotate_line(2, 0, 1)
        elif d=="M" : self.rotate("R"); self.rotate("L'")
        elif d=="M'": self.rotate("R'"); self.rotate("L")
        elif d=="S" : self.rotate("F'"); self.rotate("B")
        elif d=="S'": self.rotate("F"); self.rotate("B'")
        elif d=="E" : self.rotate("U"); self.rotate("D'")
        elif d=="E'": self.rotate("U'"); self.rotate("D")


    def rotate_plane(self, p, d=0): # 0:clockwise
        t1 = self.cell_bit[p,0]; t2 = self.cell_bit[p,1]
        if d==0:
            self.cell_bit[p,0] = self.cell_bit[p,6]; self.cell_bit[p,1] = self.cell_bit[p,7]
            self.cell_bit[p,6] = self.cell_bit[p,4]; self.cell_bit[p,7] = self.cell_bit[p,5]
            self.cell_bit[p,4] = self.cell_bit[p,2]; self.cell_bit[p,5] = self.cell_bit[p,3]
            self.cell_bit[p,2] = t1          ; self.cell_bit[p,3] = t2
        else:
            self.cell_bit[p,0] = self.cell_bit[p,2]; self.cell_bit[p,1] = self.cell_bit[p,3]
            self.cell_bit[p,2] = self.cell_bit[p,4]; self.cell_bit[p,3] = self.cell_bit[p,5]
            self.cell_bit[p,4] = self.cell_bit[p,6]; self.cell_bit[p,5] = self.cell_bit[p,7]
            self.cell_bit[p,6] = t1          ; self.cell_bit[p,7] = t2

    def rotate_line(self, p, l, d=0):
        t = np.zeros(3,dtype="int")
        pp = [1, 2, 4, 3]
        pi = [[6, 7, 0], [6, 7, 0], [6, 7, 0], [6, 7, 0]]
        if   p==0 or p==5:
            if p == 5: p = 0; l = 0 if l == 2 else 2; d = 0 if d == 1 else 1
            if d == 0:   pp = [1, 2, 4, 3]
            else:        pp = [3, 4, 2, 1]
            if   l == 0: pi = [[6, 7, 0], [6, 7, 0], [6, 7, 0], [6, 7, 0]]
            elif l == 2: pi = [[4, 3, 2], [4, 3, 2], [4, 3, 2], [4, 3, 2]]
            else: return None
        elif p==1 or p==4:
            if p == 4: p = 1; l = 0 if l == 2 else 2; d = 0 if d == 1 else 1
            if   d == 0 and l == 0:
                pp = [0, 2, 5, 3]; pi = [[2, 3, 4], [4, 5, 6], [6, 7, 0], [0, 1, 2]]
            elif d == 0 and l == 2:
                pp = [0, 2, 5, 3]; pi = [[6, 7, 0], [0, 1, 2], [2, 3, 4], [4, 5, 6]]
            elif d == 1 and l == 0:
                pp = [0, 3, 5, 2]; pi = [[2, 3, 4], [0, 1, 2], [6, 7, 0], [4, 5, 6]]
            elif d == 1 and l == 2:
                pp = [0, 3, 5, 2]; pi = [[6, 7, 0], [4, 5, 6], [2, 3, 4], [0, 1, 2]]
            else: return None
        elif p==2 or p==3:
            if p == 3: p = 2; l = 0 if l == 2 else 2; d = 0 if d == 1 else 1
            if d == 0:   pp = [4, 0, 1, 5]
            else:        pp = [4, 5, 1, 0]
            if   l == 0: pi = [[4, 5, 6], [0, 1, 2], [0, 1, 2], [0, 1, 2]]
            elif l == 2: pi = [[0, 1, 2], [4, 5, 6], [4, 5, 6], [4, 5, 6]]
            else: return None

        for ind in range(3): t[ind]                    = self.cell_bit[pp[0],pi[0][ind]]
        for ind in range(3): self.cell_bit[pp[0],pi[0][ind]] = self.cell_bit[pp[1],pi[1][ind]]
        for ind in range(3): self.cell_bit[pp[1],pi[1][ind]] = self.cell_bit[pp[2],pi[2][ind]]
        for ind in range(3): self.cell_bit[pp[2],pi[2][ind]] = self.cell_bit[pp[3],pi[3][ind]]
        for ind in range(3): self.cell_bit[pp[3],pi[3][ind]] = t[ind]

CONFIG_DEBUG = 2
CONFIG_CUBE = False
CONFIG_STEP = False

c_list = list()
rot_list = ["U", "D", "L", "R", "F", "B", "u", "d", "l", "r", "f", "b", "M", "S", "E"]
ind_list = ["0", "1", "2", "3", "4", "5", "6"]

def printd(s, m = 0):
    if CONFIG_DEBUG >= 0:
        print(s)

def create_cube(c, d = "in"):
    new_c = Cube()
    if d == "in":
        new_c.hyper_out = c
        c.hyper_in = new_c
        c_list.append(new_c)
    else:
        new_c.hyper_in = c
        c.hyper_out = new_c
        c_list.append(new_c)
    return new_c

if __name__ == "__main__":
    str_input = ""
    # str_input = "I*LR'FFBBLR'DD=P" # Basic input to output
    # str_input = "*R=[{}]}{" # Basic hypercube example
    str_input = "*RU=!(-U)R'RR" # Basic if statement
    print("Script Loaded Length %d"%len(str_input))
    printd(str_input)
    str_index = 0
    par_stack = list()
    c = Cube()
    c_list.append(c)

    while str_index < len(str_input):
        s = str_input[str_index]
        if s in rot_list:
            if str_index+1 < len(str_input) and str_input[str_index+1] == "'":
                printd("%s: Rotate"%str_input[str_index:str_index+2])
                c.rotate(str_input[str_index:str_index+2])
                str_index += 1
            else:
                printd("%s: Rotate"%s)
                c.rotate(s)
        elif s in ind_list:
            printd("%s Number inputed"%s) # Still making
        elif s == "I":
            a = input()
            printd("%s: Input:%s"%(s,a[0]))
            c.input(ord(a[0]))
        elif s == "P":
            printd("%s: Output"%s)
            print(chr(c.output()),end="")
            printd("")
        elif s == "X": printd("%s: Execute"%s); c.execute()
        elif s == "*": printd("%s: Load"%s); c.load()
        elif s == "=": printd("%s: Save"%s); c.save()
        elif s == "C": printd("%s: Clear"%s); c.clear()
        elif s == "(":
            if c.cell_core != 0:
                printd("%s: If open, Core Cell is Not Zero:%d"%(s,c.cell_core))
                # par_stack.append(str_index+1)
            else:
                printd("%s: If open, Core Cell is Zero"%s)
                loc = str_index+1
                level = 0
                # Need to converted into stack... for awesomeness
                while loc < len(str_input):
                    if str_input[loc] == "(": level += 1
                    elif str_input[loc] == ")":
                        if level > 0: level -= 1
                        else: break
                    loc += 1
                str_index = loc
        elif s == ")":
            if c.cell_core != 0:
                printd("%s: If close, Core Cell is Not Zero:%d"%(s,c.cell_core))
                loc = str_index-1
                level = 0
                # Need to converted into stack... for awesomeness
                while loc > 0:
                    if str_input[loc] == ")": level += 1
                    elif str_input[loc] == "(":
                        if level > 0: level -= 1
                        else: break
                    loc -= 1
                str_index = loc
            else:
                printd("%s If close, Core Cell is Zero"%s)
                # par_stack.append(str_index+1)
        elif s == "!": printd("%s: Core <- Input"%s); c.cell_core = c.cell_data[0]
        elif s == "-": printd("%s: Core -1"%s); c.cell_core -= 1
        elif s == "+": printd("%s: Core +1"%s); c.cell_core += 1
        elif s == "[":
            printd("%s: Move to inner Hypercube From %s"%(s,str(c)))
            if c.hyper_in == None: new_c = create_cube(c, "in")
            else: new_c = c.hyper_in
            c = new_c
        elif s == "]":
            printd("%s: Move to outer Hypercube From %s"%(s,str(c)))
            if c.hyper_out == None: new_c = create_cube(c, "out")
            else: new_c = c.hyper_out
            c = new_c
        elif s == "{":
            printd("%s: Send data to inner Hypercube"%s)
            if c.hyper_in == None: new_c = create_cube(c, "in")
            for i in range(6):
                new_c.cell_data[i] = c.cell_data[i]
        elif s == "}":
            printd("%s: Send data to outer Hypercube"%s)
            if c.hyper_out == None: new_c = create_cube(c, "out")
            for i in range(6):
                new_c.cell_data[i] = c.cell_data[i]
        else:
            printd("%s: Unrecognized Character",s)
            pass
        # for i in c_list:
            # print("%s << %s << %s"%(str(i.hyper_in),str(i),str(i.hyper_out)))
        if CONFIG_CUBE:
            c.show()
        if CONFIG_STEP:
            input()
        str_index += 1

    # for i in range(6):
        # for j in range(8):
            # c.da[i,j] = i*10+j
