import streamlit as st
import datetime
from datetime import time, date
from openpyxl import load_workbook

st.set_page_config(
        page_title="Mensageiro OLAAe",
        page_icon="cmdo.ico"
    )


def criar_mensagem_pagina():    
    
    # Título da página, divido em duas colunas, uma para a imagem
    coluna_titulo, coluna_img = st.columns(2)
    with coluna_titulo:
        st.title("Mensageiro OLAAe")
    
    with coluna_img:
        st.image('logo_cmdo.png')
    
    st.write("SEQUÊNCIA PARA O ENGAJAMENTO")
    st.write("O OLAAe designa o alvo por meio de mensagem padronizada pelas NOSDA")
    
    st.write("---")
    ocoam = st.text_input("Indicativo do OCOAM que enviará as mensagem", placeholder="OCOAM")    
  
    # Layout com 2 colunas
    col1, col2 = st.columns(2, gap="small")

    # Primeira coluna
    with col1:
        container = st.container(border=True)
        indica_incursao = container.text_input("Indicativo da Incursão", placeholder="Incursão", key="input1")
        
        container2 = st.container(border=True)
        distancia = container2.text_input("Distância", placeholder='Distância')
        
        container3 = st.container(border=True)
        numero_vetor = container3.text_input("Número/Vetor hostil", placeholder='Número de vetores hostis')
        
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
        
        container8 = st.container(border=True)
        iff = container8.text_input("IFF do vetor aéreo", placeholder='IFF')

    btn_gera_mensagem = st.button("Gerar Mensagem da Incursão")
    if btn_gera_mensagem:
        st.write("Mensagem para os GAAAe")
        
        # iniciando as variáveis
        a = indica_incursao
        c = azimute
        d = float(distancia)
        e = identifacao
        f = numero_vetor
        g = float(velocidade)
        h = rumo
        i = round(((d*1.609)/(g*1.852))*60)
        j = iff
        hora = datetime.datetime.now()
        hora_local = hora.strftime("%H")
        minutos = hora.strftime(":%M")
        hora_zulu = int(hora_local) + 3
        k = str(hora_zulu) + minutos
        l = ocoam
        
        #guardar a lista de incursão em um arquivo xlsx
        data_atual = date.today()
        data_atual_tabela = f'{data_atual.day}/{data_atual.month}/{data_atual.year}'
        arquivo_existente = 'lista_das_incursoes.xlsx'
        # dados a incluir
        hora_zulu_tabela = f'{k}Z'
        new_data = [[data_atual_tabela, a, c, d, e, f, g, h, i, j, hora_zulu_tabela, l]]
        
        wb = load_workbook(arquivo_existente)
        
        # selecionar a planilha
        ws = wb.active
        
        # adicionar os dados
        for row in new_data:
            ws.append(row)
            
        # salvar
        wb.save(arquivo_existente)       
        
        
        #separar a lista da incursão para acrescentar o código da OM
        inicio = f'A/ {a}'
        fim = f'C/ {c} D/ {d} E/ {e} F/ {f} G/ {g} H/ {h} I/ {i} J/ {j} K/ {k}Z/ L/ {l}'
        
        container_1gaaae = st.container(border=True)
        container_1gaaae.write(f'{inicio} B/ PROMETEU {fim}')
        
        container_2gaaae = st.container(border=True)
        container_2gaaae.write(f'{inicio} B/ ATLAS {fim}')
        
        container_3gaaae = st.container(border=True)
        container_3gaaae.write(f'{inicio} B/ PÓLUX {fim}')
        
        container_4gaaae = st.container(border=True)
        container_4gaaae.write(f'{inicio} B/ CASTOR {fim}')
        
        container_11gaaae = st.container(border=True)
        container_11gaaae.write(f'{inicio} B/ AJAX {fim}')
        
        container_12gaaae = st.container(border=True)
        container_12gaaae.write(f'{inicio} B/ RICO {fim}')        


pagina = st.navigation(
    [st.Page(criar_mensagem_pagina, title="Criar Msg Incursão"),
    st.Page("altera_incursao.py", title="Alterar uma incursão"),
    st.Page("listar_incursoes.py", title="Listar todas as incursões")],
    position='sidebar')
pagina.run()
