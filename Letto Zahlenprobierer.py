from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tkinter as tk
from tkinter import messagebox
import time



aufgabeNr=1         # Auswahl der Aufgabe
beispielNr=2        # Auswahl des Beispiels
feldNr=1            # Auswahl des Feldes

anfangswert=0       # wähle den Anfangswert
endwert=1000           # wähle den Endwert
schrittweite=10   # wähle die Schrittweite
einheit="Hz"          # wähle die Einheit







# WebDriver starten (z. B. Chrome)
driver = webdriver.Firefox()  # oder webdriver.Firefox() für Firefox
driver.get("https://letto.htlstp.ac.at/lettohtlstp/letto/login.jsf")  # URL deiner Letto-Software

# Warte kurz, bis die Seite geladen ist
time.sleep(3)

# Beispiel: Anmeldedaten eingeben
username_field = driver.find_element(By.ID, "j_idt22:username")  # ID des Benutzernamenfelds
password_field = driver.find_element(By.ID, "j_idt22:pwd")  # ID des Passwortfelds

username_field.send_keys("erwin.mot")
password_field.send_keys("Aderleiste30")


button1 = driver.find_element(By.ID, "j_idt22:login")  
button1.click()

time.sleep(3)

button2 = driver.find_element(By.ID, "j_idt359:j_idt361:" + str(aufgabeNr - 1) + ":j_idt378")  
button2.click()

time.sleep(3)
button3 = driver.find_element(By.ID, "j_idt999:j_idt1001:0:j_idt1018")  
button3.click()



for n in range (beispielNr - 1):

    time.sleep(5)
    button4 = driver.find_element(By.ID, "questionForm:j_idt611")  
    button4.click()


time.sleep(3)


j=anfangswert - schrittweite
while j<endwert:

    button6 = driver.find_element(By.ID, "questionForm:pruefen")  # ID des Buttons
    feld1 = driver.find_element(By.ID, "questionForm:mcq:" + str(feldNr-1) + ":inpCq")
    
    feld1.clear()
    j=j + schrittweite
    round(j,3)
    feld1.send_keys(j, einheit)
    button6.click()
    
    time.sleep(6)

    span_element = driver.find_element(By.XPATH, "//span[input[@id='questionForm:mcq:" + str(feldNr-1) + ":inpCq']]")
    span_class = span_element.get_attribute("class")
    
    if (span_class == "ergTrue ui-inputwrapper-filled"):
        print("Richtiger Wert gefunden!")

        # Funktion, um den Alert zu zeigen
        def show_alert():
            # Neues Tkinter-Fenster erstellen (wird für messagebox benötigt, aber bleibt unsichtbar)
            root = tk.Tk()
            root.withdraw()  # Versteckt das Hauptfenster

            # Zeige die Alert-Message
            messagebox.showinfo("Hinweis", "Richtiger Wert gefunden!")

            # Hauptfenster zerstören
            root.destroy()

        # Alert-Fenster anzeigen
        show_alert()
        break 
    

    
