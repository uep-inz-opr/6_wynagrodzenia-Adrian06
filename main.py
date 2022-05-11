class Pracownik:
	def __init__(self, imie, wyn_brutto):
		self.imie = imie
		self.wyn_brutto = wyn_brutto

	def wyn_netto(self):
		skl_emeryt = round(self.wyn_brutto * 0.0976, 2)
		skl_rent = round(self.wyn_brutto * 0.015, 2)
		skl_chor = round(self.wyn_brutto * 0.0245, 2)
		skl_full = round(skl_emeryt + skl_rent + skl_chor, 2)


		podstawa = round(self.wyn_brutto - skl_full, 2)

		skl_zdrow = round(podstawa * 0.09, 2)
		skl_zdrow_do_odliczenia = round(podstawa * 0.0775, 2)

		podstawa_zaliczki = round(self.wyn_brutto - 111.25 - skl_full)

		zaliczka_przed = round((podstawa_zaliczki * 0.18) - 46.33, 2)
		zaliczka_na_podatek = round(zaliczka_przed - skl_zdrow_do_odliczenia)

		netto = round(self.wyn_brutto - skl_full - skl_zdrow - zaliczka_na_podatek, 2)
		return float(netto)

	def skladki_pracodawcy(self):
		skl_emeryt = round(self.wyn_brutto * 0.0976, 2)
		skl_rent = round(self.wyn_brutto * 0.065, 2)
		skl_wyp = round(self.wyn_brutto * 0.0193, 2)
		skl_fp = round(self.wyn_brutto * 0.0245, 2)
		skl_fgsp = round(self.wyn_brutto * 0.001, 2)

		skl_prac_full = round(skl_emeryt + skl_rent + skl_wyp + skl_fp + skl_fgsp, 2)
		return float(skl_prac_full)

laczny_koszt = 0
pracownicy = {}
i = int(input())

for x in range(i):
	imie, pensja = input().split()
	pracownicy[x] = {'imie': imie, 'pensja': int(pensja)}

for id in pracownicy:
	pracownik = Pracownik(pracownicy[id]['imie'], pracownicy[id]['pensja'])
	laczny_koszt += pracownicy[id]['pensja'] + pracownik.skladki_pracodawcy()
	print(f"{pracownicy[id]['imie']} {pracownik.wyn_netto():.2f} {pracownik.skladki_pracodawcy()} {round(pracownicy[id]['pensja'] + pracownik.skladki_pracodawcy(), 2)}")

print(round(laczny_koszt, 2))