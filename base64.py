import base64

#petit programme pour me familiariser avec le Python, s/o le Ruby
print("\nBase64\n[~] Veuillez choisir une option :")
choix = input()

if(choix == "encode"):
    print("Veuillez entrer votre chaine que vous voulez encoder :")
    chaine = input().encode()
    print(base64.b64encode(chaine))

elif(choix == "decode"):
    print("Veuillez entrer votre chaine que vous voulez décoder :")
    chaine = input()
    print(base64.b64decode(chaine))
    
else:
    print("\nChoisisser entre encode & décode")
