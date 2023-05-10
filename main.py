import os
import subprocess
import smtplib
import datetime

def flash_disk_bilgileri():
    sürücüler = [chr(i) + ":" for i in range(0, 30)]
    bilgiler = []
    for sürücü in sürücüler:
        if os.path.exists(sürücü):
            boyut = os.path.getsize(sürücü)
            tarih = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            dosyalar = os.listdir(sürücü)
            bilgiler.append((sürücü, tarih, boyut, dosyalar))
    return bilgiler
def ekrana_yazdir(bilgiler):
    for sürücü, tarih, boyut, dosyalar in bilgiler:
        print(f"Flash disk takıldı: {tarih}")
        print(f"Sürücü: {sürücü}")
        print(f"Boyut: {boyut} byte")
        print(f"Dosyalar: {dosyalar}")
def eposta_gönder(bilgiler, gönderen, alici, sifre):
    mesaj = "Subject: Flash Disk Bilgileri\n\n"
    for sürücü, tarih, boyut, dosyalar in bilgiler:
        mesaj += f"Flash disk takıldı: {tarih}\n"
        mesaj += f"Sürücü: {sürücü}\n"
        mesaj += f"Boyut: {boyut} byte\n"
        mesaj += f"Dosyalar: {', '.join(dosyalar)}\n\n"
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(gönderen, sifre)
        server.sendmail(gönderen, alici, mesaj)
        server.quit()
        print("E-posta başarıyla gönderildi!")
    except:
        print("E-posta gönderme hatası!")
bilgiler = flash_disk_bilgileri()
ekrana_yazdir(bilgiler)
gonderen = 'gonderen@mail.com'
alici = 'alici@mail.com'
sifre = 'sifre'
eposta_gönder(bilgiler
