import streamlit as st

# 1. CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title='Luhvees Stores - Sistema 10K', page_icon='💰', layout='wide')

# 2. ESTILIZAÇÃO CUSTOMIZADA
st.markdown('''
    <style>
    .stApp { background-color: #0d0d0d; color: #ffffff; }
    h1, h2, h3 { color: #ff69b4 !important; }
    .stButton>button { background-color: #ff69b4; color: white; border-radius: 20px; width: 100%; font-weight: bold; }
    .stTextInput>div>div>input { background-color: #1a1a1a !important; color: white !important; border: 1px solid #ff69b4 !important; }
    </style>
''', unsafe_allow_html=True)

# 3. LÓGICA DE SEGURANÇA CORRIGIDA
if 'autenticado' not in st.session_state:
    st.session_state['autenticado'] = False

if not st.session_state['autenticado']:
    st.title('🔐 Acesso Restrito - Lojas Luhvees')
    senha = st.text_input('Insira a Senha Premium para desbloquear:', type='password')
    if st.button('Desbloquear Sistema'):
        if senha == 'LUHVEES10K':
            st.session_state['autenticado'] = True
            st.rerun()
        else:
            st.error('Senha Incorreta. Solicite acesso à Luana.')
    st.stop() # ESTA LINHA IMPEDE QUE O CONTEÚDO ABAIXO APAREÇA[cite: 4]

# --- TODO O CONTEÚDO ABAIXO SÓ APARECE APÓS A SENHA ---[cite: 4]

st.sidebar.title('💎 Menu 10K')
menu = st.sidebar.radio('Navegação:', ['Dashboard', 'Nichos & Prompts', 'Gerador de Bio', 'Calendário 7 Dias', 'IA de Legendas'])

if menu == 'Dashboard':
    st.title('🚀 Bem-vinda, Luana!')
    st.write('Sistema 10K pronto para operar.')
    st.metric("Meta Mensal", "R$ 10.000", "Ativa")

elif menu == 'Nichos & Prompts':
    st.title('🔥 Estratégias de Escala')
    nicho = st.selectbox('Escolha o Nicho:', ['Calçados de Luxo', 'Casa & Cozinha', 'Kids & Maternidade'])
    
    with st.expander('📍 FASE 1: 30 DIAS (Mineração)'):
        st.code(f'Atue como especialista em {nicho}. Identifique produtos vencedores...')
    
    with st.expander('📈 FASE 2: 60 DIAS (Anúncios)'):
        st.code(f'Crie uma campanha de Meta Ads para {nicho}...')

elif menu == 'Gerador de Bio':
    st.title('🤳 Branding Magnético')
    nome_l = st.text_input('Nome da sua Loja:')
    if st.button('Gerar Bio'):
        st.code(f'✨ {nome_l} | Ofertas Diárias\n👇 Links abaixo:')

elif menu == 'Calendário 7 Dias':
    st.title('🗓️ Cronograma 7 Dias')
    st.write('Seg: Problema | Ter: Solução | Qua: Prova Social | Qui: Dica | Sex: Oferta | Sáb: Estética | Dom: Interação')

elif menu == 'IA de Legendas':
    st.title('🤖 IA Generativa')
    produto = st.text_input('Qual produto vamos vender hoje?')
    if st.button('Gerar Legenda'):
        st.text_area('Legenda:', value=f'✨ O {produto} chegou para mudar sua rotina! #achadinhos', height=200)
