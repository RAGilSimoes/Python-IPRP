vencimento_bruto = float(input("Introduz o vencimento bruto: "))

IRS = vencimento_bruto * 0.25
SS = vencimento_bruto * 0.05
CNA = vencimento_bruto * 0.10

vencimento_liquido = vencimento_bruto - (IRS + SS + CNA)

print("Para o vencimento bruto de valor %.2f€, o vencimento líquido vai ser de %.2f€" % (vencimento_bruto, vencimento_liquido))