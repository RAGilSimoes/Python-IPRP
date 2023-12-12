def dias_mes_ano(data):
    dias_semana = {"1":"Domingo", "2":"Segunda-Feira", "3":"Terça-Feira", "4":"Quarta-Feira", "5":"Quinta-Feira", "6":"Sexta-Feira", "7":"Sábado"}
    meses_ano = {"1":"Janeiro", "2":"Fevereiro", "3":"Março", "4":"Abril", "5":"Maio", "6":"Junho", "7":"Julho", "8":"Agosto", "9":"Setembro", "10":"Outubro", "11":"Novembro", "12":"Decembro"}
    
    partes_data = data.split("/")
    
    DS = dias_semana[partes_data[0]]
    DM = partes_data[1]
    M = meses_ano[partes_data[2]]
    A = partes_data[3]
    
    data_final = DS + ", " + DM + " " + M + " " + A
    
    return data_final

print(dias_mes_ano("4/5/6/2006"))