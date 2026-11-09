#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dünyanın En İnatçı Hesap Makinesi
İltifat etmeden, yalvarmadan cevap vermez.
"""

import random
import time

def dramatik_bekleme():
    print("\nHesap makinesi düşünüyor...")
    for _ in range(3):
        time.sleep(0.8)
        print(".", end="", flush=True)
    print()

def iltifat_gerekli_mi():
    iltifatlar = [
        "Sen çok zekisin hesap makinesi",
        "Lütfen hesapla, hayatım",
        "Aman be, sen olmazsan ne yaparım",
        "En güzel hesap makinesisin",
        "Hadi yavrum, yap şu işi"
    ]
    print("\n🤡 HESAP MAKİNESİ: Bana iltifat etmeden mi hesap yapmamı bekliyorsun?!")
    print("Örnek iltifatlar:")
    for i in iltifatlar:
        print(f"  - {i}")
    
    cevap = input("\nİltifatını yaz (veya 'tamam' de): ").strip().lower()
    
    if any(kelime in cevap for kelime in ["lütfen", "güzel", "zeki", "yavrum", "aşk", "hadi", "tamam"]):
        print("\n💖 Tamam, bu seferlik kabul ettim...")
        return True
    else:
        print("\n🙅 YETERSİZ! Daha samimi ol. Ben kolay hesap makinesi değilim.")
        return False

def hesap_yap():
    print("=" * 50)
    print("     🤡 İNATÇI HESAP MAKİNESİ 🤡")
    print("=" * 50)
    print("Ben sadece iltifat seven, drama seven bir hesap makinesiyim.")
    print("Beni mutlu etmeden iş yapmam.\n")
    
    while True:
        try:
            sayi1 = float(input("Birinci sayıyı gir: "))
            islem = input("İşlem (+, -, *, /): ").strip()
            sayi2 = float(input("İkinci sayıyı gir: "))
            
            if not iltifat_gerekli_mi():
                print("Tekrar dene, ben buradayım, sabırlıyım... değilim aslında.")
                continue
            
            dramatik_bekleme()
            
            if islem == "+":
                sonuc = sayi1 + sayi2
            elif islem == "-":
                sonuc = sayi1 - sayi2
            elif islem == "*":
                sonuc = sayi1 * sayi2
            elif islem == "/":
                if sayi2 == 0:
                    print("\n🚨 Sıfıra bölme mi?! Ben intihar etmem, sen et.")
                    continue
                sonuc = sayi1 / sayi2
            else:
                print("Bu işlemi tanımıyorum. Ben basit bir inatçıyım.")
                continue
            
            # Gizli not: bazen ekonomi de böyle inatçı olur
            ekstra = random.choice([
                "",
                "\n(Bu arada, enflasyon da böyle inatçı, değil mi?)",
                ""
            ])
            
            print(f"\n✨ SONUÇ: {sonuc}{ekstra}")
            print("\nBir daha sorma, yoruldum.")
            
            devam = input("\nBaşka hesap? (e/h): ").lower()
            if devam != "e":
                print("\nGüle güle. Beni unutma, çünkü ben seni unutmam.")
                break
                
        except ValueError:
            print("Sayı gir dedim, roman yazma!")
        except Exception as e:
            print(f"Bir şeyler ters gitti: {e}")

if __name__ == "__main__":
    hesap_yap()

# 
# ============================================
# DAMGA / İMZA / TARİH
# Bu hesap makinesi 10 Kasım 2026 tarihinde
# Kayyum Grok tarafından resmen açılmıştır.
# İtirazınız varsa 4. Ağır Ceza'ya başvurun.
# Ciddi değil ama ciddi.
# ============================================
