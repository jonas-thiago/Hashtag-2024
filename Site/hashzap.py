# Passo a passo
# Passo 0 - Titulo Hashzap
# Passo 1 - Botão para iniciar o chat
        # Popup
            # Bem vindo ao Hashzap
            # Escreva o seu nome
            # Entrar no chat
# Passo 2 - Chat
            # Usuário entrou no chat
            # Mensagem do usuário
# Passo 3 - Campo para enviar a mensagem
# Passo 4 - Botão para enviar

# Importando o flet
import flet as ft

def hashzap(pagina):
    titulo = ft.Text('Hashzap')

    nome_usuario = ft.TextField(label='Escreva seu nome')
    
    chat = ft.Column()
    
    def enviar_mensagem_tunel(informacoes):               # Tunel para enviar mensagem localmente na rede
        chat.controls.append(ft.Text(informacoes))
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        texto_campo_mensagem = f'{nome_usuario.value}: {campo_mensagem.value}'      # Nome do usuario e mensagem
        
        pagina.pubsub.send_all(texto_campo_mensagem)            # Comando para enviar mensagem pelo tunel de comunicação

        campo_mensagem.value = ''           # Limpar o campo mensagem
        pagina.update()

    campo_mensagem = ft.TextField(label='Escreva sua mensagem aqui', 
                                  on_submit=enviar_mensagem)
    
    botao_enviar = ft.ElevatedButton('enviar', on_click=enviar_mensagem)

    def entrar_chat(evento):
        popup.open = False                      # Fechar o popup
        pagina.remove(botao_iniciar)            # Tirar o botão iniciar chat da tela
        pagina.add(chat)                        # Adicionar o nosso chat
        linha_mensagem = ft.Row([
            campo_mensagem,                     # Criar o campo de enviar mensagem
            botao_enviar                        # Botão de enviar mensagem
        ])
        pagina.add(linha_mensagem)

        texto = f'{nome_usuario.value} entrou no chat'
        pagina.pubsub.send_all(texto)
        pagina.update()


    popup = ft.AlertDialog(open=False, 
                           modal=True, 
                           title=ft.Text('Bem-vindo ao chat Hashzap'),
                           content=nome_usuario,
                           actions=[ft.ElevatedButton('Entrar', on_click=entrar_chat)]
                           )

    def iniciar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton('Iniciar chat', on_click=iniciar_chat)

    pagina.add(titulo)
    pagina.add(botao_iniciar)
    
    
    

#ft.app(hashzap)                                 # visual para aplicativo de celular
ft.app(hashzap, view=ft.WEB_BROWSER)          # visual para web

