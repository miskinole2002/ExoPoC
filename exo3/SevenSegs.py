
from time import sleep


class SevenSegs():

    def __init__(self,Sa,Sb,Sc,Sd,Se,Sf,Sg,type):
        self.__Sa=Sa
        self.__Sb=Sb
        self.__Sc=Sc
        self.__Sd=Sd
        self.__Se=Se
        self.__Sf=Sf
        self.__Sg=Sg
        self.__Type=type
    

    @property
    def SA(self):
        return self.__Sa
    
    def SB(self):
        return self.__Sb
    
    def SC(self):
        return self.__Sc
    
    def SD(self):
        return self.__Sd
    def SE(self):
        return self.__Se
    def SF(self):
        return self.__Sf
    def SG(self):
        return self.__Sg
    def Type(self):
        return self.__Type

    #@SA.setter
    def SA(self,a):
        self.__Sa=a
    #@SB.setter
    def SB(self,b):
        self.__Sb=b
    #@SC.setter
    def SC(self,c):
        self.__Sc=c
    #@SD.setter
    def SD(self,d):
        self.__Sd=d
    #@SE.setter
    def SE(self,e):
        self.__Se=e
    #@SF.setter
    def SF(self,f):
        self.__Sf=f
    #@Type.setter
    def TYpe(self,t):
        self.__Type=t


    
    def Show0(self):
        if self.__Type==True:
             self.__Sa.on()
             self.__Sb.on()
             self.__Sc.on()
             self.__Sd.on()
             self.__Se.on()
             self.__Sf.on()
             self.__Sg.off()
        else:
             self.__Sa.off()
             self.__Sb.off()
             self.__Sc.off()
             self.__Sd.off()
             self.__Se.off()
             self.__Sf.off()
             self.__Sg.on()
 
    def Show1(self):
        if self.__Type==True:
             self.__Sa.off()
             self.__Sb.off()
             self.__Sc.off()
             self.__Sd.off()
             self.__Se.on()
             self.__Sf.on()
             self.__Sg.off()
        else:
             self.__Sa.on()
             self.__Sb.on()
             self.__Sc.on()
             self.__Sd.on()
             self.__Se.off()
             self.__Sf.off()
             self.__Sg.on()

    def Show2(self):
        if self.__Type==True:
             self.__Sa.on()
             self.__Sb.on()
             self.__Sc.off()
             self.__Sd.on()
             self.__Se.on()
             self.__Sf.off()
             self.__Sg.on()
        else:
             self.__Sa.off()
             self.__Sb.off()
             self.__Sc.on()
             self.__Sd.off()
             self.__Se.off()
             self.__Sf.on()
             self.__Sg.off()

    def Show3(self):
      if self.__Type==True:
             self.__Sa.on()
             self.__Sb.on()
             self.__Sc.on()
             self.__Sd.on()
             self.__Se.off()
             self.__Sf.off()
             self.__Sg.on()
      else:
             self.__Sa.off()
             self.__Sb.off()
             self.__Sc.off()
             self.__Sd.off()
             self.__Se.on()
             self.__Sf.on()
             self.__Sg.off()


    def Show4(self):
        if self.__Type==True:
                self.__Sa.off()
                self.__Sb.on()
                self.__Sc.on()
                self.__Sd.off()
                self.__Se.off()
                self.__Sf.on()
                self.__Sg.on()
        else:
                self.__Sa.on()
                self.__Sb.off()
                self.__Sc.on()
                self.__Sd.on()
                self.__Se.on()
                self.__Sf.on()
                self.__Sg.off()
    


    def Show5(self):
    
        if self.__Type==True:
                self.__Sa.on()
                self.__Sb.off()
                self.__Sc.on()
                self.__Sd.on()
                self.__Se.off()
                self.__Sf.on()
                self.__Sg.on()
        else:
                self.__Sa.off()
                self.__Sb.on()
                self.__Sc.off()
                self.__Sd.off()
                self.__Se.off()
                self.__Sf.off()
                self.__Sg.off()

    def Show6(self):
        if self.__Type==True:
                self.__Sa.on()
                self.__Sb.off()
                self.__Sc.on()
                self.__Sd.on()
                self.__Se.on()
                self.__Sf.on()
                self.__Sg.on()
        else:
                self.__Sa.off()
                self.__Sb.on()
                self.__Sc.off()
                self.__Sd.off()
                self.__Se.off()
                self.__Sf.off()
                self.__Sg.off()
 

    def Show7(self):
        if self.__Type==True:
                    self.__Sa.on()
                    self.__Sb.on()
                    self.__Sc.on()
                    self.__Sd.off()
                    self.__Se.off()
                    self.__Sf.off()
                    self.__Sg.off()
        else:
                    self.__Sa.off()
                    self.__Sb.off()
                    self.__Sc.off()
                    self.__Sd.on()
                    self.__Se.on()
                    self.__Sf.on()
                    self.__Sg.on()
    



    def Show8(self):
        if self.__Type==True:
                self.__Sa.on()
                self.__Sb.on()
                self.__Sc.on()
                self.__Sd.on()
                self.__Se.on()
                self.__Sf.on()
                self.__Sg.on()
        else:
                self.__Sa.off()
                self.__Sb.off()
                self.__Sc.off()
                self.__Sd.off()
                self.__Se.off()
                self.__Sf.off()
                self.__Sg.off()
    def Show9(self):
        if self.__Type==True:
                    self.__Sa.on()
                    self.__Sb.on()
                    self.__Sc.on()
                    self.__Sd.on()
                    self.__Se.off()
                    self.__Sf.on()
                    self.__Sg.on()
        else:
                    self.__Sa.off()
                    self.__Sb.off()
                    self.__Sc.off()
                    self.__Sd.off()
                    self.__Se.on()
                    self.__Sf.off()
                    self.__Sg.off()

    def cout_up(self):
    #0
        self.Show0()
        sleep(1)
        self.Show1()    
        sleep(1)

            #2
        self.Show2() 
        sleep(1)

            #3
        self.Show3()  
        sleep(1)
                
            #4
        self.Show4()
        sleep(1)

            #5
        self.Show5()
        sleep(1)

            #6
        self. Show6() 
        sleep(1)

            #7
        self.Show7() 
        sleep(1)


            #8
        self. Show8()  
        sleep(1)


            #9
        self. Show9()
        sleep(1)
        
        self:ShowA()
        sleep(1)


    def cout_down(self):
        self. Show9()
        sleep(1)
        self. Show8()
        sleep(1)
        self. Show7()
        sleep(1)
        self. Show6()
        sleep(1)
        self. Show5()
        sleep(1)
        self. Show4()
        sleep(1)
        self. Show3()
        sleep(1)
        self. Show2()
        sleep(1)
        self. Show1()
        sleep(1)
        self. Show0()
        sleep(1)

    def ShowL(self):
        if self.__Type==True:
             self.__Sa.off()
             self.__Sb.off()
             self.__Sc.off()
             self.__Sd.on()
             self.__Se.on()
             self.__Sf.on()
             self.__Sg.off()
        else:
             self.__Sa.on()
             self.__Sb.on()
             self.__Sc.on()
             self.__Sd.off()
             self.__Se.off()
             self.__Sf.off()
             self.__Sg.on()
    
    def ShowH(self):
        if self.__Type==True:
             self.__Sa.off()
             self.__Sb.on()
             self.__Sc.on()
             self.__Sd.off()
             self.__Se.on()
             self.__Sf.on()
             self.__Sg.on()
        else:
             self.__Sa.on()
             self.__Sb.off()
             self.__Sc.off()
             self.__Sd.on()
             self.__Se.off()
             self.__Sf.off()
             self.__Sg.on()

    def Clear(self):
        if self.__Type==True:
             self.__Sa.off()
             self.__Sb.off()
             self.__Sc.off()
             self.__Sd.off()
             self.__Se.off()
             self.__Sf.off()
             self.__Sg.off()
        else:
             self.__Sa.on()
             self.__Sb.on()
             self.__Sc.on()
             self.__Sd.on()
             self.__Se.on()
             self.__Sf.on()
             self.__Sg.on()