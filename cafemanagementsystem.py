from tkinter import *
import time
import random
import datetime
import tempfile
import os
import os.path
import tkinter as tk
path='C:\\Users\\Poojita\\Desktop\\New folder'
os.chdir(path)

root=tk.Tk()
root.geometry("1600x800")
root.title("CAFE MANAGEMENT SYSTEM")
#root.iconbitmap(r"C:\Users\Poojita\Desktop\working\practice1\cafemanagementsystem\icon.ico")

tops = Frame(root,width =1600,height=50,relief=RAISED,bd=14)
tops.pack(side=TOP)
label1 = Label(tops,font=('arial',30,'bold'),text="CAFE MANAGEMENT SYSTEM",fg="black",bd=10)
label1.grid(row=0,column=0)
label2 = Label(tops,font=('arial',16,'bold'),text="Name",fg="black",bd=10)
label2.grid(row=0,column=1)
textname=StringVar()
filenamei=StringVar()
labelfilename=Label(tops,text='filename',font=('arial',16,'bold'),fg="black",bd=10)
labelfilename.grid(row=1,column=1)
filename=Entry(tops,font=("arial bold",13),width=25,bd=8,justify=LEFT,textvariable=filenamei)
filename.grid(row=1,column=2)
label1entry=Entry(tops,font=("arial bold",13),width=25,bd=8,justify=LEFT,textvariable=textname)
label1entry.grid(row=0,column=2)

localtime=time.asctime(time.localtime(time.time()))
label1 = Label(tops,font=('arial',15,'bold'),text=localtime,fg="blue",bd=10,anchor=W)
label1.grid(row=1,column=0)

f1 = Frame(root,width =900,height=700,relief=RAISED,bd=14)
f1.pack(side=LEFT)
f11 = Frame(f1,width =900,height=300,relief=SUNKEN,bd=14)
f11.pack(side=TOP)
f11a = Frame(f11,width =450,height=300,relief=SUNKEN,bd=14)
f11a.pack(side=LEFT)
f11b = Frame(f11,width =450,height=300,relief=SUNKEN,bd=14)
f11b.pack(side=RIGHT)
f12 = Frame(f1,width =900,height=300,relief=SUNKEN,bd=14)
f12.pack(side=BOTTOM)
f12a = Frame(f12,width =450,height=300,relief=SUNKEN,bd=14)
f12a.pack(side=LEFT)
f12b = Frame(f12,width =450,height=300,relief=SUNKEN,bd=14)
f12b.pack(side=RIGHT)
f2 = Frame(root,width =700,height=700,relief=SUNKEN,bd=14)
f2.pack(side=RIGHT)
f2a = Frame(f2,width =700,height=500,relief=SUNKEN,bd=14)
f2a.pack(side=TOP)
f2a1 = Frame(f2a,width =700,height=300,relief=SUNKEN,bd=14)
f2a1.pack(side=TOP)
f2a2 = Frame(f2a,width =700,height=200,relief=SUNKEN,bd=14)
f2a2.pack(side=BOTTOM)
f2b = Frame(f2,width =700,height=200,bd=14)
f2b.pack(side=BOTTOM)
#==========================================VARIABLES=====================================
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()
var26=IntVar()
var27=IntVar()
var28=IntVar()
var29=IntVar()
var30=IntVar()
var31=IntVar()
var32=IntVar()
var33=IntVar()
var34=IntVar()
var35=IntVar()
var36=IntVar()
var37=IntVar()
var38=IntVar()
var39=IntVar()
var40=IntVar()
var41=IntVar()
var42=IntVar()
var43=IntVar()
var44=IntVar()
var45=IntVar()
var46=IntVar()
var47=IntVar()
var48=IntVar()
var49=IntVar()
var50=IntVar()
var51=IntVar()
var52=IntVar()
var53=IntVar()
var54=IntVar()
var55=IntVar()
var56=IntVar()
var57=IntVar()
var58=IntVar()
var59=IntVar()
var60=IntVar()
var61=IntVar()
var62=IntVar()
var63=IntVar()
var64=IntVar()
var65=IntVar()
var66=IntVar()
var67=IntVar()

textlussi=IntVar()
textdalgona_coffee=IntVar()
textflat_white=IntVar()
textcappuccino=IntVar()
textexpresso=IntVar()
textcold_coffee=IntVar()
textbutter_milk=IntVar()
textlemonaid=IntVar()
textbutter_cake=IntVar()
textpound_cake=IntVar()
textsponge_cake=IntVar()
textgenoise_cake=IntVar()
textbiscuit_cake=IntVar()
textchiffon_cake=IntVar()
textcarrot_cake=IntVar()
textred_velvet_cake=IntVar()
textorange_juice=IntVar()
textapple_juice=IntVar()
textpineapple_juice=IntVar()
textcarrot_juice=IntVar()
textbeetroot_juice=IntVar()
textbanana_juice=IntVar()
textgrape_juice=IntVar()
textstrawberry_juice=IntVar()
textchocobar=IntVar()
textvannila=IntVar()
textchocolate=IntVar()
textblueberry=IntVar()
textcaramel=IntVar()
textmint=IntVar()
textbig_mix=IntVar()
textbutterscotch=IntVar()
textbouillon_soup=IntVar()
textbroth_soup=IntVar()
textcream_soup=IntVar()
textpotage_soup=IntVar()
textcorn_soup=IntVar()
textsprout_salad=IntVar()
textpasta_salad=IntVar()
textorzo_salad=IntVar()
textkale_salad=IntVar()
textgreek_salad=IntVar()
texthalwa=IntVar()
textkaju_barfi=IntVar()
textladdu=IntVar()
textjilebi=IntVar()
textjangry=IntVar()
textmysore_pak=IntVar()
textpalkova=IntVar()
textkesari=IntVar()
textbadusha=IntVar()
textkalakani=IntVar()
textputarekulu=IntVar()
textrasgulla=IntVar()
textmalai_laddu=IntVar()
texttokkudu_laddu=IntVar()
textpaneer_sandwich=IntVar()
textcheese_sandwich=IntVar()
textgrilled_sandwich=IntVar()
textclub_sandwich=IntVar()
textpotato_sandwich=IntVar()
textmushroom_sandwich=IntVar()
textchocolate_sandwich=IntVar()
textcucumber_sandwich=IntVar()
textcurd_sanwich=IntVar()
textveg_sandwich=IntVar()
#==========================================BUTTONS=======================================
def chkbutton():
    if (var1.get()==1):
        txtlussi.configure(state=NORMAL)
    elif (var1.get()==0):
        txtlussi.configure(state=DISABLED)

    if var2.get()==1:
        txtdalgona_coffee.configure(state=NORMAL)
    elif var2.get()==0:
        txtdalgona_coffee.configure(state=DISABLED)
        
    if var3.get()==1:
        txtflat_white.configure(state=NORMAL)
    elif var3.get()==0:
        txtflat_white.configure(state=DISABLED)

    if var4.get()==1:
        txtcappuccino.configure(state=NORMAL)
    elif var4.get()==0:
        txtcappuccino.configure(state=DISABLED)

    if var5.get()==1:
        txtexpresso.configure(state=NORMAL)
    elif var5.get()==0:
        txtexpresso.configure(state=DISABLED)

    if var6.get()==1:
        txtcold_coffee.configure(state=NORMAL)
    elif var6.get()==0:
        txtcold_coffee.configure(state=DISABLED)

    if var7.get()==1:
        txtbutter_milk.configure(state=NORMAL)
    elif var7.get()==0:
        txtbutter_milk.configure(state=DISABLED)

    if var8.get()==1:
        txtlemonaid.configure(state=NORMAL)
    elif var8.get()==0:
        txtlemonaid.configure(state=DISABLED)

    if var9.get()==1:
        txtbutter_cake.configure(state=NORMAL)
    elif var9.get()==0:
        txtbutter_cake.configure(state=DISABLED)

    if var10.get()==1:
        txtpound_cake.configure(state=NORMAL)
    elif var10.get()==0:
        txtpound_cake.configure(state=DISABLED)
        
    if var11.get()==1:
        txtsponge_cake.configure(state=NORMAL)
    elif var11.get()==0:
        txtsponge_cake.configure(state=DISABLED)

    if var12.get()==1:
        txtgenoise_cake.configure(state=NORMAL)
    elif var12.get()==0:
        txtgenoise_cake.configure(state=DISABLED)

    if var13.get()==1:
        txtbiscuit_cake.configure(state=NORMAL)
    elif var13.get()==0:
        txtbiscuit_cake.configure(state=DISABLED)

    if var14.get()==1:
        txtchiffon_cake.configure(state=NORMAL)
    elif var14.get()==0:
        txtchiffon_cake.configure(state=DISABLED)

    if var15.get()==1:
        txtcarrot_cake.configure(state=NORMAL)
    elif var15.get()==0:
        txtcarrot_cake.configure(state=DISABLED)

    if var16.get()==1:
        txtred_velvet_cake.configure(state=NORMAL)
    elif var16.get()==0:
        txtred_velvet_cake.configure(state=DISABLED)

    if var17.get()==1:
        txtorange_juice.configure(state=NORMAL)
    elif var17.get()==0:
        txtorange_juice.configure(state=DISABLED)

    if var18.get()==1:
        txtapple_juice.configure(state=NORMAL)
    elif var18.get()==0:
        txtapple_juice.configure(state=DISABLED)

    if var19.get()==1:
        txtpineapple_juice.configure(state=NORMAL)
    elif var19.get()==0:
        txtpineapple_juice.configure(state=DISABLED)

    if var20.get()==1:
        txtcarrot_juice.configure(state=NORMAL)
    elif var20.get()==0:
        txtcarrot_juice.configure(state=DISABLED)

    if var21.get()==1:
        txtbeetroot_juice.configure(state=NORMAL)
    elif var21.get()==0:
        txtbeetroot_juice.configure(state=DISABLED)

    if var22.get()==1:
        txtbanana_juice.configure(state=NORMAL)
    elif var22.get()==0:
        txtbanana_juice.configure(state=DISABLED)

    if var23.get()==1:
        txtgrape_juice.configure(state=NORMAL)
    elif var23.get()==0:
        txtgrape_juice.configure(state=DISABLED)

    if var24.get()==1:
        txtstrawberry_juice.configure(state=NORMAL)
    elif var24.get()==0:
        txtstrawberry_juice.configure(state=DISABLED)

    if var25.get()==1:
        txtchocobar.configure(state=NORMAL)
    elif var25.get()==0:
        txtchocobar.configure(state=DISABLED)
        
    if var26.get()==1:
        txtvannila.configure(state=NORMAL)
    elif var26.get()==0:
        txtvannila.configure(state=DISABLED)

    if var27.get()==1:
        txtchocolate.configure(state=NORMAL)
    elif var27.get()==0:
        txtchocolate.configure(state=DISABLED)

    if var28.get()==1:
        txtmint.configure(state=NORMAL)
    elif var28.get()==0:
        txtmint.configure(state=DISABLED)

    if var29.get()==1:
        txtblueberry.configure(state=NORMAL)
    elif var29.get()==0:
        txtblueberry.configure(state=DISABLED)

    if var30.get()==1:
        txtcaramel.configure(state=NORMAL)
    elif var30.get()==0:
        txtcaramel.configure(state=DISABLED)

    if var31.get()==1:
        txtbig_mix.configure(state=NORMAL)
    elif var31.get()==0:
        txtbig_mix.configure(state=DISABLED)
        
    if var32.get()==1:
        txtbutterscotch.configure(state=NORMAL)
    elif var32.get()==0:
        txtbutterscotch.configure(state=DISABLED)
    
    if var33.get()==1:
        txtbouillon_soup.configure(state=NORMAL)
    elif var33.get()==0:
        txtbouillon_soup.configure(state=DISABLED)

    if var34.get()==1:
        txtbroth_soup.configure(state=NORMAL)
    elif var34.get()==0:
        txtbroth_soup.configure(state=DISABLED)

    if var35.get()==1:
        txtcream_soup.configure(state=NORMAL)
    elif var35.get()==0:
        txtcream_soup.configure(state=DISABLED)

    if var36.get()==1:
        txtpotage_soup.configure(state=NORMAL)
    elif var36.get()==0:
        txtpotage_soup.configure(state=DISABLED)

    if var37.get()==1:
        txtcorn_soup.configure(state=NORMAL)
    elif var37.get()==0:
        txtcorn_soup.configure(state=DISABLED)

    if var38.get()==1:
        txtsprout_salad.configure(state=NORMAL)
    elif var38.get()==0:
        txtsprout_salad.configure(state=DISABLED)

    if var39.get()==1:
        txtpasta_salad.configure(state=NORMAL)
    elif var39.get()==0:
        txtpasta_salad.configure(state=DISABLED)

    if var40.get()==1:
        txtorzo_salad.configure(state=NORMAL)
    elif var40.get()==0:
        txtorzo_salad.configure(state=DISABLED)

    if var41.get()==1:
        txtkale_salad.configure(state=NORMAL)
    elif var41.get()==0:
        txtkale_salad.configure(state=DISABLED)

    if var42.get()==1:
        txtgreek_salad.configure(state=NORMAL)
    elif var42.get()==0:
        txtgreek_salad.configure(state=DISABLED)

    if var43.get()==1:
        txthalwa.configure(state=NORMAL)
    elif var43.get()==0:
        txthalwa.configure(state=DISABLED)

    if var44.get()==1:
        txtkaju_barfi.configure(state=NORMAL)
    elif var44.get()==0:
        txtkaju_barfi.configure(state=DISABLED)

    if var45.get()==1:
        txtladdu.configure(state=NORMAL)
    elif var45.get()==0:
        txtladdu.configure(state=DISABLED)

    if var46.get()==1:
        txtjilebi.configure(state=NORMAL)
    elif var46.get()==0:
        txtjilebi.configure(state=DISABLED)

    if var47.get()==1:
        txtjangri.configure(state=NORMAL)
    elif var47.get()==0:
        txtjangri.configure(state=DISABLED)

    if var48.get()==1:
        txtmysore_pak.configure(state=NORMAL)
    elif var48.get()==0:
        txtmysore_pak.configure(state=DISABLED)

    if var49.get()==1:
        txtpalkova.configure(state=NORMAL)
    elif var49.get()==0:
        txtpalkova.configure(state=DISABLED)

    if var50.get()==1:
        txtkesari.configure(state=NORMAL)
    elif var50.get()==0:
        txtkesari.configure(state=DISABLED)

    if var51.get()==1:
        txtbadusha.configure(state=NORMAL)
    elif var51.get()==0:
        txtbadusha.configure(state=DISABLED)

    if var52.get()==1:
        txtkalakani.configure(state=NORMAL)
    elif var52.get()==0:
        txtkalakani.configure(state=DISABLED)

    if var53.get()==1:
        txtputarekulu.configure(state=NORMAL)
    elif var53.get()==0:
        txtputarekulu.configure(state=DISABLED)

    if var54.get()==1:
        txtrasgulla.configure(state=NORMAL)
    elif var54.get()==0:
        txtrasgulla.configure(state=DISABLED)

    if var55.get()==1:
        txtmalai_laddu.configure(state=NORMAL)
    elif var55.get()==0:
        txtmalai_laddu.configure(state=DISABLED)

    if var56.get()==1:
        txttokkudu_laddu.configure(state=NORMAL)
    elif var56.get()==0:
        txttokkudu_laddu.configure(state=DISABLED)

    if var57.get()==1:
        txtpaneer_sandwich.configure(state=NORMAL)
    elif var57.get()==0:
        txtpaneer_sandwich.configure(state=DISABLED)

    if var58.get()==1:
        txtcheese_sandwich.configure(state=NORMAL)
    elif var58.get()==0:
        txtcheese_sandwich.configure(state=DISABLED)

    if var59.get()==1:
        txtgrilled_sandwich.configure(state=NORMAL)
    elif var59.get()==0:
        txtgrilled_sandwich.configure(state=DISABLED)

    if var60.get()==1:
        txtclub_sandwich.configure(state=NORMAL)
    elif var60.get()==0:
        txtclub_sandwich.configure(state=DISABLED)

    if var61.get()==1:
        txtpotato_sandwich.configure(state=NORMAL)
    elif var61.get()==0:
        txtpotato_sandwich.configure(state=DISABLED)

    if var62.get()==1:
        txtmushroom_sandwich.configure(state=NORMAL)
    elif var62.get()==0:
        txtmushroom_sandwich.configure(state=DISABLED)

    if var63.get()==1:
        txtchocolate_sandwich.configure(state=NORMAL)
    elif var63.get()==0:
        txtchocolate_sandwich.configure(state=DISABLED)

    if var64.get()==1:
        txtcucumber_sandwich.configure(state=NORMAL)
    elif var64.get()==0:
        txtcucumber_sandwich.configure(state=DISABLED)

    if var65.get()==1:
        txtcurd_sandwich.configure(state=NORMAL)
    elif var65.get()==0:
        txtcurd_sandwich.configure(state=DISABLED)

    if var66.get()==1:
        txtveg_sandwich.configure(state=NORMAL)
    elif var66.get()==0:
        txtveg_sandwich.configure(state=DISABLED)

def exit():
    root.destroy()
def reset():
    filenamei.set("")
    os.chdir(path)
    textname.set("")
    textentry1.set("0")
    textentry2.set("0")
    textentry3.set("0")

    textlussi.set("0")
    textdalgona_coffee.set("0")
    textflat_white.set("0")
    textcappuccino.set("0")
    textexpresso.set("0")
    textcold_coffee.set("0")
    textbutter_milk.set("0")
    textlemonaid.set("0")
    textbutter_cake.set("0")
    textpound_cake.set("0")
    textsponge_cake.set("0")
    textgenoise_cake.set("0")
    textbiscuit_cake.set("0")
    textchiffon_cake.set("0")
    textcarrot_cake.set("0")
    textred_velvet_cake.set("0")
    textorange_juice.set("0")
    textapple_juice.set("0")
    textpineapple_juice.set("0")
    textcarrot_juice.set("0")
    textbeetroot_juice.set("0")
    textbanana_juice.set("0")
    textgrape_juice.set("0")
    textstrawberry_juice.set("0")
    textchocobar.set("0")
    textvannila.set("0")
    textchocolate.set("0")
    textmint.set("0")
    textblueberry.set("0")
    textcaramel.set("0")
    textbig_mix.set("0")
    textbutterscotch.set("0")
    textbouillon_soup.set("0")
    textbroth_soup.set("0")
    textcream_soup.set("0")
    textpotage_soup.set("0")
    textcorn_soup.set("0")
    textsprout_salad.set("0")
    textpasta_salad.set("0")
    textorzo_salad.set("0")
    textkale_salad.set("0")
    textgreek_salad.set("0")
    texthalwa.set("0")
    textkaju_barfi.set("0")
    textladdu.set("0")
    textjilebi.set("0")
    textjangry.set("0")
    textmysore_pak.set("0")
    textpalkova.set("0")
    textkesari.set("0")
    textbadusha.set("0")
    textkalakani.set("0")
    textputarekulu.set("0")
    textrasgulla.set("0")
    textmalai_laddu.set("0")
    texttokkudu_laddu.set("0")
    textpaneer_sandwich.set("0")
    textcheese_sandwich.set("0")
    textgrilled_sandwich.set("0")
    textclub_sandwich.set("0")
    textpotato_sandwich.set("0")
    textmushroom_sandwich.set("0")
    textchocolate_sandwich.set("0")
    textcucumber_sandwich.set("0")
    textcurd_sanwich.set("0")
    textveg_sandwich.set("0")
    
    

    txtlussi.configure(state=DISABLED)
    txtdalgona_coffee.configure(state=DISABLED)
    txtflat_white.configure(state=DISABLED)
    txtcappuccino.configure(state=DISABLED)
    txtexpresso.configure(state=DISABLED)
    txtcold_coffee.configure(state=DISABLED)
    txtbutter_milk.configure(state=DISABLED)
    txtlemonaid.configure(state=DISABLED)
    txtbutter_cake.configure(state=DISABLED)
    txtpound_cake.configure(state=DISABLED)
    txtsponge_cake.configure(state=DISABLED)
    txtgenoise_cake.configure(state=DISABLED)
    txtbiscuit_cake.configure(state=DISABLED)
    txtchiffon_cake.configure(state=DISABLED)
    txtcarrot_cake.configure(state=DISABLED)
    txtred_velvet_cake.configure(state=DISABLED)
    txtorange_juice.configure(state=DISABLED)
    txtapple_juice.configure(state=DISABLED)
    txtpineapple_juice.configure(state=DISABLED)
    txtcarrot_juice.configure(state=DISABLED)
    txtbeetroot_juice.configure(state=DISABLED)
    txtbanana_juice.configure(state=DISABLED)
    txtgrape_juice.configure(state=DISABLED)
    txtstrawberry_juice.configure(state=DISABLED)
    txtchocobar.configure(state=DISABLED)
    txtvannila.configure(state=DISABLED)
    txtchocolate.configure(state=DISABLED)
    txtmint.configure(state=DISABLED)
    txtblueberry.configure(state=DISABLED)
    txtbig_mix.configure(state=DISABLED)
    txtcaramel.configure(state=DISABLED)
    txtbutterscotch.configure(state=DISABLED)
    txtbouillon_soup.configure(state=DISABLED)
    txtbroth_soup.configure(state=DISABLED)
    txtcream_soup.configure(state=DISABLED)
    txtpotage_soup.configure(state=DISABLED)
    txtcorn_soup.configure(state=DISABLED)
    txtsprout_salad.configure(state=DISABLED)
    txtpasta_salad.configure(state=DISABLED)
    txtorzo_salad.configure(state=DISABLED)
    txtkale_salad.configure(state=DISABLED)
    txtgreek_salad.configure(state=DISABLED)
    txthalwa.configure(state=DISABLED)
    txtkaju_barfi.configure(state=DISABLED)
    txtladdu.configure(state=DISABLED)
    txtjilebi.configure(state=DISABLED)
    txtjangri.configure(state=DISABLED)
    txtmysore_pak.configure(state=DISABLED)
    txtpalkova.configure(state=DISABLED)
    txtkesari.configure(state=DISABLED)
    txtbadusha.configure(state=DISABLED)
    txtkalakani.configure(state=DISABLED)
    txtputarekulu.configure(state=DISABLED)
    txtrasgulla.configure(state=DISABLED)
    txtmalai_laddu.configure(state=DISABLED)
    txttokkudu_laddu.configure(state=DISABLED)
    txtpaneer_sandwich.configure(state=DISABLED)
    txtcheese_sandwich.configure(state=DISABLED)
    txtgrilled_sandwich.configure(state=DISABLED)
    txtclub_sandwich.configure(state=DISABLED)
    txtpotato_sandwich.configure(state=DISABLED)
    txtmushroom_sandwich.configure(state=DISABLED)
    txtchocolate_sandwich.configure(state=DISABLED)
    txtcucumber_sandwich.configure(state=DISABLED)
    txtcurd_sandwich.configure(state=DISABLED)
    txtveg_sandwich.configure(state=DISABLED)

    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)
    var28.set(0)
    var29.set(0)
    var30.set(0)
    var31.set(0)
    var32.set(0)
    var33.set(0)
    var34.set(0)
    var35.set(0)
    var36.set(0)
    var37.set(0)
    var38.set(0)
    var39.set(0)
    var40.set(0)
    var41.set(0)
    var42.set(0)
    var43.set(0)
    var44.set(0)
    var45.set(0)
    var46.set(0)
    var47.set(0)
    var48.set(0)
    var49.set(0)
    var50.set(0)
    var51.set(0)
    var52.set(0)
    var53.set(0)
    var54.set(0)
    var55.set(0)
    var56.set(0)
    var57.set(0)
    var58.set(0)
    var59.set(0)
    var60.set(0)
    var61.set(0)
    var62.set(0)
    var63.set(0)
    var64.set(0)
    var65.set(0)
    var66.set(0)

def total():
    global cost1
    global sevice_charge
    global totalbill

    item1=float(textlussi.get())
    item2=float(textdalgona_coffee.get())
    item3=float(textflat_white.get())
    item4=float(textcappuccino.get())
    item5=float(textexpresso.get())
    item6=float(textcold_coffee.get())
    item7=float(textbutter_milk.get())
    item8=float(textlemonaid.get())
    item9=float(textorange_juice.get())
    item10=float(textapple_juice.get())
    item11=float(textpineapple_juice.get())
    item12=float(textcarrot_juice.get())
    item13=float(textbeetroot_juice.get())
    item14=float(textbanana_juice.get())
    item15=float(textgrape_juice.get())
    item16=float(textstrawberry_juice.get())
    item17=float(textbutter_cake.get())
    item18=float(textpound_cake.get())
    item19=float(textsponge_cake.get())
    item20=float(textgenoise_cake.get())
    item21=float(textbiscuit_cake.get())
    item22=float(textchiffon_cake.get())
    item23=float(textcarrot_cake.get())
    item24=float(textred_velvet_cake.get())
    item25=float(textchocobar.get())
    item26=float(textvannila.get())
    item27=float(textchocolate.get())
    item28=float(textmint.get())
    item29=float(textblueberry.get())
    item30=float(textcaramel.get())
    item31=float(textbig_mix.get())
    item32=float(textbutterscotch.get())
    item33=float(textbouillon_soup.get())
    item34=float(textbroth_soup.get())
    item35=float(textcream_soup.get())
    item36=float(textpotage_soup.get())
    item37=float(textcorn_soup.get())
    item38=float(textsprout_salad.get())
    item39=float(textpasta_salad.get())
    item40=float(textorzo_salad.get())
    item41=float(textkale_salad.get())
    item42=float(textgreek_salad.get())
    item43=float(textpaneer_sandwich.get())
    item44=float(textcheese_sandwich.get())
    item45=float(textgrilled_sandwich.get())
    item46=float(textclub_sandwich.get())
    item47=float(textpotato_sandwich.get())
    item48=float(textmushroom_sandwich.get())
    item49=float(textchocolate_sandwich.get())
    item50=float(textcucumber_sandwich.get())
    item51=float(textcurd_sanwich.get())
    item52=float(textveg_sandwich.get())
    item53=float(texthalwa.get())
    item54=float(textkaju_barfi.get())
    item55=float(textladdu.get())
    item56=float(textjilebi.get())
    item57=float(textjangry.get())
    item58=float(textputarekulu.get())
    item59=float(textrasgulla.get())
    item60=float(textmysore_pak.get())
    item61=float(textpalkova.get())
    item62=float(textkesari.get())
    item63=float(textbadusha.get())
    item64=float(textkalakani.get())
    item65=float(textmalai_laddu.get())
    item66=float(texttokkudu_laddu.get())

    c1=item1*35+item2*35+item3*35+item4*35+item5*35+item6*35+item7*35+item8*35
    c2=item9*50+item10*50+item11*50+item12*50+item13*50+item14*50+item15*50+item16*50
    c3=item17*70+item18*70+item19*70+item20*70+item21*70+item22*70+item23*70+item24*70
    c4=item25*90+item26*90+item27*90+item28*90+item29*90+item30*90+item31*90+item32*90
    c5=item33*120+item34*120+item35*120+item36*120+item37*120+item38*120+item39*120+item40*120+item41*120+item42*120
    c6=item43*150+item44*150+item45*150+item46*150+item47*150+item48*150+item49*150+item50*150+item51*150+item52*150
    c7=item53*15+item54*15+item55*15+item56*15+item57*15+item58*15+item59*15+item60*15+item61*15+item62*15+item63*15+item64*15+item65*15+item66*15

    cost1="Rs",str("%0.2f" % (c1+c2+c3+c4+c5+c6+c7))
    textentry1.set(cost1)
    sevice_charge="Rs",str("%0.2f" % ((c1+c2+c3+c4+c5+c6+c7)/10))
    textentry2.set(sevice_charge)
    totalbill="Rs"+str("%0.2f" % ((c1+c2+c3+c4+c5+c6+c7)+((c1+c2+c3+c4+c5+c6+c7)/10)))
    textentry3.set(totalbill)
    
def receipt():
    screen=Toplevel(root)
    screen.geometry("800x800")
    screen.title("Receipt")
    topsx = Frame(screen,width =800,height=100,relief=RAISED,bd=14)
    topsx.pack(side=TOP)
    label1x = Label(topsx,font=('arial',50,'bold'),text="Receipt Card",fg="black",bd=10,anchor=W)
    label1x.grid(row=0,column=0)
    bottom=Frame(screen,width =700,height=700,relief=RAISED,bd=14)
    bottom.pack(side=BOTTOM)

    lblReceipt = Label(bottom, font=('arial', 12, 'bold'), text="Receipt",bd = 2, anchor = "w")
    lblReceipt.grid(row = 0, column = 0, sticky = W)
    txtReceipt = Text(bottom, font=('arial', 11, 'bold'), width = 100, height =300, bg="white", bd=8)
    txtReceipt.grid(row = 1, column = 0)

    x = random.randint(10908, 500876)
    randomRef = str(x)
    Receipt_Ref=("BILL" + randomRef)

    txtReceipt.insert(END, 'Name: \t\t\t'+label1entry.get()+"\n\n")
    txtReceipt.insert(END, 'Receipt Ref: \t\t\t'+Receipt_Ref+"\t\t\t"+localtime+"\n")
    txtReceipt.insert(END, '\n\nItems\t\t\t'+'Quantity\t\t\t'+"Price \n\n")

    if textlussi.get() > 0:
        txtReceipt.insert(END, 'Lussi:\t\t\t'+str(textlussi.get())+'\t\t\t'+str('Rs%.2f'%(textlussi.get()*35))+'\n')
    if textdalgona_coffee.get() > 0:
        txtReceipt.insert(END, 'Dalgona coffee:\t\t\t'+str(textdalgona_coffee.get())+'\t\t\t'+str('Rs%.2f'%(textdalgona_coffee.get()*35))+'\n')
    if textflat_white.get() > 0:
        txtReceipt.insert(END, 'Flat white:\t\t\t'+str(textflat_white.get())+'\t\t\t'+str('Rs%.2f'%(textflat_white.get()*35))+'\n')
    if textcappuccino.get() > 0:
        txtReceipt.insert(END, 'Cappuccino:\t\t\t'+str(textcappuccino.get())+'\t\t\t'+str('Rs%.2f'%(textcappuccino.get()*35))+'\n')
    if textexpresso.get() > 0:
        txtReceipt.insert(END, 'Expresso:\t\t\t'+str(textexpresso.get())+'\t\t\t'+str('Rs%.2f'%(textexpresso.get()*35))+'\n')
    if textcold_coffee.get() > 0:
        txtReceipt.insert(END, 'Cold coffee:\t\t\t'+str(textcold_coffee.get())+'\t\t\t'+str('Rs%.2f'%(textcold_coffee.get()*35))+'\n')
    if textbutter_milk.get() > 0:
        txtReceipt.insert(END, 'Butter milk:\t\t\t'+str(textbutter_milk.get())+'\t\t\t'+str('Rs%.2f'%(textbutter_milk.get()*35))+'\n')
    if textlemonaid.get() > 0:
        txtReceipt.insert(END, 'lemonaid:\t\t\t'+str(textlemonaid.get())+'\t\t\t'+str('Rs%.2f'%(textlemonaid.get()*35))+'\n')
    
    if textorange_juice.get() > 0:
        txtReceipt.insert(END, 'Orange juice:\t\t\t'+str(textorange_juice.get())+'\t\t\t'+str('Rs%.2f'%(textorange_juice.get()*50))+'\n')
    if textapple_juice.get() > 0:
        txtReceipt.insert(END, 'Apple juice:\t\t\t'+str(textapple_juice.get())+'\t\t\t'+str('Rs%.2f'%(textapple_juice.get()*50))+'\n')
    if textpineapple_juice.get() > 0:
        txtReceipt.insert(END, 'Pineapple juice:\t\t\t'+str(textpineapple_juice.get())+'\t\t\t'+str('Rs%.2f'%(textpineapple_juice.get()*50))+'\n')
    if textcarrot_juice.get() > 0:
        txtReceipt.insert(END, 'Carrot juice:\t\t\t'+str(textcarrot_juice.get())+'\t\t\t'+str('Rs%.2f'%(textcarrot_juice.get()*50))+'\n')
    if textbeetroot_juice.get() > 0:
        txtReceipt.insert(END, 'Beetroot juice:\t\t\t'+str(textbeetroot_juice.get())+'\t\t\t'+str('Rs%.2f'%(textbeetroot_juice.get()*50))+'\n')
    if textbanana_juice.get() > 0:
        txtReceipt.insert(END, 'Banana juice:\t\t\t'+str(textbanana_juice.get())+'\t\t\t'+str('Rs%.2f'%(textbanana_juice.get()*50))+'\n')
    if textgrape_juice.get() > 0:
        txtReceipt.insert(END, 'Grape juice:\t\t\t'+str(textgrape_juice.get())+'\t\t\t'+str('Rs%.2f'%(textgrape_juice.get()*50))+'\n')
    if textstrawberry_juice.get() > 0:
        txtReceipt.insert(END, 'Strawberry juice:\t\t\t'+str(textstrawberry_juice.get())+'\t\t\t'+str('Rs%.2f'%(textstrawberry_juice.get()*50))+'\n')

    if textbutter_cake.get() > 0:
        txtReceipt.insert(END, 'Butter cake:\t\t\t'+str(textbutter_cake.get())+'\t\t\t'+str('Rs%.2f'%(textbutter_cake.get()*70))+'\n')
    if textpound_cake.get() > 0:
        txtReceipt.insert(END, 'Pound cake:\t\t\t'+str(textpound_cake.get())+'\t\t\t'+str('Rs%.2f'%(textpound_cake.get()*70))+'\n')
    if textsponge_cake.get() > 0:
        txtReceipt.insert(END, 'Sponge cake:\t\t\t'+str(textsponge_cake.get())+'\t\t\t'+str('Rs%.2f'%(textsponge_cake.get()*70))+'\n')
    if textgenoise_cake.get() > 0:
        txtReceipt.insert(END, 'Genoise cake:\t\t\t'+str(textgenoise_cake.get())+'\t\t\t'+str('Rs%.2f'%(textgenoise_cake.get()*70))+'\n')
    if textbiscuit_cake.get() > 0:
        txtReceipt.insert(END, 'Biscuit cake:\t\t\t'+str(textbiscuit_cake.get())+'\t\t\t'+str('Rs%.2f'%(textbiscuit_cake.get()*70))+'\n')
    if textchiffon_cake.get() > 0:
        txtReceipt.insert(END, 'Chiffon cake:\t\t\t'+str(textchiffon_cake.get())+'\t\t\t'+str('Rs%.2f'%(textchiffon_cake.get()*70))+'\n')
    if textcarrot_cake.get() > 0:
        txtReceipt.insert(END, 'Carrot cake:\t\t\t'+str(textcarrot_cake.get())+'\t\t\t'+str('Rs%.2f'%(textcarrot_cake.get()*70))+'\n')
    if textred_velvet_cake.get() > 0:
        txtReceipt.insert(END, 'Red velvet cake:\t\t\t'+str(textred_velvet_cake.get())+'\t\t\t'+str('Rs%.2f'%(textred_velvet_cake.get()*70))+'\n')
    if textchocobar.get() > 0:
        txtReceipt.insert(END, 'Chocobar:\t\t\t'+str(textchocobar.get())+'\t\t\t'+str('Rs%.2f'%(textchocobar.get()*90))+'\n')
    if textvannila.get() > 0:
        txtReceipt.insert(END, 'Vannila:\t\t\t'+str(textvannila.get())+'\t\t\t'+str('Rs%.2f'%(textvannila.get()*90))+'\n')
    if textchocolate.get() > 0:
        txtReceipt.insert(END, 'Chocolate:\t\t\t'+str(textchocolate.get())+'\t\t\t'+str('Rs%.2f'%(textchocolate.get()*90))+'\n')
    if textmint.get() > 0:
        txtReceipt.insert(END, 'Mint:\t\t\t'+str(textmint.get())+'\t\t\t'+str('Rs%.2f'%(textmint.get()*90))+'\n')
    if textblueberry.get() > 0:
        txtReceipt.insert(END, 'Blueberry:\t\t\t'+str(textblueberry.get())+'\t\t\t'+str('Rs%.2f'%(textblueberry.get()*90))+'\n')
    if textcaramel.get() > 0:
        txtReceipt.insert(END, 'caramel:\t\t\t'+str(textcaramel.get())+'\t\t\t'+str('Rs%.2f'%(textcaramel.get()*90))+'\n')
    if textbig_mix.get() > 0:
        txtReceipt.insert(END, 'Big mix:\t\t\t'+str(textbig_mix.get())+'\t\t\t'+str('Rs%.2f'%(textbig_mix.get()*90))+'\n')
    if textbutterscotch.get() > 0:
        txtReceipt.insert(END, 'Butterscotch:\t\t\t'+str(textbutterscotch.get())+'\t\t\t'+str('Rs%.2f'%(textbutterscotch.get()*90))+'\n')

    if textbouillon_soup.get() > 0:
        txtReceipt.insert(END, 'Boullion soup:\t\t\t'+str(textbouillon_soup.get())+'\t\t\t'+str('Rs%.2f'%(textbouillon_soup.get()*120))+'\n')
    if textbroth_soup.get() > 0:
        txtReceipt.insert(END, 'Broth soup:\t\t\t'+str(textbroth_soup.get())+'\t\t\t'+str('Rs%.2f'%(textbroth_soup.get()*120))+'\n')
    if textcream_soup.get() > 0:
        txtReceipt.insert(END, 'Cream soup:\t\t\t'+str(textcream_soup.get())+'\t\t\t'+str('Rs%.2f'%(textcream_soup.get()*120))+'\n')
    if textpotage_soup.get() > 0:
        txtReceipt.insert(END, 'Potage soup:\t\t\t'+str(textpotage_soup.get())+'\t\t\t'+str('Rs%.2f'%(textpotage_soup.get()*120))+'\n')
    if textcorn_soup.get() > 0:
        txtReceipt.insert(END, 'Corn soup:\t\t\t'+str(textcorn_soup.get())+'\t\t\t'+str('Rs%.2f'%(textcorn_soup.get()*120))+'\n')
    if textsprout_salad.get() > 0:
        txtReceipt.insert(END, 'Sprout salad:\t\t\t'+str(textsprout_salad.get())+'\t\t\t'+str('Rs%.2f'%(textsprout_salad.get()*120))+'\n')
    if textpasta_salad.get() > 0:
        txtReceipt.insert(END, 'Pasta salad:\t\t\t'+str(textpasta_salad.get())+'\t\t\t'+str('Rs%.2f'%(textpasta_salad.get()*120))+'\n')
    if textorzo_salad.get() > 0:
        txtReceipt.insert(END, 'Orzo salad:\t\t\t'+str(textorzo_salad.get())+'\t\t\t'+str('Rs%.2f'%(textorzo_salad.get()*120))+'\n')
    if textkale_salad.get() > 0:
        txtReceipt.insert(END, 'kale salad:\t\t\t'+str(textkale_salad.get())+'\t\t\t'+str('Rs%.2f'%(textkale_salad.get()*120))+'\n')
    if textgreek_salad.get() > 0:
        txtReceipt.insert(END, 'greek salad:\t\t\t'+str(textgreek_salad.get())+'\t\t\t'+str('Rs%.2f'%(textgreek_salad.get()*120))+'\n')
    
    if textpaneer_sandwich.get() > 0:
        txtReceipt.insert(END, 'Paneer sandwich:\t\t\t'+str(textpaneer_sandwich.get())+'\t\t\t'+str('Rs%.2f'%(textpaneer_sandwich.get()*150))+'\n')
    if textcheese_sandwich.get() > 0:
        txtReceipt.insert(END, 'Cheese sandwich:\t\t\t'+str(textcheese_sandwich.get())+'\t\t\t'+str('Rs%.2f'%(textcheese_sandwich.get()*150))+'\n')
    if textgrilled_sandwich.get() > 0:
        txtReceipt.insert(END, 'Grilled sandwich:\t\t\t'+str(textgrilled_sandwich.get())+'\t\t\t'+str('Rs%.2f'%(textgrilled_sandwich.get()*150))+'\n')
    if textclub_sandwich.get() > 0:
        txtReceipt.insert(END, 'club sandwich:\t\t\t'+str(textclub_sandwich.get())+'\t\t\t'+str('Rs%.2f'%(textclub_sandwich.get()*50))+'\n')
    if textpotato_sandwich.get() > 0:
        txtReceipt.insert(END, 'Potato sandwich:\t\t\t'+str(textpotato_sandwich.get())+'\t\t\t'+str('Rs%.2f'%(textpotato_sandwich.get()*150))+'\n')
    if textmushroom_sandwich.get() > 0:
        txtReceipt.insert(END, 'Mushroom sandwich:\t\t\t'+str(textmushroom_sandwich.get())+'\t\t\t'+str('Rs%.2f'%(textmushroom_sandwich.get()*150))+'\n')
    if textchocolate_sandwich.get() > 0:
        txtReceipt.insert(END, 'Chocolate sandwich:\t\t\t'+str(textchocolate_sandwich.get())+'\t\t\t'+str('Rs%.2f'%(textchocolate_sandwich.get()*150))+'\n')
    if textcucumber_sandwich.get() > 0:
        txtReceipt.insert(END, 'Cucumber sandwich:\t\t\t'+str(textcucumber_sandwich.get())+'\t\t\t'+str('Rs%.2f'%(textcucumber_sandwich.get()*150))+'\n')
    if textcurd_sanwich.get() > 0:
        txtReceipt.insert(END, 'Curd sandwich:\t\t\t'+str(textcurd_sanwich.get())+'\t\t\t'+str('Rs%.2f'%(textcurd_sanwich.get()*150))+'\n')
    if textveg_sandwich.get() > 0:
        txtReceipt.insert(END, 'Veg sandwich:\t\t\t'+str(textveg_sandwich.get())+'\t\t\t'+str('Rs%.2f'%(textveg_sandwich.get()*150))+'\n')
    
    if texthalwa.get() > 0:
        txtReceipt.insert(END, 'Halwa:\t\t\t'+str(texthalwa.get())+'\t\t\t'+str('Rs%.2f'%(texthalwa.get()*15))+'\n')
    if textkaju_barfi.get() > 0:
        txtReceipt.insert(END, 'Kaju barfi:\t\t\t'+str(textkaju_barfi.get())+'\t\t\t'+str('Rs%.2f'%(textkaju_barfi.get()*15))+'\n')
    if textladdu.get() > 0:
        txtReceipt.insert(END, 'Laddu:\t\t\t'+str(textladdu.get())+'\t\t\t'+str('Rs%.2f'%(textladdu.get()*15))+'\n')
    if textjilebi.get() > 0:
        txtReceipt.insert(END, 'Jilebi:\t\t\t'+str(textjilebi.get())+'\t\t\t'+str('Rs%.2f'%(textjilebi.get()*15))+'\n')
    if textjangry.get() > 0:
        txtReceipt.insert(END, 'Jangry:\t\t\t'+str(textjangry.get())+'\t\t\t'+str('Rs%.2f'%(textjangry.get()*10))+'\n')
    if textputarekulu.get() > 0:
        txtReceipt.insert(END, 'Putarekulu:\t\t\t'+str(textputarekulu.get())+'\t\t\t'+str('Rs%.2f'%(textputarekulu.get()*15))+'\n')
    if textrasgulla.get() > 0:
        txtReceipt.insert(END, 'Rasgulla:\t\t\t'+str(textrasgulla.get())+'\t\t\t'+str('Rs%.2f'%(textrasgulla.get()*15))+'\n')
    if textmysore_pak.get() > 0:
        txtReceipt.insert(END, 'Mysore pak:\t\t\t'+str(textmysore_pak.get())+'\t\t\t'+str('Rs%.2f'%(textmysore_pak.get()*15))+'\n')
    if textpalkova.get() > 0:
        txtReceipt.insert(END, 'Palkova:\t\t\t'+str(textpalkova.get())+'\t\t\t'+str('Rs%.2f'%(textpalkova.get()*15))+'\n')
    if textkesari.get() > 0:
        txtReceipt.insert(END, 'Kesari:\t\t\t'+str(textkesari.get())+'\t\t\t'+str('Rs%.2f'%(textkesari.get()*15))+'\n')
    if textbadusha.get() > 0:
        txtReceipt.insert(END, 'Badusha:\t\t\t'+str(textbadusha.get())+'\t\t\t'+str('Rs%.2f'%(textbadusha.get()*15))+'\n')
    if textkalakani.get() > 0:
        txtReceipt.insert(END, 'Kalakani:\t\t\t'+str(textkalakani.get())+'\t\t\t'+str('Rs%.2f'%(textkalakani.get()*15))+'\n')
    if textmalai_laddu.get() > 0:
        txtReceipt.insert(END, 'Malai laddu:\t\t\t'+str(textmalai_laddu.get())+'\t\t\t'+str('Rs%.2f'%(textmalai_laddu.get()*15))+'\n')
    if texttokkudu_laddu.get() > 0:
        txtReceipt.insert(END, 'Tokkudu laddu:\t\t\t'+str(texttokkudu_laddu.get())+'\t\t\t'+str('Rs%.2f'%(texttokkudu_laddu.get()*15))+'\n')
    txtReceipt.insert(END, '\n\n\nCost of food:\t\t\t'+str(cost1)+"\n")
    txtReceipt.insert(END, 'Service charge:\t\t\t'+str(sevice_charge)+"\n")
    txtReceipt.insert(END, 'Total bill:\t\t\t'+str(totalbill)+"\n")

    def printf():
        q=txtReceipt.get("1.0","end-1c")
        filename=tempfile.mkdtemp(".txt")
        open(filename,"w").write(q)
        os.startfile(filename,"print")
    def save():
        newfolder=filenamei.get()
        if os.path.exists(newfolder)==False:
            
            os.makedirs(newfolder)
            path2=path+'\\'+newfolder
            os.chdir(path2)
            label1entryi=label1entry.get()
                
            #label1entryi=label1entry.get()
            #file=open(label1entryi,"w")
            file=open(label1entryi+'.txt',"w")
            file.write('Name: \t\t\t'+label1entry.get()+"\n\n")
            file.write('Receipt Ref: \t\t\t'+Receipt_Ref+"\t\t\t"+localtime+"\n")
            file.write('\n\nItems\t\t\t'+'Quantity\t\t\t'+"Price \n\n")

            if textlussi.get() > 0:
                file.write('Lussi:\t\t\t'+str(textlussi.get())+'\t\t\t'+str('Rs%.2f'%(textlussi.get()*35))+'\n')
            if textdalgona_coffee.get() > 0:
                file.write('Dalgona coffee:\t\t\t'+str(textdalgona_coffee.get())+'\t\t\t'+str('Rs%.2f'%(textdalgona_coffee.get()*35))+'\n')
            if textflat_white.get() > 0:
                file.write('Flat white:\t\t\t'+str(textflat_white.get())+'\t\t\t'+str('Rs%.2f'%(textflat_white.get()*35))+'\n')
            if textcappuccino.get() > 0:
                file.write('Cappuccino:\t\t\t'+str(textcappuccino.get())+'\t\t\t'+str('Rs%.2f'%(textcappuccino.get()*35))+'\n')
            if textexpresso.get() > 0:
                file.write('Expresso:\t\t\t'+str(textexpresso.get())+'\t\t\t'+str('Rs%.2f'%(textexpresso.get()*35))+'\n')
            if textcold_coffee.get() > 0:
                file.write('Cold coffee:\t\t\t'+str(textcold_coffee.get())+'\t\t\t'+str('Rs%.2f'%(textcold_coffee.get()*35))+'\n')
            if textbutter_milk.get() > 0:
                file.write('Butter milk:\t\t\t'+str(textbutter_milk.get())+'\t\t\t'+str('Rs%.2f'%(textbutter_milk.get()*35))+'\n')
            if textlemonaid.get() > 0:
                file.write( 'lemonaid:\t\t\t'+str(textlemonaid.get())+'\t\t\t'+str('Rs%.2f'%(textlemonaid.get()*35))+'\n')
                
            if textorange_juice.get() > 0:
                file.write( 'Orange juice:\t\t\t'+str(textorange_juice.get())+'\t\t\t'+str('Rs%.2f'%(textorange_juice.get()*50))+'\n')
            if textapple_juice.get() > 0:
                file.write('Apple juice:\t\t\t'+str(textapple_juice.get())+'\t\t\t'+str('Rs%.2f'%(textapple_juice.get()*50))+'\n')
            if textpineapple_juice.get() > 0:
                file.write( 'Pineapple juice:\t\t\t'+str(textpineapple_juice.get())+'\t\t\t'+str('Rs%.2f'%(textpineapple_juice.get()*50))+'\n')
            if textcarrot_juice.get() > 0:
                file.write('Carrot juice:\t\t\t'+str(textcarrot_juice.get())+'\t\t\t'+str('Rs%.2f'%(textcarrot_juice.get()*50))+'\n')
            if textbeetroot_juice.get() > 0:
                file.write('Beetroot juice:\t\t\t'+str(textbeetroot_juice.get())+'\t\t\t'+str('Rs%.2f'%(textbeetroot_juice.get()*50))+'\n')
            if textbanana_juice.get() > 0:
                file.write('Banana juice:\t\t\t'+str(textbanana_juice.get())+'\t\t\t'+str('Rs%.2f'%(textbanana_juice.get()*50))+'\n')
            if textgrape_juice.get() > 0:
                file.write('Grape juice:\t\t\t'+str(textgrape_juice.get())+'\t\t\t'+str('Rs%.2f'%(textgrape_juice.get()*50))+'\n')
            if textstrawberry_juice.get() > 0:
                file.write('Strawberry juice:\t\t\t'+str(textstrawberry_juice.get())+'\t\t\t'+str('Rs%.2f'%(textstrawberry_juice.get()*50))+'\n')

            if textbutter_cake.get() > 0:
                file.write('Butter cake:\t\t\t'+str(textbutter_cake.get())+'\t\t\t'+str('Rs%.2f'%(textbutter_cake.get()*70))+'\n')
            if textpound_cake.get() > 0:
                file.write('Pound cake:\t\t\t'+str(textpound_cake.get())+'\t\t\t'+str('Rs%.2f'%(textpound_cake.get()*70))+'\n')
            if textsponge_cake.get() > 0:
                file.write('Sponge cake:\t\t\t'+str(textsponge_cake.get())+'\t\t\t'+str('Rs%.2f'%(textsponge_cake.get()*70))+'\n')
            if textgenoise_cake.get() > 0:
                file.write('Genoise cake:\t\t\t'+str(textgenoise_cake.get())+'\t\t\t'+str('Rs%.2f'%(textgenoise_cake.get()*70))+'\n')
            if textbiscuit_cake.get() > 0:
                file.write('Biscuit cake:\t\t\t'+str(textbiscuit_cake.get())+'\t\t\t'+str('Rs%.2f'%(textbiscuit_cake.get()*70))+'\n')
            if textchiffon_cake.get() > 0:
                file.write( 'Chiffon cake:\t\t\t'+str(textchiffon_cake.get())+'\t\t\t'+str('Rs%.2f'%(textchiffon_cake.get()*70))+'\n')
            if textcarrot_cake.get() > 0:
                file.write('Carrot cake:\t\t\t'+str(textcarrot_cake.get())+'\t\t\t'+str('Rs%.2f'%(textcarrot_cake.get()*70))+'\n')
            if textred_velvet_cake.get() > 0:
                file.write('Red velvet cake:\t\t\t'+str(textred_velvet_cake.get())+'\t\t\t'+str('Rs%.2f'%(textred_velvet_cake.get()*70))+'\n')
            if textchocobar.get() > 0:
                file.write('Chocobar:\t\t\t'+str(textchocobar.get())+'\t\t\t'+str('Rs%.2f'%(textchocobar.get()*90))+'\n')
            if textvannila.get() > 0:
                file.write('Vannila:\t\t\t'+str(textvannila.get())+'\t\t\t'+str('Rs%.2f'%(textvannila.get()*90))+'\n')
            if textchocolate.get() > 0:
                file.write('Chocolate:\t\t\t'+str(textchocolate.get())+'\t\t\t'+str('Rs%.2f'%(textchocolate.get()*90))+'\n')
            if textmint.get() > 0:
                file.write('Mint:\t\t\t'+str(textmint.get())+'\t\t\t'+str('Rs%.2f'%(textmint.get()*90))+'\n')
            if textblueberry.get() > 0:
                file.write('Blueberry:\t\t\t'+str(textblueberry.get())+'\t\t\t'+str('Rs%.2f'%(textblueberry.get()*90))+'\n')
            if textcaramel.get() > 0:
                file.write('caramel:\t\t\t'+str(textcaramel.get())+'\t\t\t'+str('Rs%.2f'%(textcaramel.get()*90))+'\n')
            if textbig_mix.get() > 0:
                file.write('Big mix:\t\t\t'+str(textbig_mix.get())+'\t\t\t'+str('Rs%.2f'%(textbig_mix.get()*90))+'\n')
            if textbutterscotch.get() > 0:
                file.write('Butterscotch:\t\t\t'+str(textbutterscotch.get())+'\t\t\t'+str('Rs%.2f'%(textbutterscotch.get()*90))+'\n')

            if textbouillon_soup.get() > 0:
                file.write('Boullion soup:\t\t\t'+str(textbouillon_soup.get())+'\t\t\t'+str('Rs%.2f'%(textbouillon_soup.get()*120))+'\n')
            if textbroth_soup.get() > 0:
                file.write('Broth soup:\t\t\t'+str(textbroth_soup.get())+'\t\t\t'+str('Rs%.2f'%(textbroth_soup.get()*120))+'\n')
            if textcream_soup.get() > 0:
                file.write('Cream soup:\t\t\t'+str(textcream_soup.get())+'\t\t\t'+str('Rs%.2f'%(textcream_soup.get()*120))+'\n')
            if textpotage_soup.get() > 0:
                file.write('Potage soup:\t\t\t'+str(textpotage_soup.get())+'\t\t\t'+str('Rs%.2f'%(textpotage_soup.get()*120))+'\n')
            if textcorn_soup.get() > 0:
                file.write('Corn soup:\t\t\t'+str(textcorn_soup.get())+'\t\t\t'+str('Rs%.2f'%(textcorn_soup.get()*120))+'\n')
            if textsprout_salad.get() > 0:
                file.write('Sprout salad:\t\t\t'+str(textsprout_salad.get())+'\t\t\t'+str('Rs%.2f'%(textsprout_salad.get()*120))+'\n')
            if textpasta_salad.get() > 0:
                file.write('Pasta salad:\t\t\t'+str(textpasta_salad.get())+'\t\t\t'+str('Rs%.2f'%(textpasta_salad.get()*120))+'\n')
            if textorzo_salad.get() > 0:
                file.write('Orzo salad:\t\t\t'+str(textorzo_salad.get())+'\t\t\t'+str('Rs%.2f'%(textorzo_salad.get()*120))+'\n')
            if textkale_salad.get() > 0:
                file.write('kale salad:\t\t\t'+str(textkale_salad.get())+'\t\t\t'+str('Rs%.2f'%(textkale_salad.get()*120))+'\n')
            if textgreek_salad.get() > 0:
                file.write('greek salad:\t\t\t'+str(textgreek_salad.get())+'\t\t\t'+str('Rs%.2f'%(textgreek_salad.get()*120))+'\n')
                    
            if textpaneer_sandwich.get() > 0:
                file.write('Paneer sandwich:\t\t\t'+str(textpaneer_sandwich.get())+'\t\t\t'+str('Rs%.2f'%(textpaneer_sandwich.get()*150))+'\n')
            if textcheese_sandwich.get() > 0:
                file.write('Cheese sandwich:\t\t\t'+str(textcheese_sandwich.get())+'\t\t\t'+str('Rs%.2f'%(textcheese_sandwich.get()*150))+'\n')
            if textgrilled_sandwich.get() > 0:
                file.write('Grilled sandwich:\t\t\t'+str(textgrilled_sandwich.get())+'\t\t\t'+str('Rs%.2f'%(textgrilled_sandwich.get()*150))+'\n')
            if textclub_sandwich.get() > 0:
                file.write('club sandwich:\t\t\t'+str(textclub_sandwich.get())+'\t\t\t'+str('Rs%.2f'%(textclub_sandwich.get()*50))+'\n')
            if textpotato_sandwich.get() > 0:
                file.write('Potato sandwich:\t\t\t'+str(textpotato_sandwich.get())+'\t\t\t'+str('Rs%.2f'%(textpotato_sandwich.get()*150))+'\n')
            if textmushroom_sandwich.get() > 0:
                file.write('Mushroom sandwich:\t\t\t'+str(textmushroom_sandwich.get())+'\t\t\t'+str('Rs%.2f'%(textmushroom_sandwich.get()*150))+'\n')
            if textchocolate_sandwich.get() > 0:
                file.write('Chocolate sandwich:\t\t\t'+str(textchocolate_sandwich.get())+'\t\t\t'+str('Rs%.2f'%(textchocolate_sandwich.get()*150))+'\n')
            if textcucumber_sandwich.get() > 0:
                file.write('Cucumber sandwich:\t\t\t'+str(textcucumber_sandwich.get())+'\t\t\t'+str('Rs%.2f'%(textcucumber_sandwich.get()*150))+'\n')
            if textcurd_sanwich.get() > 0:
                file.write('Curd sandwich:\t\t\t'+str(textcurd_sanwich.get())+'\t\t\t'+str('Rs%.2f'%(textcurd_sanwich.get()*150))+'\n')
            if textveg_sandwich.get() > 0:
                file.write('Veg sandwich:\t\t\t'+str(textveg_sandwich.get())+'\t\t\t'+str('Rs%.2f'%(textveg_sandwich.get()*150))+'\n')
                    
            if texthalwa.get() > 0:
                file.write('Halwa:\t\t\t'+str(texthalwa.get())+'\t\t\t'+str('Rs%.2f'%(texthalwa.get()*15))+'\n')
            if textkaju_barfi.get() > 0:
                file.write('Kaju barfi:\t\t\t'+str(textkaju_barfi.get())+'\t\t\t'+str('Rs%.2f'%(textkaju_barfi.get()*15))+'\n')
            if textladdu.get() > 0:
                file.write('Laddu:\t\t\t'+str(textladdu.get())+'\t\t\t'+str('Rs%.2f'%(textladdu.get()*15))+'\n')
            if textjilebi.get() > 0:
                file.write('Jilebi:\t\t\t'+str(textjilebi.get())+'\t\t\t'+str('Rs%.2f'%(textjilebi.get()*15))+'\n')
            if textjangry.get() > 0:
                file.write('Jangry:\t\t\t'+str(textjangry.get())+'\t\t\t'+str('Rs%.2f'%(textjangry.get()*10))+'\n')
            if textputarekulu.get() > 0:
                file.write('Putarekulu:\t\t\t'+str(textputarekulu.get())+'\t\t\t'+str('Rs%.2f'%(textputarekulu.get()*15))+'\n')
            if textrasgulla.get() > 0:
                file.write('Rasgulla:\t\t\t'+str(textrasgulla.get())+'\t\t\t'+str('Rs%.2f'%(textrasgulla.get()*15))+'\n')
            if textmysore_pak.get() > 0:
                file.write('Mysore pak:\t\t\t'+str(textmysore_pak.get())+'\t\t\t'+str('Rs%.2f'%(textmysore_pak.get()*15))+'\n')
            if textpalkova.get() > 0:
                file.write('Palkova:\t\t\t'+str(textpalkova.get())+'\t\t\t'+str('Rs%.2f'%(textpalkova.get()*15))+'\n')
            if textkesari.get() > 0:
                file.write('Kesari:\t\t\t'+str(textkesari.get())+'\t\t\t'+str('Rs%.2f'%(textkesari.get()*15))+'\n')
            if textbadusha.get() > 0:
                file.write('Badusha:\t\t\t'+str(textbadusha.get())+'\t\t\t'+str('Rs%.2f'%(textbadusha.get()*15))+'\n')
            if textkalakani.get() > 0:
                file.write('Kalakani:\t\t\t'+str(textkalakani.get())+'\t\t\t'+str('Rs%.2f'%(textkalakani.get()*15))+'\n')
            if textmalai_laddu.get() > 0:
                file.write('Malai laddu:\t\t\t'+str(textmalai_laddu.get())+'\t\t\t'+str('Rs%.2f'%(textmalai_laddu.get()*15))+'\n')
            if texttokkudu_laddu.get() > 0:
                file.write('Tokkudu laddu:\t\t\t'+str(texttokkudu_laddu.get())+'\t\t\t'+str('Rs%.2f'%(texttokkudu_laddu.get()*15))+'\n')
            if texttokkudu_laddu.get() > 0:
                file.write('Tokkudu laddu:\t\t\t'+str(texttokkudu_laddu.get())+'\t\t\t'+str('Rs%.2f'%(texttokkudu_laddu.get()*15)))
            file.write('\n\n\nCost of food:\t\t\t'+str(cost1)+"\n")
            file.write('Service charge:\t\t\t'+str(sevice_charge)+"\n")
            file.write('Total bill:\t\t\t'+str(totalbill)+"\n")
            file.close()
        elif os.path.exists(newfolder)==True:
            path2=path+'\\'+newfolder
            os.chdir(path2)
            label1entryi=label1entry.get()
            file=open(label1entryi,'a')
            file.write('Name: \t\t\t'+label1entry.get()+"\n\n")
            file.write('Receipt Ref: \t\t\t'+Receipt_Ref+"\t\t\t"+localtime+"\n")
            file.write('\n\nItems\t\t\t'+'Quantity\t\t\t'+"Price \n\n")

            if textlussi.get() > 0:
                file.write('Lussi:\t\t\t'+str(textlussi.get())+'\t\t\t'+str('Rs%.2f'%(textlussi.get()*35))+'\n')
            if textdalgona_coffee.get() > 0:
                file.write('Dalgona coffee:\t\t\t'+str(textdalgona_coffee.get())+'\t\t\t'+str('Rs%.2f'%(textdalgona_coffee.get()*35))+'\n')
            if textflat_white.get() > 0:
                file.write('Flat white:\t\t\t'+str(textflat_white.get())+'\t\t\t'+str('Rs%.2f'%(textflat_white.get()*35))+'\n')
            if textcappuccino.get() > 0:
                file.write('Cappuccino:\t\t\t'+str(textcappuccino.get())+'\t\t\t'+str('Rs%.2f'%(textcappuccino.get()*35))+'\n')
            if textexpresso.get() > 0:
                file.write('Expresso:\t\t\t'+str(textexpresso.get())+'\t\t\t'+str('Rs%.2f'%(textexpresso.get()*35))+'\n')
            if textcold_coffee.get() > 0:
                file.write('Cold coffee:\t\t\t'+str(textcold_coffee.get())+'\t\t\t'+str('Rs%.2f'%(textcold_coffee.get()*35))+'\n')
            if textbutter_milk.get() > 0:
                file.write('Butter milk:\t\t\t'+str(textbutter_milk.get())+'\t\t\t'+str('Rs%.2f'%(textbutter_milk.get()*35))+'\n')
            if textlemonaid.get() > 0:
                file.write( 'lemonaid:\t\t\t'+str(textlemonaid.get())+'\t\t\t'+str('Rs%.2f'%(textlemonaid.get()*35))+'\n')
                
            if textorange_juice.get() > 0:
                file.write( 'Orange juice:\t\t\t'+str(textorange_juice.get())+'\t\t\t'+str('Rs%.2f'%(textorange_juice.get()*50))+'\n')
            if textapple_juice.get() > 0:
                file.write('Apple juice:\t\t\t'+str(textapple_juice.get())+'\t\t\t'+str('Rs%.2f'%(textapple_juice.get()*50))+'\n')
            if textpineapple_juice.get() > 0:
                file.write( 'Pineapple juice:\t\t\t'+str(textpineapple_juice.get())+'\t\t\t'+str('Rs%.2f'%(textpineapple_juice.get()*50))+'\n')
            if textcarrot_juice.get() > 0:
                file.write('Carrot juice:\t\t\t'+str(textcarrot_juice.get())+'\t\t\t'+str('Rs%.2f'%(textcarrot_juice.get()*50))+'\n')
            if textbeetroot_juice.get() > 0:
                file.write('Beetroot juice:\t\t\t'+str(textbeetroot_juice.get())+'\t\t\t'+str('Rs%.2f'%(textbeetroot_juice.get()*50))+'\n')
            if textbanana_juice.get() > 0:
                file.write('Banana juice:\t\t\t'+str(textbanana_juice.get())+'\t\t\t'+str('Rs%.2f'%(textbanana_juice.get()*50))+'\n')
            if textgrape_juice.get() > 0:
                file.write('Grape juice:\t\t\t'+str(textgrape_juice.get())+'\t\t\t'+str('Rs%.2f'%(textgrape_juice.get()*50))+'\n')
            if textstrawberry_juice.get() > 0:
                file.write('Strawberry juice:\t\t\t'+str(textstrawberry_juice.get())+'\t\t\t'+str('Rs%.2f'%(textstrawberry_juice.get()*50))+'\n')

            if textbutter_cake.get() > 0:
                file.write('Butter cake:\t\t\t'+str(textbutter_cake.get())+'\t\t\t'+str('Rs%.2f'%(textbutter_cake.get()*70))+'\n')
            if textpound_cake.get() > 0:
                file.write('Pound cake:\t\t\t'+str(textpound_cake.get())+'\t\t\t'+str('Rs%.2f'%(textpound_cake.get()*70))+'\n')
            if textsponge_cake.get() > 0:
                file.write('Sponge cake:\t\t\t'+str(textsponge_cake.get())+'\t\t\t'+str('Rs%.2f'%(textsponge_cake.get()*70))+'\n')
            if textgenoise_cake.get() > 0:
                file.write('Genoise cake:\t\t\t'+str(textgenoise_cake.get())+'\t\t\t'+str('Rs%.2f'%(textgenoise_cake.get()*70))+'\n')
            if textbiscuit_cake.get() > 0:
                file.write('Biscuit cake:\t\t\t'+str(textbiscuit_cake.get())+'\t\t\t'+str('Rs%.2f'%(textbiscuit_cake.get()*70))+'\n')
            if textchiffon_cake.get() > 0:
                file.write( 'Chiffon cake:\t\t\t'+str(textchiffon_cake.get())+'\t\t\t'+str('Rs%.2f'%(textchiffon_cake.get()*70))+'\n')
            if textcarrot_cake.get() > 0:
                file.write('Carrot cake:\t\t\t'+str(textcarrot_cake.get())+'\t\t\t'+str('Rs%.2f'%(textcarrot_cake.get()*70))+'\n')
            if textred_velvet_cake.get() > 0:
                file.write('Red velvet cake:\t\t\t'+str(textred_velvet_cake.get())+'\t\t\t'+str('Rs%.2f'%(textred_velvet_cake.get()*70))+'\n')
            if textchocobar.get() > 0:
                file.write('Chocobar:\t\t\t'+str(textchocobar.get())+'\t\t\t'+str('Rs%.2f'%(textchocobar.get()*90))+'\n')
            if textvannila.get() > 0:
                file.write('Vannila:\t\t\t'+str(textvannila.get())+'\t\t\t'+str('Rs%.2f'%(textvannila.get()*90))+'\n')
            if textchocolate.get() > 0:
                file.write('Chocolate:\t\t\t'+str(textchocolate.get())+'\t\t\t'+str('Rs%.2f'%(textchocolate.get()*90))+'\n')
            if textmint.get() > 0:
                file.write('Mint:\t\t\t'+str(textmint.get())+'\t\t\t'+str('Rs%.2f'%(textmint.get()*90))+'\n')
            if textblueberry.get() > 0:
                file.write('Blueberry:\t\t\t'+str(textblueberry.get())+'\t\t\t'+str('Rs%.2f'%(textblueberry.get()*90))+'\n')
            if textcaramel.get() > 0:
                file.write('caramel:\t\t\t'+str(textcaramel.get())+'\t\t\t'+str('Rs%.2f'%(textcaramel.get()*90))+'\n')
            if textbig_mix.get() > 0:
                file.write('Big mix:\t\t\t'+str(textbig_mix.get())+'\t\t\t'+str('Rs%.2f'%(textbig_mix.get()*90))+'\n')
            if textbutterscotch.get() > 0:
                file.write('Butterscotch:\t\t\t'+str(textbutterscotch.get())+'\t\t\t'+str('Rs%.2f'%(textbutterscotch.get()*90))+'\n')

            if textbouillon_soup.get() > 0:
                file.write('Boullion soup:\t\t\t'+str(textbouillon_soup.get())+'\t\t\t'+str('Rs%.2f'%(textbouillon_soup.get()*120))+'\n')
            if textbroth_soup.get() > 0:
                file.write('Broth soup:\t\t\t'+str(textbroth_soup.get())+'\t\t\t'+str('Rs%.2f'%(textbroth_soup.get()*120))+'\n')
            if textcream_soup.get() > 0:
                file.write('Cream soup:\t\t\t'+str(textcream_soup.get())+'\t\t\t'+str('Rs%.2f'%(textcream_soup.get()*120))+'\n')
            if textpotage_soup.get() > 0:
                file.write('Potage soup:\t\t\t'+str(textpotage_soup.get())+'\t\t\t'+str('Rs%.2f'%(textpotage_soup.get()*120))+'\n')
            if textcorn_soup.get() > 0:
                file.write('Corn soup:\t\t\t'+str(textcorn_soup.get())+'\t\t\t'+str('Rs%.2f'%(textcorn_soup.get()*120))+'\n')
            if textsprout_salad.get() > 0:
                file.write('Sprout salad:\t\t\t'+str(textsprout_salad.get())+'\t\t\t'+str('Rs%.2f'%(textsprout_salad.get()*120))+'\n')
            if textpasta_salad.get() > 0:
                file.write('Pasta salad:\t\t\t'+str(textpasta_salad.get())+'\t\t\t'+str('Rs%.2f'%(textpasta_salad.get()*120))+'\n')
            if textorzo_salad.get() > 0:
                file.write('Orzo salad:\t\t\t'+str(textorzo_salad.get())+'\t\t\t'+str('Rs%.2f'%(textorzo_salad.get()*120))+'\n')
            if textkale_salad.get() > 0:
                file.write('kale salad:\t\t\t'+str(textkale_salad.get())+'\t\t\t'+str('Rs%.2f'%(textkale_salad.get()*120))+'\n')
            if textgreek_salad.get() > 0:
                file.write('greek salad:\t\t\t'+str(textgreek_salad.get())+'\t\t\t'+str('Rs%.2f'%(textgreek_salad.get()*120))+'\n')
                    
            if textpaneer_sandwich.get() > 0:
                file.write('Paneer sandwich:\t\t\t'+str(textpaneer_sandwich.get())+'\t\t\t'+str('Rs%.2f'%(textpaneer_sandwich.get()*150))+'\n')
            if textcheese_sandwich.get() > 0:
                file.write('Cheese sandwich:\t\t\t'+str(textcheese_sandwich.get())+'\t\t\t'+str('Rs%.2f'%(textcheese_sandwich.get()*150))+'\n')
            if textgrilled_sandwich.get() > 0:
                file.write('Grilled sandwich:\t\t\t'+str(textgrilled_sandwich.get())+'\t\t\t'+str('Rs%.2f'%(textgrilled_sandwich.get()*150))+'\n')
            if textclub_sandwich.get() > 0:
                file.write('club sandwich:\t\t\t'+str(textclub_sandwich.get())+'\t\t\t'+str('Rs%.2f'%(textclub_sandwich.get()*50))+'\n')
            if textpotato_sandwich.get() > 0:
                file.write('Potato sandwich:\t\t\t'+str(textpotato_sandwich.get())+'\t\t\t'+str('Rs%.2f'%(textpotato_sandwich.get()*150))+'\n')
            if textmushroom_sandwich.get() > 0:
                file.write('Mushroom sandwich:\t\t\t'+str(textmushroom_sandwich.get())+'\t\t\t'+str('Rs%.2f'%(textmushroom_sandwich.get()*150))+'\n')
            if textchocolate_sandwich.get() > 0:
                file.write('Chocolate sandwich:\t\t\t'+str(textchocolate_sandwich.get())+'\t\t\t'+str('Rs%.2f'%(textchocolate_sandwich.get()*150))+'\n')
            if textcucumber_sandwich.get() > 0:
                file.write('Cucumber sandwich:\t\t\t'+str(textcucumber_sandwich.get())+'\t\t\t'+str('Rs%.2f'%(textcucumber_sandwich.get()*150))+'\n')
            if textcurd_sanwich.get() > 0:
                file.write('Curd sandwich:\t\t\t'+str(textcurd_sanwich.get())+'\t\t\t'+str('Rs%.2f'%(textcurd_sanwich.get()*150))+'\n')
            if textveg_sandwich.get() > 0:
                file.write('Veg sandwich:\t\t\t'+str(textveg_sandwich.get())+'\t\t\t'+str('Rs%.2f'%(textveg_sandwich.get()*150))+'\n')
                    
            if texthalwa.get() > 0:
                file.write('Halwa:\t\t\t'+str(texthalwa.get())+'\t\t\t'+str('Rs%.2f'%(texthalwa.get()*15))+'\n')
            if textkaju_barfi.get() > 0:
                file.write('Kaju barfi:\t\t\t'+str(textkaju_barfi.get())+'\t\t\t'+str('Rs%.2f'%(textkaju_barfi.get()*15))+'\n')
            if textladdu.get() > 0:
                file.write('Laddu:\t\t\t'+str(textladdu.get())+'\t\t\t'+str('Rs%.2f'%(textladdu.get()*15))+'\n')
            if textjilebi.get() > 0:
                file.write('Jilebi:\t\t\t'+str(textjilebi.get())+'\t\t\t'+str('Rs%.2f'%(textjilebi.get()*15))+'\n')
            if textjangry.get() > 0:
                file.write('Jangry:\t\t\t'+str(textjangry.get())+'\t\t\t'+str('Rs%.2f'%(textjangry.get()*10))+'\n')
            if textputarekulu.get() > 0:
                file.write('Putarekulu:\t\t\t'+str(textputarekulu.get())+'\t\t\t'+str('Rs%.2f'%(textputarekulu.get()*15))+'\n')
            if textrasgulla.get() > 0:
                file.write('Rasgulla:\t\t\t'+str(textrasgulla.get())+'\t\t\t'+str('Rs%.2f'%(textrasgulla.get()*15))+'\n')
            if textmysore_pak.get() > 0:
                file.write('Mysore pak:\t\t\t'+str(textmysore_pak.get())+'\t\t\t'+str('Rs%.2f'%(textmysore_pak.get()*15))+'\n')
            if textpalkova.get() > 0:
                file.write('Palkova:\t\t\t'+str(textpalkova.get())+'\t\t\t'+str('Rs%.2f'%(textpalkova.get()*15))+'\n')
            if textkesari.get() > 0:
                file.write('Kesari:\t\t\t'+str(textkesari.get())+'\t\t\t'+str('Rs%.2f'%(textkesari.get()*15))+'\n')
            if textbadusha.get() > 0:
                file.write('Badusha:\t\t\t'+str(textbadusha.get())+'\t\t\t'+str('Rs%.2f'%(textbadusha.get()*15))+'\n')
            if textkalakani.get() > 0:
                file.write('Kalakani:\t\t\t'+str(textkalakani.get())+'\t\t\t'+str('Rs%.2f'%(textkalakani.get()*15))+'\n')
            if textmalai_laddu.get() > 0:
                file.write('Malai laddu:\t\t\t'+str(textmalai_laddu.get())+'\t\t\t'+str('Rs%.2f'%(textmalai_laddu.get()*15))+'\n')
            if texttokkudu_laddu.get() > 0:
                file.write('Tokkudu laddu:\t\t\t'+str(texttokkudu_laddu.get())+'\t\t\t'+str('Rs%.2f'%(texttokkudu_laddu.get()*15))+'\n')
            if texttokkudu_laddu.get() > 0:
                file.write('Tokkudu laddu:\t\t\t'+str(texttokkudu_laddu.get())+'\t\t\t'+str('Rs%.2f'%(texttokkudu_laddu.get()*15)))
            file.write('\n\n\nCost of food:\t\t\t'+str(cost1)+"\n")
            file.write('Service charge:\t\t\t'+str(sevice_charge)+"\n")
            file.write('Total bill:\t\t\t'+str(totalbill)+"\n")
            file.close()
                
        Label(topsx,text='saved sucessfully',fg='green').grid(row=3,column=0)        
            

    btnprint=Button(topsx,padx=8,pady=8,fg='black',font=('arial bold',13),
                    width=6,text="print",relief=RAISED,bg="grey",command=printf).grid(row=1,column=0)
    btnsave=Button(topsx,padx=8,pady=8,fg='black',font=('arial bold',13),
                    width=6,text="Save",relief=RAISED,bg="grey",command=save).grid(row=2,column=0)
def menu():
    screen1=Toplevel(root)
    screen1.title("Menu")
    screen1.geometry("500x500")
    
    topsm = Frame(screen1,width =500,height=50,relief=RAISED,bd=14)
    topsm.pack(side=TOP)
    label1x = Label(topsm,font=('arial',50,'bold'),text="Menu Card",fg="black",bd=10,anchor=W)
    label1x.grid(row=0,column=0)
    text1=Label(topsm,font=('arial',20,'bold'),text="Welcome to our cafe!!",fg="black",bd=10,anchor=W)
    text1.grid(row=1,column=0)
    text2=Label(topsm,font=('arial',20,'bold'),text="Have a look at todays speacials",fg="black",bd=10,anchor=W)
    text2.grid(row=2,column=0)
    bottomm=Frame(screen1,width =200,height=400,relief=RAISED,bd=14)
    bottomm.pack(side=TOP)
    
    def drinks():
        screen2=Toplevel(screen1)
        screen2.geometry("400x400")
        screen2.title("Items")
        Label(screen2,font=('arial',13,'bold'),text="Lussi",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Dalgona coffee",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Flat white",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Cappuccino",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Cold coffee",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Butter milk",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Lemonaid",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Expresso",fg="black",bd=10,anchor=W).pack()
    def juices():
        screen2=Toplevel(screen1)
        screen2.geometry("400x400")
        screen2.title("Items")
        Label(screen2,font=('arial',13,'bold'),text="Orange juice",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Apple juice",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Pineapple juice",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Carrot",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Beetroot juice",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Grape juice",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Strawberry juice",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Banana juice",fg="black",bd=10,anchor=W).pack()
    def cakes():
        screen2=Toplevel(screen1)
        screen2.geometry("400x400")
        screen2.title("Items")
        Label(screen2,font=('arial',13,'bold'),text="Butter cake",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Pound cake",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Sponge cake",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Genoise cake",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Biscuit cake",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Chiffon cake",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Carrot cake",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Red velvet cake",fg="black",bd=10,anchor=W).pack()
    def ice_cream():
        screen2=Toplevel(screen1)
        screen2.geometry("400x400")
        screen2.title("Items")
        Label(screen2,font=('arial',13,'bold'),text="chocobar",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Vannila",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Chocolate",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Mint",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Blueberry",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Caramel",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Big mix",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Butterscotch",fg="black",bd=10,anchor=W).pack()
    def soups():
        screen2=Toplevel(screen1)
        screen2.geometry("400x400")
        screen2.title("Items")
        Label(screen2,font=('arial',13,'bold'),text="Bouillon soup",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Broth soup",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Cream soup",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Potage soup",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="corn soup",fg="black",bd=10,anchor=W).pack()
    def sandwich():
        screen2=Toplevel(screen1)
        screen2.geometry("400x400")
        screen2.title("Items")
        Label(screen2,font=('arial',13,'bold'),text="Paneer sandwich",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Cheese sandwich",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Grilled sandwich",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Club sandwich",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Potato sandwich",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Mushroom sandwich",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="chocolate sandwich",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="cucumber sandwich",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="curd sandwich",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Veg sandwich",fg="black",bd=10,anchor=W).pack()
    def salads():
        screen2=Toplevel(screen1)
        screen2.geometry("400x400")
        screen2.title("Items")
        Label(screen2,font=('arial',13,'bold'),text="Sprout salad",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Pasta salad",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Orzo salad",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Kale salad",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Greek salad",fg="black",bd=10,anchor=W).pack()
    def sweets():
        screen2=Toplevel(screen1)
        screen2.geometry("400x600")
        screen2.title("Items")
        Label(screen2,font=('arial',13,'bold'),text="Halwa",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Kaju barfi",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Laddu",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Jilebi",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Jangri",fg="black",bd=10,anchor=W).pack()               
        Label(screen2,font=('arial',13,'bold'),text="Putarekulu",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Rasgulla",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Mysore pak",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Palkova",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Kesari",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Badusha",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Kalakani",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Malai laddu",fg="black",bd=10,anchor=W).pack()
        Label(screen2,font=('arial',13,'bold'),text="Tokkudu laddu",fg="black",bd=10,anchor=W).pack()               
               



    btndrinks=Button(bottomm,padx=8,pady=8,fg='black',font=('arial bold',13),
                    width=6,text="Drinks",bg="grey",command=drinks).grid(row=1,column=0)
    btnjuice=Button(bottomm,padx=8,pady=8,fg='black',font=('arial bold',13),
                    width=6,text="Juices",relief=RAISED,bg="grey",command=juices).grid(row=2,column=0)
    btncakes=Button(bottomm,padx=8,pady=8,fg='black',font=('arial bold',13),
                    width=6,text="Cakes",relief=RAISED,bg="grey",command=cakes).grid(row=3,column=0)
    btnice_creams=Button(bottomm,padx=8,pady=8,fg='black',font=('arial bold',13),
                    width=6,text="Ice creams",relief=RAISED,bg="grey",command=ice_cream).grid(row=4,column=0)
    btnsoups=Button(bottomm,padx=8,pady=8,fg='black',font=('arial bold',13),
                    width=6,text="Soups",relief=RAISED,bg="grey",command=soups).grid(row=1,column=1)
    btnsalads=Button(bottomm,padx=8,pady=8,fg='black',font=('arial bold',13),
                    width=6,text="Salads",relief=RAISED,bg="grey",command=salads).grid(row=2,column=1)
    btnsandwich=Button(bottomm,padx=8,pady=8,fg='black',font=('arial bold',13),
                    width=6,text="Sandwich",relief=RAISED,bg="grey",command=sandwich).grid(row=3,column=1)
    btnsweets=Button(bottomm,padx=8,pady=8,fg='black',font=('arial bold',13),
                    width=6,text="Sweets",relief=RAISED,bg="grey",command=sweets).grid(row=4,column=1)


btntotal=Button(f2b,padx=8,pady=8,fg='black',font=('arial bold',13),
                width=6,text="Total",relief=RAISED,bg="grey",command=total).grid(row=0,column=0)
btnreset=Button(f2b,padx=8,pady=8,fg='black',font=('arial bold',13),
                width=6,text="Reset",relief=RAISED,bg='grey',command=reset).grid(row=0,column=1)
btnmenu=Button(f2b,padx=8,pady=8,fg='black',font=('arial bold',13),
                width=6,text="Menu",relief=RAISED,bg='grey',command=menu).grid(row=0,column=2)
btnreceipt=Button(f2b,padx=8,pady=8,fg='black',font=('arial bold',13),
                width=6,text="Receipt",relief=RAISED,bg='grey',command=receipt).grid(row=0,column=3)
btnquit=Button(f2b,padx=8,pady=8,fg='black',font=('arial bold',13),
                width=6,text="Exit",relief=RAISED,bg='grey',command=exit).grid(row=0,column=4)

#=========================================DRINKS===========================================
lussi=Checkbutton(f11a,text="Lussi",variable=var1,onvalue=1,offvalue=0,font=("arial bold",13),command=chkbutton).grid(row=0,column=0)
dalgona_coffee=Checkbutton(f11a,text="Dalgona coffee",variable=var2,onvalue=1,offvalue=0,font=("arial bold",13),command=chkbutton).grid(row=1,column=0)
flat_white=Checkbutton(f11a,text="Flat white",variable=var3,onvalue=1,offvalue=0,font=("arial bold",13),command=chkbutton).grid(row=2,column=0)
cappuccino=Checkbutton(f11a,text="Cappuccino",variable=var4,onvalue=1,offvalue=0,font=("arial bold",13),command=chkbutton).grid(row=3,column=0)
expresso=Checkbutton(f11a,text="Expresso",variable=var5,onvalue=1,offvalue=0,font=("arial bold",13),command=chkbutton).grid(row=4,column=0)
cold_coffee=Checkbutton(f11a,text="Cold coffee",variable=var6,onvalue=1,offvalue=0,font=("arial bold",13),command=chkbutton).grid(row=5,column=0)
butter_milk=Checkbutton(f11a,text="Butter Milk",variable=var7,onvalue=1,offvalue=0,font=("arial bold",13),command=chkbutton).grid(row=6,column=0)
lemonaid=Checkbutton(f11a,text="Lemonaid",variable=var8,onvalue=1,offvalue=0,font=("arial bold",13),command=chkbutton).grid(row=7,column=0)

txtlussi=Entry(f11a,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textlussi,bg="blue",fg="white")
txtlussi.grid(row=0,column=1)
txtdalgona_coffee=Entry(f11a,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textdalgona_coffee,bg="blue",fg="white")
txtdalgona_coffee.grid(row=1,column=1)
txtflat_white=Entry(f11a,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textflat_white,bg="blue",fg="white")
txtflat_white.grid(row=2,column=1)
txtcappuccino=Entry(f11a,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textcappuccino,bg="blue",fg="white")
txtcappuccino.grid(row=3,column=1)
txtexpresso=Entry(f11a,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textexpresso,bg="blue",fg="white")
txtexpresso.grid(row=4,column=1)
txtcold_coffee=Entry(f11a,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textcold_coffee,bg="blue",fg="white")
txtcold_coffee.grid(row=5,column=1)
txtbutter_milk=Entry(f11a,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textbutter_milk,bg="blue",fg="white")
txtbutter_milk.grid(row=6,column=1)
txtlemonaid=Entry(f11a,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textlemonaid,bg="blue",fg="white")
txtlemonaid.grid(row=7,column=1)
#============================================JUICES===========================================================================#
orange_juice=Checkbutton(f11a,text="Orange juice",variable=var17,onvalue=1,offvalue=0,font=("arial bold",13),command=chkbutton).grid(row=0,column=2)
apple_juice=Checkbutton(f11a,text="Apple juice",variable=var18,onvalue=1,offvalue=0,font=("arial bold",13),command=chkbutton).grid(row=1,column=2)
pineapple_juice=Checkbutton(f11a,text="Pineapple juice",variable=var19,onvalue=1,offvalue=0,font=("arial bold",13),command=chkbutton).grid(row=2,column=2)
carrot_juice=Checkbutton(f11a,text="Carrot juice",variable=var20,onvalue=1,offvalue=0,font=("arial bold",13),command=chkbutton).grid(row=3,column=2)
beetroot_juice=Checkbutton(f11a,text="Beetroot juice",variable=var21,onvalue=1,offvalue=0,font=("arial bold",13),command=chkbutton).grid(row=4,column=2)
banana_juice=Checkbutton(f11a,text="Banana juice",variable=var22,onvalue=1,offvalue=0,font=("arial bold",13),command=chkbutton).grid(row=5,column=2)
grape_juice=Checkbutton(f11a,text="Grape juice",variable=var23,onvalue=1,offvalue=0,font=("arial bold",13),command=chkbutton).grid(row=6,column=2)
strawberry_juice=Checkbutton(f11a,text="Stewberry juice",variable=var24,onvalue=1,offvalue=0,font=("arial bold",13),command=chkbutton).grid(row=7,column=2)

txtorange_juice=Entry(f11a,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textorange_juice,bg="blue",fg="white")
txtorange_juice.grid(row=0,column=3)
txtapple_juice=Entry(f11a,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textapple_juice,bg="blue",fg="white")
txtapple_juice.grid(row=1,column=3)
txtpineapple_juice=Entry(f11a,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textpineapple_juice,bg="blue",fg="white")
txtpineapple_juice.grid(row=2,column=3)
txtcarrot_juice=Entry(f11a,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textcarrot_juice,bg="blue",fg="white")
txtcarrot_juice.grid(row=3,column=3)
txtbeetroot_juice=Entry(f11a,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textbeetroot_juice,bg="blue",fg="white")
txtbeetroot_juice.grid(row=4,column=3)
txtbanana_juice=Entry(f11a,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textbanana_juice,bg="blue",fg="white")
txtbanana_juice.grid(row=5,column=3)
txtgrape_juice=Entry(f11a,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textgrape_juice,bg="blue",fg="white")
txtgrape_juice.grid(row=6,column=3)
txtstrawberry_juice=Entry(f11a,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textstrawberry_juice,bg="blue",fg="white")
txtstrawberry_juice.grid(row=7,column=3)
#============================================CAKES================================================
butter_cake=Checkbutton(f11b,text="Butter Cake",variable=var9,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=0,column=0)
pound_cake=Checkbutton(f11b,text="Pound Cake",variable=var10,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=1,column=0)
sponge_cake=Checkbutton(f11b,text="Sponge Cake",variable=var11,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=2,column=0)
genoise_cake=Checkbutton(f11b,text="Genoise Cake",variable=var12,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=3,column=0)
biscuit_cake=Checkbutton(f11b,text="Buiscui Cake",variable=var13,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=4,column=0)
Chiffon_cake=Checkbutton(f11b,text="Chiffon cake",variable=var14,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=5,column=0)
carrot_cake=Checkbutton(f11b,text="Carrot Cake",variable=var15,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=6,column=0)
red_velvet_cake=Checkbutton(f11b,text="Red Velvet Cake",variable=var16,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=7,column=0)
txtbutter_cake=Entry(f11b,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textbutter_cake,bg="blue",fg="white")
txtbutter_cake.grid(row=0,column=1)
txtpound_cake=Entry(f11b,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textpound_cake,bg="blue",fg="white")
txtpound_cake.grid(row=1,column=1)
txtsponge_cake=Entry(f11b,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textsponge_cake,bg="blue",fg="white")
txtsponge_cake.grid(row=2,column=1)
txtgenoise_cake=Entry(f11b,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textgenoise_cake,bg="blue",fg="white")
txtgenoise_cake.grid(row=3,column=1)
txtbiscuit_cake=Entry(f11b,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textbiscuit_cake,bg="blue",fg="white")
txtbiscuit_cake.grid(row=4,column=1)
txtchiffon_cake=Entry(f11b,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textchiffon_cake,bg="blue",fg="white")
txtchiffon_cake.grid(row=5,column=1)
txtcarrot_cake=Entry(f11b,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textcarrot_cake,bg="blue",fg="white")
txtcarrot_cake.grid(row=6,column=1)
txtred_velvet_cake=Entry(f11b,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textred_velvet_cake,bg="blue",fg="white")
txtred_velvet_cake.grid(row=7,column=1)
#==========================================ICE CREAMS=========================================================
chocobar=Checkbutton(f11b,text="Chocobar",variable=var25,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=0,column=2)
vannila=Checkbutton(f11b,text="Vannila",variable=var26,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=1,column=2)
chocolate =Checkbutton(f11b,text="Chocolate",variable=var27,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=2,column=2)
mint=Checkbutton(f11b,text="Mint",variable=var28,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=3,column=2)
blueberry=Checkbutton(f11b,text="Blueberry",variable=var29,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=4,column=2)
caramel=Checkbutton(f11b,text="Caramel",variable=var30,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=5,column=2)
big_mix=Checkbutton(f11b,text="Big mix",variable=var31,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=6,column=2)
butterscotch=Checkbutton(f11b,text="Butterscotch",variable=var32,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=7,column=2)
txtchocobar=Entry(f11b,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textchocobar,bg="blue",fg="white")
txtchocobar.grid(row=0,column=3)
txtvannila=Entry(f11b,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textvannila,bg="blue",fg="white")
txtvannila.grid(row=1,column=3)
txtchocolate=Entry(f11b,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textchocolate,bg="blue",fg="white")
txtchocolate.grid(row=2,column=3)
txtmint=Entry(f11b,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textmint,bg="blue",fg="white")
txtmint.grid(row=3,column=3)
txtblueberry=Entry(f11b,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textblueberry,bg="blue",fg="white")
txtblueberry.grid(row=4,column=3)
txtcaramel=Entry(f11b,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textcaramel,bg="blue",fg="white")
txtcaramel.grid(row=5,column=3)
txtbig_mix=Entry(f11b,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textbig_mix,bg="blue",fg="white")
txtbig_mix.grid(row=6,column=3)
txtbutterscotch=Entry(f11b,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textbutterscotch,bg="blue",fg="white")
txtbutterscotch.grid(row=7,column=3)
#======================================================SOUPS============================================================
bouillon_soup=Checkbutton(f12a,text="Bouillon soup",variable=var33,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=0,column=0)
broth_soup=Checkbutton(f12a,text="Broth soup",variable=var34,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=1,column=0)
cream_soup =Checkbutton(f12a,text="Cream soup",variable=var35,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=2,column=0)
potage_soup=Checkbutton(f12a,text="Potage soup",variable=var36,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=3,column=0)
corn_soup=Checkbutton(f12a,text="Corn soup",variable=var37,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=4,column=0)

txtbouillon_soup=Entry(f12a,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textbouillon_soup,bg="blue",fg="white")
txtbouillon_soup.grid(row=0,column=2)
txtbroth_soup=Entry(f12a,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textbroth_soup,bg="blue",fg="white")
txtbroth_soup.grid(row=1,column=2)
txtcream_soup=Entry(f12a,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textcream_soup,bg="blue",fg="white")
txtcream_soup.grid(row=2,column=2)
txtpotage_soup=Entry(f12a,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textpotage_soup,bg="blue",fg="white")
txtpotage_soup.grid(row=3,column=2)
txtcorn_soup=Entry(f12a,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textcorn_soup,bg="blue",fg="white")
txtcorn_soup.grid(row=4,column=2)
#================================================SALADS=======================================================
sprout_salad=Checkbutton(f12a,text="Sprout salad",variable=var38,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=0,column=3)
pasta_salad=Checkbutton(f12a,text="Pasta salad",variable=var39,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=1,column=3)
orzo_salad =Checkbutton(f12a,text="Orzo salad",variable=var40,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=2,column=3)
kale_salad=Checkbutton(f12a,text="Kale salad",variable=var41,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=3,column=3)
greek_salad=Checkbutton(f12a,text="Greek salad",variable=var42,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=4,column=3)

txtsprout_salad=Entry(f12a,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textsprout_salad,bg="blue",fg="white")
txtsprout_salad.grid(row=0,column=4)
txtpasta_salad=Entry(f12a,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textpasta_salad,bg="blue",fg="white")
txtpasta_salad.grid(row=1,column=4)
txtorzo_salad=Entry(f12a,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textorzo_salad,bg="blue",fg="white")
txtorzo_salad.grid(row=2,column=4)
txtkale_salad=Entry(f12a,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textkale_salad,bg="blue",fg="white")
txtkale_salad.grid(row=3,column=4)
txtgreek_salad=Entry(f12a,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textgreek_salad,bg="blue",fg="white")
txtgreek_salad.grid(row=4,column=4)

#=========================================SWEETS====================================================================
halwa=Checkbutton(f2a1,text="Halwa",variable=var43,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=0,column=0)
kaju_barfi=Checkbutton(f2a1,text="Kaju Barfi",variable=var44,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=1,column=0)
laddu =Checkbutton(f2a1,text="Laddu",variable=var45,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=2,column=0)
jilebi=Checkbutton(f2a1,text="Jilebi",variable=var46,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=3,column=0)
jangri=Checkbutton(f2a1,text="Jangri",variable=var47,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=4,column=0)
putarekulu=Checkbutton(f2a1,text="Putarekulu",variable=var53,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=5,column=0)
rasgulla=Checkbutton(f2a1,text="Rasgulla",variable=var54,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=6,column=0)
mysore_pak=Checkbutton(f2a1,text="Mysore pak",variable=var48,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=0,column=2)
palkova=Checkbutton(f2a1,text="Palkova",variable=var49,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=1,column=2)
kesari =Checkbutton(f2a1,text="Kesari",variable=var50,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=2,column=2)
badusha=Checkbutton(f2a1,text="Badusha",variable=var51,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=3,column=2)
kalakani=Checkbutton(f2a1,text="Kalakani",variable=var52,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=4,column=2)
malai_laddu=Checkbutton(f2a1,text="Malai laddu",variable=var55,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=5,column=2)
tokkudu_laddu=Checkbutton(f2a1,text="Tokkudu laddu",variable=var56,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=6,column=2)

txthalwa=Entry(f2a1,font=("arial bold",13),width=5,bd=6,justify=LEFT,state=DISABLED,textvariable=texthalwa,bg="blue",fg="white")
txthalwa.grid(row=0,column=1)
txtkaju_barfi=Entry(f2a1,font=("arial bold",13),width=5,bd=6,justify=LEFT,state=DISABLED,textvariable=textkaju_barfi,bg="blue",fg="white")
txtkaju_barfi.grid(row=1,column=1)
txtladdu=Entry(f2a1,font=("arial bold",13),width=5,bd=6,justify=LEFT,state=DISABLED,textvariable=textladdu,bg="blue",fg="white")
txtladdu.grid(row=2,column=1)
txtjilebi=Entry(f2a1,font=("arial bold",13),width=5,bd=6,justify=LEFT,state=DISABLED,textvariable=textjilebi,bg="blue",fg="white")
txtjilebi.grid(row=3,column=1)
txtjangri=Entry(f2a1,font=("arial bold",13),width=5,bd=6,justify=LEFT,state=DISABLED,textvariable=textjangry,bg="blue",fg="white")
txtjangri.grid(row=4,column=1)
txtputarekulu=Entry(f2a1,font=("arial bold",13),width=5,bd=6,justify=LEFT,state=DISABLED,textvariable=textputarekulu,bg="blue",fg="white")
txtputarekulu.grid(row=5,column=1)
txtrasgulla=Entry(f2a1,font=("arial bold",13),width=5,bd=6,justify=LEFT,state=DISABLED,textvariable=textrasgulla,bg="blue",fg="white")
txtrasgulla.grid(row=6,column=1)
txtmysore_pak=Entry(f2a1,font=("arial bold",13),width=5,bd=6,justify=LEFT,state=DISABLED,textvariable=textmysore_pak,bg="blue",fg="white")
txtmysore_pak.grid(row=0,column=3)
txtpalkova=Entry(f2a1,font=("arial bold",13),width=5,bd=6,justify=LEFT,state=DISABLED,textvariable=textpalkova,bg="blue",fg="white")
txtpalkova.grid(row=1,column=3)
txtkesari=Entry(f2a1,font=("arial bold",13),width=5,bd=6,justify=LEFT,state=DISABLED,textvariable=textkesari,bg="blue",fg="white")
txtkesari.grid(row=2,column=3)
txtbadusha=Entry(f2a1,font=("arial bold",13),width=5,bd=6,justify=LEFT,state=DISABLED,textvariable=textbadusha,bg="blue",fg="white")
txtbadusha.grid(row=3,column=3)
txtkalakani=Entry(f2a1,font=("arial bold",13),width=5,bd=6,justify=LEFT,state=DISABLED,textvariable=textkalakani,bg="blue",fg="white")
txtkalakani.grid(row=4,column=3)
txtmalai_laddu=Entry(f2a1,font=("arial bold",13),width=5,bd=6,justify=LEFT,state=DISABLED,textvariable=textmalai_laddu,bg="blue",fg="white")
txtmalai_laddu.grid(row=5,column=3)
txttokkudu_laddu=Entry(f2a1,font=("arial bold",13),width=5,bd=6,justify=LEFT,state=DISABLED,textvariable=texttokkudu_laddu,bg="blue",fg="white")
txttokkudu_laddu.grid(row=6,column=3)
#==========================================SANDWICHES===================================================================
paneer_sandwich=Checkbutton(f12b,text="Panner sandwich",variable=var57,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=0,column=0)
cheese_sandwich=Checkbutton(f12b,text="Cheese Sandwich",variable=var58,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=1,column=0)
grilled_sandwich =Checkbutton(f12b,text="Grilled sandwich",variable=var59,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=2,column=0)
club_sandwich=Checkbutton(f12b,text="Club sandwich",variable=var60,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=3,column=0)
potato_sandwich=Checkbutton(f12b,text="Potato sandwich",variable=var61,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=4,column=0)

txtpaneer_sandwich=Entry(f12b,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textpaneer_sandwich,bg="blue",fg="white")
txtpaneer_sandwich.grid(row=0,column=1)
txtcheese_sandwich=Entry(f12b,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textcheese_sandwich,bg="blue",fg="white")
txtcheese_sandwich.grid(row=1,column=1)
txtgrilled_sandwich=Entry(f12b,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textgrilled_sandwich,bg="blue",fg="white")
txtgrilled_sandwich.grid(row=2,column=1)
txtclub_sandwich=Entry(f12b,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textclub_sandwich,bg="blue",fg="white")
txtclub_sandwich.grid(row=3,column=1)
txtpotato_sandwich=Entry(f12b,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textpotato_sandwich,bg="blue",fg="white")
txtpotato_sandwich.grid(row=4,column=1)

mushroom_sandwich=Checkbutton(f12b,text="Mushroom sandwich",variable=var62,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=0,column=2)
chocolate_sandwich=Checkbutton(f12b,text="chocolate sandwich",variable=var63,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=1,column=2)
cucumber_sandwich =Checkbutton(f12b,text="Cucumber sandwich",variable=var64,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=2,column=2)
curd_sanwich=Checkbutton(f12b,text="curd sandwich",variable=var65,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=3,column=2)
veg_sandwich=Checkbutton(f12b,text="Veg sandwich",variable=var66,onvalue=1,offvalue=0,
                    font=("arial bold",13),command=chkbutton).grid(row=4,column=2)

txtmushroom_sandwich=Entry(f12b,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textmushroom_sandwich,bg="blue",fg="white")
txtmushroom_sandwich.grid(row=0,column=3)
txtchocolate_sandwich=Entry(f12b,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textchocolate_sandwich,bg="blue",fg="white")
txtchocolate_sandwich.grid(row=1,column=3)
txtcucumber_sandwich=Entry(f12b,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textcucumber_sandwich,bg="blue",fg="white")
txtcucumber_sandwich.grid(row=2,column=3)
txtcurd_sandwich=Entry(f12b,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textcurd_sanwich,bg="blue",fg="white")
txtcurd_sandwich.grid(row=3,column=3)
txtveg_sandwich=Entry(f12b,font=("arial bold",13),width=8,bd=8,justify=LEFT,state=DISABLED,textvariable=textveg_sandwich,bg="blue",fg="white")
txtveg_sandwich.grid(row=4,column=3)
#===================================BILLING========================================================================
textentry1=IntVar()
textentry2=IntVar()
textentry3=IntVar()
label1=Label(f2a2,text="cost of food",font=("arial bold",14)).grid(row=0,column=0)
entry1=Entry(f2a2,font=("arial bold",14),width=12,bd=8,textvariable=textentry1)
entry1.grid(row=0,column=1)
label2=Label(f2a2,text="service charges",font=("arial bold",14)).grid(row=1,column=0)
entry2=Entry(f2a2,font=("arial bold",14),width=12,bd=8,textvariable=textentry2)
entry2.grid(row=1,column=1)
label3=Label(f2a2,text="Total bill",font=("arial bold",15)).grid(row=2,column=0)
entry3=Entry(f2a2,font=("arial bold",14),width=12,bd=8,textvariable=textentry3)
entry3.grid(row=2,column=1)

root.mainloop()