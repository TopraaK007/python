# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
class Sirket():
    def __init__(self,ad):
        self.ad=ad
        self.calisma= True

    def program(self):
        secim = self.menu_secim()

        if secim==1:
            self.calisan_ekle()
        if secim==2:
            self.calisan_cikar()
        if secim==3:
            ay_yilsecim=input("Yıllık bazda görmek ister misiniz? (Evet/Hayır) ")
            if ay_yilsecim=="Evet":
                self.verilecek_maas("y")
            else:
                self.verilecek_maas()
        if secim==4:
            self.maaslari_ver()
        if secim==5:
            self.masraf_gir()
        if secim==6:
            self.gelir_gir()

    def menu_secim(self):
            secim = int(input("*** {}Otomasyonuna Hoş Geldiniz *** \n\n1-Çalışan Ekle\n2-Çalışan Çıkar\n3-Verilecek Maaşı Göster\n4-Maaşları Ver\n5-Masraf Gİr\n6-Gelir Gİr\n\nSeçimlerinizi Girniz:".format( self.ad)))
            while secim<1 or secim>6:
                secim=int(input("1-6 arasında sayı giriniz"))
            return secim


    def calisan_ekle(self):
        id = 1
        ad = input("Çalışan adı gir:")
        soyad =input(("Çalışan soyad gir:"))
        yas = input(("Çalışan yaş    gir:"))
        maas = input(("Çalışan maaş gir:"))
        cinsiyet = input(("Çalışan cinsiyet gir:"))
    # bunu yaparak dosyamızı hem okuyup hem yazıcaz alttaki işlem ise readlines satırları okucak satır yoksa boş liste döndürecek
        with open("calisanlar.txt","r") as dosya:
            calisan_listesi=dosya.readlines()
        if len(calisan_listesi)==0:
            id=1
        else:
            with open("calisanlar.txt","r") as dosya:
                id=int(dosya.readlines()[-1].split(")")[0]) + 1


        with open("calisanlar.txt","a+") as dosya:
            dosya.write("{}){}-{}-{}-{}-{}\n".format(id,ad,soyad,yas,maas,cinsiyet))


    def calisan_cikar(self):
        with open("calisanlar.txt","r") as dosya:
            calisanlarr=dosya.readlines()

        gcalisanlar=[]

        for calisan in calisanlarr:
            gcalisanlar.append(" ".join(calisan[:-1].split("-")))

        for calisan in gcalisanlar:
            print(calisan)

        secim=int(input("Lütfen çıkarmak istedğiniz elemanın numarasını giriniz:(1-{}:".format(len(gcalisanlar))))
        while secim < 1 or secim>len(gcalisanlar):
            secim=int(input("Lütfen 1-{} arasında numara giriniz:".format(len(gcalisanlar))))
        calisanlarr.pop(secim-1)

        değisen_calisanlar=[]
        sayac=1
        for calisan in calisanlarr:
            değisen_calisanlar.append(str(sayac)+")"+calisan.split(")")[1])
            sayac+=1
        with open("calisanlar.txt","w") as dosya:
            dosya.writelines(değisen_calisanlar)



    def verilecek_maas(self,hesap="a"):
        '''hesap a ise aylık y ise yıllık maaşı'''
        with open("calisanlar.txt","r") as dosya:
            calisanlar=dosya.readlines()

        maaslar=[]

        for calisan in calisanlar:
            maaslar.append(int(calisan.split("-")[-2]))
        if hesap=="a":
            print("Bu ay ödenecek maaş: {}".format(sum(maaslar)))
        else:
            print("Yıllık verilecek maaş:{}".format(sum(maaslar)*12))


    def maaslari_ver(self):
        with open("calisanlar.txt","r") as dosya:
            calisanlar=dosya.readlines()

        maaslar=[]

        for calisan in calisanlar:
            maaslar.append(int(calisan.split("-")[-2]))
        tpl_maas=sum(maaslar)

        with open("butce.txt","r") as dosya:
            tbutce=int(dosya.readlines()[0])

        tbutce=tbutce-tpl_maas

        with open("butce.txt","w") as dosya:
            dosya.write(str(tbutce))

    def masraf_gir(self):
        masraf_t=input("Masrafın türünü  giriniz:")

        masraf_gideri = int(input("Ödenecek Tutarı Girin:"))

        with open("masraflar.txt","a+") as dosya:
            dosya.write("-{}={}\n".format(masraf_t,masraf_gideri))

    def gelir_gir(self):
        gelir_t=input("Gelir Türünü Gİriniz:")

        gelir_miktari=int(input("Gelir Miktarını giriniz: "))

        with open("gelirler.txt","a+") as dosya:
            dosya.write("-{}={}\n".format(gelir_t,gelir_miktari))


sirket=Sirket("Toprak ")
while sirket.calisma:
        sirket.program()
