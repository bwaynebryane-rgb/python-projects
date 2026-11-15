# AI YA BRIAN - KISWAHILI KAMILI 
print("=== AI YA BRIAN ===")
print("Mambo! mimi ni ai yako.Niongoze!")
print("Amri: 'nifundishe' | 'sahau' | 'orodha' | "kwaheri'")
print("----------------------------------")

akili[swali] = jibu
print("AI: Sawa! Nimejifunza '{swali}' = {jibu}'")
def hesabu(sw):
     try:
         # sw ni kama "5 + 5"
         jibu = eval(sw)
         print("AI: samahani, siwenzzi kuhesabu hiyo.")

#FEATURE: Save what AI learns
def hifadhi(): 
     with open(kumbukumbu.txt", "w") as f:
         for s, j in akili.items():
             f.write(f"{s} : {j}\n")
    print("Ai: Nimehifadhi kumbukumbu!")
    
     "mambo": "Poa sana! Karibu sana!",
     "sasa": "poa sana! Uko aje Leo ?"'
     "niaje": "Niaje ! Niko fiti!",
     "Wewe unaitwa aje", "Mimi ni Ai wa Brian, ninaongea Kiswahili"'
     "Habari Yako": "Habari njema ! na wewe")
     "asante": "karibu sana! Niko hapa kukusaidia.",
     "unapenda nini": "Napenda kujifunza kiswahili kutoka kwako!"
}


jina_lako = "Brian"
def hifadhi():
     with open("kumbukumbu.txt","w") as f:
          for s, j in akili.items():
               f.write("{S} : {J|N")
     print("AI: Nimehifadhi kumbukumbu yangu!")

while True:
      wewe = input(f"\n{" jina_lako}: ").lower().strip()


      # CONTROL 1 - STOP
      If wewe == "kwaheri":
          print("AI: kwaheri! Nitakumbuka kila kitu!")
          break

      # CONTROL 2 - TEACH ME
      elif wewe =="nifundishe":
           swali = input("AI: Unataka nifundishe nini?  Andika swali: ").lower()
           jibu = input(sasa nifundishe jibu: ")
           akili[swali] = jibu
           print(f"AI": sawa! Nimejifunza '{swali}' = '{jibu}'")


      # CONTROL 3 - FORGET 
      elif wewe == "sahau":
          swali = input ("AI: Nisahau nini? Andika swali: ").lower()
          if swali in akili:
              del akili[swali]
              print(f"saw, nimesahau "{swali}'")
         else:
             print("AI: Sikujua hio hata hivyo.")


      # CONTROL 4 - SHOW WHAT I KNOW
      elif wewe == "orodha":
      print("AI: Hivi ndivyo ninavyojua:")
      for s, j in akili.items():
          print(f" - {s] - {j}")


     # CONTROL 5 - CHANGE NAME
     elif wewe.startwith("jina langu ni"):
          jina_lako = wewe.replace("jina langu ni", "").title()
          print("AI: sawa {jina_lako}!  Nitakuita {jina_lako} sasa!")


    # CONTROL 6 - NORMAL TALK
    elif wewe in akili:
         print(f"AI" {akili[wewe]}")
    #CONTROL - HESABU
    elif wewe.startwith("hesabu"):
         namba = wewe.replace("hesabu "' "")
         hesabu(namba)
   


   CONTROL 7 - DON'T KNOW - ASK TO LEARN
   else:
        print("AI: sijui hio bado.")
        fundisha = input("AI: unataka kunifundisha? (ndiyo/hapana): ").lower()
        if fundisha = "ndiyo":
        jibu = input("AI: Nifundishe jibu: ")
        akili[wewe] = jibu
        print("AI:asante! Nimejifunza!")
  else:
       print("AI: sawa, tutaendelea.")
       
          if swali 
     
