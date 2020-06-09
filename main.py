import numpy as np

def main():
    inst = np.genfromtxt("doc/instances.txt",dtype = int)
    fonction_aleatoire(inst)

def fonction_aleatoire(inst):
    for inst_temp in inst:
        res = genere(inst_temp[0])
        score = trouve_score((inst_temp),res)
        export(inst_temp, res, score)
    
def genere(taille):
    rand = np.random.randint(2, size=taille)
    rand[rand==0]=-1
    return rand
    print(rand)
    
    
def export(inst_temp,res,score):
    nom_fic= "res/res_N{0}_K{1}_S{2}.csv".format(inst_temp[0],inst_temp[1],score)
    with open(nom_fic,"w") as fic:
        fic.write("\n".join(",".join(map(str, x)) for x in (inst_temp,res)))

def trouve_score(inst_temp,prop):
    N=inst_temp[0]
    K=inst_temp[1]
    score = 0
    i = 0
    niv = 2 #Boucle sur les niv
    inter = 0#Boucle sur les intéractions
    while niv<K+1: #Tant qu'on a pas atteint le niv
        print(f"niv :{niv}")
        while (i+niv-1)<N: #Tant qu'on est dnas le tableau
            inter += prop[i]*prop[i+niv-1]
            print(f"pos{i}, mul:{prop[i]*prop[i+niv-1]}")
            i += 1 #Se déplace dans le tableau
        print(f"inter:{inter}")
        score += inter**2
        inter = 0
        i=0
        niv += 1
    print(f"score: {score}")
    return score
        
        
if __name__ == "__main__":
    main()
    

    
    