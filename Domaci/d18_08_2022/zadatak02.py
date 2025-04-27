from FacebookPostovi import facebookPost

facebookPost1 = facebookPost()
facebookPost1.imeIPrezimeObjavio = "Svetolik Kljajic"
facebookPost1.imeIprezimeNaProfilu = "Mitar Miric"
facebookPost1.tekstObjave = "Sta ima"
facebookPost1.brojLajkova = 10
facebookPost1.brojDeljenja = 5

facebookPost1.like()
facebookPost1.like()
facebookPost1.like()
facebookPost1.dislike()
facebookPost1.share()
facebookPost1.share()

facebookPost1.print()
print()
