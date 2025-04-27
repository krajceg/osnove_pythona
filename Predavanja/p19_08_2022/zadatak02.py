from radnik import Radnik

radnik1 = Radnik()

radnik1.set_jmbg(12345677)
radnik1.set_ime_prezime("Svetolik Kljajic")
radnik1.set_broj_dece(0)
radnik1.set_stepen_strucne_spreme(7)
radnik1.set_godine_radnog_staza(2)

print(radnik1.plata_radnika())
print(radnik1.kreditno_sposoban())
