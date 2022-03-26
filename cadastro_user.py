# import random
# 
# email = "vickcastro@gmail.com"
# entrada_do_usuario = input("Digite seu email:")
# 
# if entrada_do_usuario == email:
#     print("Email correto")
# else:
#     print("Email incorreto")

import json
    
arquivo = open("db.csv", "a")

json.dump("elefantebranco", arquivo)


arquivo.close()