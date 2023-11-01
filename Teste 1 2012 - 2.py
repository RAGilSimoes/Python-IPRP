pH = float(input("Introduz o pH da solução química: "))

if pH < 7:
    print("A solução química de pH ", pH, " é uma solução ácida.")
elif pH == 7:
    print("A solução química de pH ", pH, " é uma solução neutra.")
elif pH > 7:
    print("A solução química de pH ", pH, " é uma solução básica.")