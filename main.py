import numpy as np

class Cube:
    def __init__(self):
        self.hb = None
        self.hf = None
        
        self.dc = np.zeros(6,dtype="int8")
        self.da = np.zeros((6,8),dtype="int8")
        self.static_one()

    def pl(self, idx):
        return [ "%3d%3d%3d"%(self.da[idx,6],self.da[idx,7],self.da[idx,0])
                ,"%3d%3d%3d"%(self.da[idx,5],self.dc[idx]  ,self.da[idx,1])
                ,"%3d%3d%3d"%(self.da[idx,4],self.da[idx,3],self.da[idx,2])]
    def show(self):
        for i in range(3):
            print(" "*9+self.pl(0)[i])
        for i in range(3):
            print(self.pl(3)[i]+self.pl(1)[i]+self.pl(2)[i]+self.pl(4)[i])
        for i in range(3):
            print(" "*9+self.pl(5)[i])
        print()

    def make_num(self, p): # make binary number
        d = 0
        for ind in range(8): d += self.da[p,ind] << ind
        return d
    def sp(self, p):        # Only callable from save
        self.dc[p] = 0
        for ind in range(8): self.dc[p] += self.da[p,ind] << ind
    def lp(self, p):        # Only callable from load
        for ind in range(8): self.da[p,ind] = (self.dc[p] >> ind )& 1
    def static_one(self): self.dc[1] = 1    # Make One as one
    
    def clear(self, p=0):                   # ?C
        if p==0:
            for i in range(6): self.dc[i] = 0
        else: self.dc[p] = 0
        self.static_one()
    def save(self, p=0):
        if p==0:                            # ?=
            for i in range(6): self.sp(i)
        else: self.sp(i)
        self.static_one()
    def load(self, p=0):                    # ?*
        if p==0:
            for i in range(6): self.lp(i)
        else: self.lp(i)
    def execute(self, p=0):                 # X
        self.dc[2] = self.dc[2] & d
        self.dc[3] = self.dc[3] | d
        self.dc[4] = self.dc[4] ^ d
    def input(self, v): self.dc[0] = v      # I
    def output(self): return self.dc[5]     # P
    def rotate(self, d): # UDBFLR/U'D'B'F'L'R'/udbflr/u'd'b'f'l'r'/MSE/M'S'E'
        # print("Rotating %s"%d)
        if   d=="U" or d=="d" : self.rp(0, 0); self.rl(0, 0, 0)
        elif d=="U'"or d=="d'": self.rp(0, 1); self.rl(0, 0, 1)
        elif d=="D" or d=="u" : self.rp(5, 0); self.rl(5, 0, 0)
        elif d=="D'"or d=="u'": self.rp(5, 1); self.rl(5, 0, 1)
        elif d=="B" or d=="f" : self.rp(4, 0); self.rl(4, 0, 0)
        elif d=="B'"or d=="f'": self.rp(4, 1); self.rl(4, 0, 1)
        elif d=="F" or d=="b" : self.rp(1, 0); self.rl(1, 0, 0)
        elif d=="F'"or d=="b'": self.rp(1, 1); self.rl(1, 0, 1)
        elif d=="L" or d=="r" : self.rp(3, 0); self.rl(3, 0, 0)
        elif d=="L'"or d=="r'": self.rp(3, 1); self.rl(3, 0, 1)
        elif d=="R" or d=="l" : self.rp(2, 0); self.rl(2, 0, 0)
        elif d=="R'"or d=="l'": self.rp(2, 1); self.rl(2, 0, 1)
        elif d=="M" : self.rotate("R"); self.rotate("L'")
        elif d=="M'": self.rotate("R'"); self.rotate("L")
        elif d=="S" : self.rotate("F'"); self.rotate("B")
        elif d=="S'": self.rotate("F"); self.rotate("B'")
        elif d=="E" : self.rotate("U"); self.rotate("D'")
        elif d=="E'": self.rotate("U'"); self.rotate("D")


    def rp(self, p, d=0): # 0:clockwise
        t1 = self.da[p,0]; t2 = self.da[p,1]
        if d==0:
            self.da[p,0] = self.da[p,6]; self.da[p,1] = self.da[p,7]
            self.da[p,6] = self.da[p,4]; self.da[p,7] = self.da[p,5]
            self.da[p,4] = self.da[p,2]; self.da[p,5] = self.da[p,3]
            self.da[p,2] = t1          ; self.da[p,3] = t2
        else:
            self.da[p,0] = self.da[p,2]; self.da[p,1] = self.da[p,3]
            self.da[p,2] = self.da[p,4]; self.da[p,3] = self.da[p,5]
            self.da[p,4] = self.da[p,6]; self.da[p,5] = self.da[p,7]
            self.da[p,6] = t1          ; self.da[p,7] = t2
    
    def rl(self, p, l, d=0):
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
        
        for ind in range(3): t[ind]                    = self.da[pp[0],pi[0][ind]]
        for ind in range(3): self.da[pp[0],pi[0][ind]] = self.da[pp[1],pi[1][ind]]
        for ind in range(3): self.da[pp[1],pi[1][ind]] = self.da[pp[2],pi[2][ind]]
        for ind in range(3): self.da[pp[2],pi[2][ind]] = self.da[pp[3],pi[3][ind]]
        for ind in range(3): self.da[pp[3],pi[3][ind]] = t[ind]

CONFIG_DEBUG = 1

c = Cube()

def printd(s, m = 0, sc = False):
    if CONFIG_DEBUG >= 0:
        print(s)
    if sc:
        c.show()

if __name__ == "__main__":
    
    str_input = "I*LR'FFBBLR'DD=P"
    print("Script Loaded")
    printd(str_input)
    rot_list = ["U", "D", "L", "R", "F", "B", "u", "d", "l", "r", "f", "b", "M", "S", "E"]
    ind_list = ["0", "1", "2", "3", "4", "5", "6"]
    str_index = 0

    while str_index < len(str_input):
        if str_input[str_index] in rot_list:
            if str_index+1 < len(str_input) and str_input[str_index+1] == "'":
                printd("Rotate: %s"%str_input[str_index:str_index+2])
                c.rotate(str_input[str_index:str_index+2])
                str_index += 1
            else:
                printd("Rotate: %s"%str_input[str_index])
                c.rotate(str_input[str_index])
        elif str_input[str_index] in ind_list:
            printd("Number inputed") # Making
        elif str_input[str_index] == "I":
            a = input()
            printd("Input: %s"%a[0])
            c.input(ord(a[0]))
        elif str_input[str_index] == "P":
            printd("Output: ")
            print(chr(c.output()),end="")
            printd("")
        elif str_input[str_index] == "X":
            printd("Execute")
            c.execute()
        elif str_input[str_index] == "*":
            printd("Load")
            c.load()
        elif str_input[str_index] == "=":
            printd("Save")
            c.save()
        elif str_input[str_index] == "C":
            printd("Clear")
            c.clear()
        elif str_input[str_index] == "{":
            printd("Move to previous Hypercube")
        elif str_input[str_index] == "}":
            printd("Move to next Hypercube")
        elif str_input[str_index] == "[":
            printd("Send center data to previous Hypercube")
        elif str_input[str_index] == "]":
            printd("Send center data to next Hypercube")
        else:
            printd("Unrecognized Character")
            pass
        str_index += 1
    
    # for i in range(6):
        # for j in range(8):
            # c.da[i,j] = i*10+j
