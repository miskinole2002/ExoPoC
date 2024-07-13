from tkinter   import*
from gpiozero import LED
from gpiozero import Button as button
from SevenSegs import SevenSegs
from time import sleep
#from tkinter import Button as button

class AlarmSyst():
    
    def Act(self):
            if(self.status==True):
                self.led.on()
                sleep(1)
                self.status=False
               # self.btnOn.config(text="ON",bg="green")
     
    def Deact(self):
        if(self.status==False):
            self.afficheur.cout_down
            self.led.off()
          #  self.btnOn.config(text="off",bg="red")
            self.status=True
            
    def IntruONOFF(self):
        if(self.status==False):
           if (self.statusLbl==True):
               self.btnOn.config(text="on",bg="red")
               self.lblZ1.config(bg="green")
               self.lblZ2.config(bg="green")
               self.lblZ3.config(bg="green")
               self.lblZ4.config(bg="green")
               self.led.off()
               self.led.on()
        
              # self.statusLbl=True
           else:
                
               self.lblZ1.config(bg="red")
               self.lblZ2.config(bg="red")
               self.lblZ3.config(bg="red")
               self.lblZ4.config(bg="red")
               self.btnOn.config(text="off",bg="red")
               self.statusLbl=False
               
     #checkZ1-Z4
    def CheckZone(self):
            if(self.status==False):
                if (self.Z1.is_pressed==True):
                    self.afficheur.Show1
                    self.led.blink()
                    sleep(1)
                    self.lblZ1.config(bg="red")
                    self.btnOn.config(text="off",bg="green")
                    self.statusLbl=True
                    #
                elif (self.Z2.is_pressed==True):
                    self.afficheur.Show2
                    self.lblZ2.config(bg="red")
                    self.btnOn.config(text="off",bg="green")
                    self.led.blink()
                    sleep(1)
                    self.statusLbl=True
                    
                elif (self.Z3.is_pressed==True):
                    self.afficheur.Show3
                    self.lblZ3.config(bg="red")
                    self.btnOn.config(text="off",bg="green")
                    self.led.blink()
                    sleep(1)
                    self.statusLbl=True
                
                elif (self.Z4.is_pressed==True):
                    self.afficheur.Show1
                    self.led.blink()
                    sleep(1)
                    self.lblZ4.config(bg="red")
                    self.btnOn.config(text="off",bg="green")
                    self.statusLbl=True
                elif(self.reset.is_pressed==True):
                    self.led.off()
     
    def Reset(self):
        self.affiche.clear()
        self.led.Off()
    def __init__(self,root):
        
        self.status= True
        self.statusLbl=False
        self.tk=root
        self.Z1=button(22)
        self.Z2=button(5)
        self.Z3=button(6)
        self.Z4=button(19)
        self.reset=button(27)
        self.led=LED(2)
         
        self.afficheur=SevenSegs(8,9,10,11,12,13,17,False)

        self.tilte=Label(self.tk,text="PI security GUI",bg="green")
        self.tilte.grid(row=0,columnspan=3)

        #Z1
        self.lblZ1=Label(self.tk,text="Z1",bg="green")
        self.lblZ1.grid(row=1,column=1)

        #Z2
        self.lblZ2=Label(self.tk,text="Z2",bg="green")
        self.lblZ2.grid(row=1,column=2)

        #Z3
        self.lblZ3=Label(self.tk,text="Z3",bg="green")
        self.lblZ3.grid(row=2,column=1)
        #Z4
        self.lblZ4=Label(self.tk,text="Z4",bg="green")
        self.lblZ4.grid(row=2,column=2)
        #button on/off
        self.btnOn=Button(self.tk,text="ON",command=lambda:self.IntruONOFF())
        self.btnOn.grid(row=3,columnspan=2,column=2)

         #button Activate
        self.act=Button(self.tk,text="activate",command=lambda:self.Act())
        self.act.grid(row=1,column =5,columnspan=3)

        #button deActivate
        self.deAct=Button(self.tk,text="deactivate",command=lambda:self.Deact())
        self.deAct.grid(row=2,column =5,columnspan=3)

        #button Reset
        self.Reset=Button(self.tk,text="Reset",command=lambda:self.Reset())
        self.Reset.grid(row=3,column =5,columnspan=3)
        self.Z1.when_pressed=self.CheckZone
        self.Z2.when_pressed=self.CheckZone
        self.Z3.when_pressed=self.CheckZone
        self.Z4.when_pressed=self.CheckZone
        self.tk.mainloop()
        
       
        
       
                    
                    
           
       
        

            