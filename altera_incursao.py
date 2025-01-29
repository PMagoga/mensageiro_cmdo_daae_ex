import streamlit as st
import datetime
from datetime import time, date
from openpyxl import load_workbook

st.title("Alterar uma Incursão")


# Layout com 2 colunas
col1, col2 = st.columns(2, gap="small")

# Primeira coluna
with col1:
    container = st.container(border=True)
    indica_incursao = container.text_input("Incursão a alterar", placeholder="Incursão", key="input1")

    container2 = st.container(border=True)
    distancia = container2.text_input("Distância", placeholder='Distância')
    
    container4 = st.container(border=True)
    rumo = container4.text_input("Rumo", placeholder='Rumo')

    # segunda coluna
with col2:
    container5 = st.container(border=True)
    azimute = container5.text_input("Azimute", placeholder="azimute", key="azimute")
        
    container6 = st.container(border=True)
    identifacao = container6.text_input("Identificação", placeholder='Identificação')
        
    container7 = st.container(border=True)
    velocidade = container7.text_input("Velocidade", placeholder='Velocidade')

btn_gera_mensagem = st.button("Gerar Mensagem da Incursão")

if btn_gera_mensagem:
    st.write("Mensagem para os GAAAe")
        
    # iniciando as variáveis
    a = indica_incursao
    aa = f'ALTERA INCURSÃO:{a}'
    c = azimute
    d = float(distancia)
    e = identifacao
    f = "-----"
    g = float(velocidade)
    h = rumo
    i = round(((d*1.609)/(g*1.852))*60)
    j = "-----"
    hora = datetime.datetime.now()
    hora_local = hora.strftime("%H")
    minutos = hora.strftime(":%M")
    hora_zulu = int(hora_local) + 3
    k = str(hora_zulu) + minutos
    l = "OCOAM"
        
    #guardar a lista de incursão em um arquivo xlsx
    data_atual = date.today()
    data_atual_tabela = f'{data_atual.day}/{data_atual.month}/{data_atual.year}'
    arquivo_existente = 'lista_das_incursoes.xlsx'
    # dados a incluir
    hora_zulu_tabela = f'{k}Z'
    new_data = [[data_atual_tabela, aa, c, d, e, f, g, h, i, j, hora_zulu_tabela, l]]
        
    wb = load_workbook(arquivo_existente)
    
    # selecionar a planilha
    ws = wb.active
      
    # adicionar os dados
    for row in new_data:
            ws.append(row)
            
    # salvar
    wb.save(arquivo_existente)       
        
        
    #separar a lista da incursão para acrescentar o código da OM
    inicio = f'A/ ALTERA INCURSÃO:{a}'
    fim = f'C/ {c} D/ {d} E/ {e} F/ {f} G/ {g} H/ {h} I/ {i} J/ {j} K/ {k}Z/ L/ {l}'
        
    container_msg_alterada = st.container(border=True)
    container_msg_alterada.write(f'{inicio} {fim}')
        



