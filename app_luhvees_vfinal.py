import streamlit as st

# 1. CONFIGURAÇÃO DA PÁGINA (Interface Premium)
st.set_page_config(page_title='Luhvees Stores - Sistema 10K', page_icon='💰', layout='wide')

# 2. ESTILIZAÇÃO CUSTOMIZADA (Pink, Lilac & Black)
st.markdown('''
    <style>
    .stApp { background-color: #0d0d0d; color: #ffffff; }
    h1, h2, h3 { color: #ff69b4 !important; }
    .stButton>button { 
        background-color: #ff69b4; 
        color: white; 
        border-radius: 20px; 
        border: none;
        padding: 10px 25px;
        font-weight: bold;
        width: 100%;
    }
    .stTextInput>div>div>input, .stTextArea>div>textarea, .stSelectbox>div>div {
        background-color: #1a1a1a !important;
        color: white !important;
        border: 1px solid #ff69b4 !important;
    }
    .stExpander { border: 1px solid #dda0dd !important; background-color: #111 !important; }
    </style>
''', unsafe_allow_html=True)

# 3. SISTEMA DE SEGURANÇA (Gatekeeper)
def check_password():
    if 'password_correct' not in st.session_state:
        st.title('🔐 Acesso Restrito - Luhvees Stores')
        senha = st.text_input('Insira a Senha Premium:', type='password')
        if st.button('Desbloquear Sistema'):
            if senha == 'LUHVEES10K':
                st.session_state['password_correct'] = True
                st.rerun()
            else:
                st.error('Senha Incorreta. Solicite acesso à Luana.')
        return False
    return True

if check_password():
    # 4. BARRA LATERAL E NAVEGAÇÃO[cite: 4]
    st.sidebar.title('💎 Menu 10K')
    menu = st.sidebar.radio('Navegação:', 
        ['Dashboard', 'Nichos & Prompts', 'Gerador de Bio', 'Calendário 7 Dias', 'IA de Legendas'])
    
    st.sidebar.divider()
    st.sidebar.write('© 2024 Luhvees Stores')

    # --- PÁGINA: DASHBOARD ---[cite: 4]
    if menu == 'Dashboard':
        st.title('🚀 Bem-vinda ao Sistema de Automação')
        st.write('Seu ecossistema para faturar R$ 10.000 mensais.')
        col1, col2, col3 = st.columns(3)
        col1.metric("Meta Mensal", "R$ 10.000", "Foco")
        col2.metric("Status", "Escala Ativa", "90 Dias")
        col3.metric("Conversão", "+25%", "IA")

    # --- PÁGINA: NICHOS & PROMPTS (Matadores)[cite: 4]
    elif menu == 'Nichos & Prompts':
        st.title('🔥 Estratégias de Escala')
        nicho = st.selectbox('Escolha o Nicho:', ['Calçados de Luxo', 'Casa & Cozinha', 'Kids & Maternidade'])
        
        with st.expander('📍 FASE 1: 30 DIAS (Mineração)'):
            st.code(f'Atue como especialista em {nicho}. Identifique produtos vencedores com efeito "UAU" e alta margem...')
        
        with st.expander('📈 FASE 2: 60 DIAS (Anúncios)'):
            st.code(f'Crie uma campanha de Meta Ads para {nicho} usando o framework PAS (Problema, Agitação, Solução)...')

    # --- PÁGINA: GERADOR DE BIO[cite: 4]
    elif menu == 'Gerador de Bio':
        st.title('🤳 Branding Magnético')
        nome_l = st.text_input('Nome da sua Loja:')
        if st.button('Gerar Bio Profissional'):
            st.success('Bio Gerada com Sucesso!')
            st.code(f'✨ {nome_l} | Curadoria de Elite\n🛍️ Resolvendo seu dia a dia com estilo\n🔥 Ofertas diárias exclusivas nos Stories\n👇 Pegue seu link aqui:')

    # --- PÁGINA: CALENDÁRIO 7 DIAS[cite: 4]
    elif menu == 'Calendário 7 Dias':
        st.title('🗓️ Cronograma de Lucro Semanal')
        dias = {
            'Segunda': '❌ O PROBLEMA: Mostre a dor que o produto resolve.',
            'Terça': '✨ A SOLUÇÃO: O produto em ação (Vídeo Viral).',
            'Quarta': '📦 CONFIANÇA: Unboxing ou Depoimento de cliente.',
            'Quinta': '💡 DICA: Como usar ou cuidar do seu produto.',
            'Sexta': '💰 OFERTA: Promoção relâmpago com escassez.',
            'Sábado': '💃 ESTÉTICA: Vídeo de lifestyle com música em alta.',
            'Domingo': '❓ INTERAÇÃO: Enquetes e perguntas para engajar.'
        }
        for dia, acao in dias.items():
            st.write(f'**{dia}**: {acao}')

    # --- PÁGINA: IA GERADOR DE LEGENDAS[cite: 4]
    elif menu == 'IA Gerador de Legendas':
        st.title('🤖 IA Generativa Luhvees')
        produto = st.text_input('Qual produto vamos vender hoje?')
        objetivo = st.selectbox('Objetivo do Post:', ['Venda Direta', 'Curiosidade', 'Educação'])
        
        if st.button('Gerar Legenda Matadora'):
            st.write('### Sua Legenda Pronta:')
            st.text_area('Copie e poste:', value=f'✨ VOCÊ NÃO PODE IGNORAR ISSO! ✨\n\nO {produto} acabou de chegar para transformar sua rotina. Chega de perder tempo com o que não funciona.\n\n✅ Qualidade Premium\n✅ Entrega Garantida\n\n🔥 Estoque limitado! Clique no link da Bio agora.', height=200)
            st.balloons()
