
class Nodo:
    def __init__(self):                      # t es el grado minimo del arbol
        self.hijos = []
        self.keys = []
        self.hoja = True
        self.n = 0

class ArbolB:
    def __init__(self, t):
        self.t = t
        self.root = None                                # Se inicia sin raiz

    def bTreeCreate(self):                              # Se crea el arbol
        if self.root == None:
            self.root = Nodo(self.t)
        return self.root

    def Insert(self, k):
        root = self.root
        if root.n == 2 * self.t - 1:
            s = Nodo(self.t)
            self.root = s
            s.hoja = False
            s.n = 0
            s.hijos[1] = root
            self.Split_hijos(s, 1)
            self.insertar_no_lleno(s, k)
        else:
            self.insertar_no_lleno(root, k)

    # Split
    def Split(self, x, i):
        t = self.t
        y = x.hijos[i]
        z = t(y.hoja)
        x.hijos.insert_key(i + 1, z)
        x.keys.insert_key(i, y.keys[t - 1])
        z.keys = y.keys[t: (2 * t) - 1]
        y.keys = y.keys[0: t - 1]
        if not y.hoja:
            z.hijos = y.hijos[t: 2 * t]
            y.hijos = y.hijos[0: t - 1]

    def Split_hijos(self, x, t):
        z = self.root
        y = x.hijos[t]
        z.hoja = y.hoja
        z.n = t - 1
        for j in self.t - 1:
            z.keys[j] = y.keys[j + t]
        if y.hoja == False:
            for j in t:
                z.hijos[j] = y.hijos[j + t]
        y.n = t - 1
        for j in x.n + 1:
            x.hijos[j + 1] = x.hijos[j]
        x.keys = y.keys[t]
        x.n = x.n + 1

    def insertar_no_lleno(self, x, k):
        i = x.n
        if x.hoja:
            while i >= 1 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
            x.n = x.n + 1
            #self.writetoDisk(x)
        else:
            while i >= 1 and k < x.keys[i]:
                i -= 1
            i += 1
            #self.readfromDisk(x.hijoern)
            if x.hijos[i].n == (2 * self.t) - 1:
                self.Split_hijos(x, i)
                if k > x.keys(arbol.root.keys[i]):
                    i += 1
            self.insertar_no_lleno(x.hijos[i], k)



    def Search(self, x, k):
        i = 1
        print(x.n)
        print(x.keys[i])
        while i <= x.n and k > x.keys[i]:
            i = i + 1
        if i <= x.n and k > x.keys[i]:
            return(x, i)
        else:
            if x.hoja:
                return None
            else:
                #ReadDisc(x.hijos[i]))
                return self.search(x.childer[i], k)


if __name__ == "__main__":
# 66 84 72 77 79 67
    arbol = ArbolB(2)
    T = arbol.bTreeCreate()
    arbol.Insert(66)
    arbol.Insert(84)
    arbol.Insert(72)
    arbol.Insert(77)
    arbol.Insert(79)
    arbol.Insert(67)
    # for hijos in arbol.root.hijos:
    #     if hijos:
    #         print("hijo")
    #         print(hijos.keys)
    # print("ROOT")
    print(arbol.root.keys)

    # print(arbol.search(arbol.root, 77))
