import numpy as np


def main():
    inst = np.genfromtxt("doc/instances.txt",dtype = int)
    inst_temp=inst[0]
    res=[1,0,1,0,0,1]
    score=2
    export(inst_temp, res, score)
    
def export(inst_temp,res,score):
    nom_fic= "res_N{0}_K{1}_Score{2}".format(inst_temp[0],inst_temp[1],score)
    with open(nom_fic,"w") as fic:
        fic.write("\n".join(",".join(map(str, x)) for x in (inst_temp,res)))
        
        
if __name__ == "__main__":
    main()
    

    
    