###Code exemple, à adapter!!!###

"""
Ce code sauvegarde en format csv (valeurs séparées par des virgules), mais ce n'est pas ce que le prof veux... à modifié.  (Ainsi que l'adapter au orienté-objet?)

Le save_check() pourrait être enlevé puisque l'utilisateur pointera le programme au bon fichier de sauvegarde (il peux en avoir plusieurs).  

Idée: Quand l'utilisateur vas pointer au fichier de sauvegarde à charger ou bien pour savegardé, le path de <os.sys.path.append(...)> sera modifié.

"""

os.sys.path.append(r'/home/python/rpg/sorcerer')


def save_check():                            #Verifies if the save file is empty
    if os.stat("save.csv").st_size==0:       #or not
        save();
    else:
        load();
    

def save():
    save = {}
    save["check"] = test
    w = csv.writer(open("save.csv", "w"))
    for key, val in save.items():
        w.writerow([key, val])



def load():                                         #Allows the program to
    save = {}                                       #"jump" to whereever the user
    for key, val in csv.reader(open("save.csv")):   #is at in the game based on
        save[key] = val                             #the value of location in
                                                    #save.csv (homebrew switch-
                                                    #case statement)
    location = {"0" : front,
                "1" : post_sorting
               }
    
    location[save.get('location')]()    
