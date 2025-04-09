from slackPoruke import slackMessage

poruka1 = slackMessage("Sveta je legenda", "Tamara Milic", "09.04.2025. 01:17")

poruka2 = slackMessage("Sveta voli Tamaru",
                       "Svetolik Kljajic", "09.04.2025. 01.18")

# print(f"{poruka1.imeIPrezime} - {poruka1.datumIVreme}")
# print(poruka1.tekstPoruke)
# print()
# print(f"{poruka2.imeIPrezime} - {poruka2.datumIVreme}")
# print(poruka2.tekstPoruke)

poruka1.stampaj()
poruka2.stampaj()
