#####Bibliotecas

from tkinter import *
from tkinter import messagebox
import customtkinter

####DESIGN
customtkinter.set_appearance_mode("Dark")
root = customtkinter.CTk()
root.geometry("500x300") 
root.title("EcoCarbon")
root.iconbitmap('logo.ico')
logo = PhotoImage(file="imagens\lg.png")
logo = logo.subsample(5,5)
imagen1 = Label(image=logo, bg="#363636")
imagen1.place(x=10,y=10)




#####textos

texto1 = customtkinter.CTkLabel(root,text="Ecocarbon Calculadora", font=('Arial', 30) ).place(relx=0.5, rely=0.1, anchor=CENTER)
texto2 = customtkinter.CTkLabel(root,text="Selecione o combustível utilizado pelo veículo", font=('Arial', 18) ).place(relx=0.5, rely=0.4, anchor=CENTER)
texto3 = customtkinter.CTkLabel(root,text="DIGITE O KM QUE DESEJA PERCORRER", font=('Arial', 16) ).place(relx=0.5, rely=0.65, anchor=CENTER)

#### ENTRADA DE DADOS
ent1 = customtkinter.CTkEntry(root,placeholder_text="DIGITE O KM")
ent1.pack(padx=10, pady=10)
ent1.place(relx=0.5, rely=0.75, anchor=CENTER)

######combobox
cmb = customtkinter.CTkComboBox(root, values=["Gasolina","Diesel","Etanol","Elétrico"])
cmb.place(relx=0.5, rely=0.5, anchor=CENTER)
cmb.set("Gasolina")



####Função checkbox

def checkcmbo():
     ###set de const e variaveis
     KM = int(ent1.get())
     co2e = int(ent1.get())  
     compensação_arvores = int ( co2e / 5.85 )
        
     #menssagens e informação     
     MSG=messagebox.showinfo(title=(f'RESULTADO DA EMISSÃO'), message=f'Foram emitidos em {KM} KM aproximadamente {co2e} KG de CO2')
     info=messagebox.showinfo(title=("Compensação"), message=f'Seria Necessário o plantio de {compensação_arvores} árvores para compensar o CO2 emitido.')

     if cmb.get() == "Gasolina":
         co2e =int( KM * 2.2 * 1) 
         print(co2e)
         MSG
         info
         
         

     elif cmb.get() == "Diesel":
         co2e = int ( KM * 2.6 * 1 )
         print(co2e)

         MSG
         info
         

 
     elif cmb.get() == "Etanol":
         co2e = int (KM * 1.5 * 1)
         print(co2e)
         MSG
         info


         

     elif cmb.get() == "Elétrico":
         co2e = int (KM * 0.0426 * 1)
         print(co2e)
         MSG
         info

         

     elif cmb.get() == "":
               print("SELECIONE UMA EMISSÃO")
               messagebox.showerror("SELECIONE UMA EMISSÃO", "SELECIONE UMA EMISSÃO")




##Botão da função

btn = customtkinter.CTkButton(root, text="Calcular",command=checkcmbo)
btn.pack(padx=10, pady=10)
btn.place(relx=0.5, rely=0.9, anchor=CENTER)







root.mainloop()





 
#programa de calculo de emissões e compensações de carbono de veiculos


#FÓRMULA DE EMISSÃO = KM * 2.212 * 1

#gasolina 2.212
#ETANOL 1.5
#DIESEL 2.603
#ELETRICO 0.0426

# Referencias da fórmula e calculos do programa:

#https://carbonfreebrasil.com/


# Referencia de codigo

#https://youtu.be/i24MxljM-Bw?si=NAIo4N-vzLRyQqKC


