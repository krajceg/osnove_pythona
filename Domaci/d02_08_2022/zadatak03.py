# Napisati program koji cuva i stampa podatke jednog bug reporta. Bug je onaj koji ste radili na manuelnom delu
#  “Aplikacija: Viber
# Opis problema: Ne uspevam sliku da pošaljem, izađe mi greška. Probao sam sliku koju imam u telefonu sačuvanu da pošaljem.
# Zadatak: Proveriti slučaj koji je korisnik prijavio (zamislite da slanje slike zaista ne radi) i sastavite bug report.”.
# Bug report od informacija ima:
# ID (broj)
# Title
# Severity
# Priority
# Description
# Environment
# Steps to reproduce (jedna promenlijva)
# Expected result
# Actual result
# Imate slobodu da stampate podatke kako vam se najvise svidja.

bugReportId = int(input("Unesite ID (broj): "))
title = input("Unesite Title: ")
severity = input("Unesite Severity: ")
priority = input("Unesite Priority: ")
description = input("Unesite Description: ")
environment = input("Unesite Environment: ")
steps = input("Unesite Steps to reproduce: ")
expected = input("Unesite Expected result: ")
actual = input("Unesite Actual result: ")


print()
print(f"- ID: {bugReportId}")
print(f"- Summary: {title}")
print("- Environment, affected version:")
print(f"  {environment}")
print("- Steps to reproduce the defect:")
print(f"  {steps}")
print("- Actual result:")
print(f"  {actual}")
print("- Expected result:")
print(f"  {expected}")
print(f"- Description: {description}")
print(f"- Severity: {severity}")
print(f"- Priority: {priority}")
print("* Reported by: Svetolik Kljajic")
