#Título: Hashzap
#Botão para iniciar chat    #popup (janela na frente da tela)
    #Título: Bem vindo ao haszap
    #campo de texto: Escreva seu nome no chat
    #Botão: Entrar no chat
        #Sumir com o título hashzap
        #Fechar a janela (popup)
        #Carregar chat
            #As mensagen já foram enviadas
            #Campo: Digite sua mensagem
            #Botão de Enviar


#Importar o flet
import flet as ft            

#criar a função principal do seu aplicativo
def main(pagina):
    #criar todas as funcionalidades

    #criar o elemento
    titulo = ft.Text("Hashzap")
    titulo_janela = ft.Text("Bem vindo ao Hashzap")


    chat = ft.Column()

    def enviar_mensagam_tunel(mensagem):
        texto_chat = ft.Text(mensagem)
        chat.controls.append(texto_chat)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagam_tunel)    

    def enviar_mensagem(evento):
        texto_mensagem = campo_mensagem.value
        nome_usuario = campo_nome_usuario.value
        mensagem = f"{nome_usuario}: {texto_mensagem}"
        pagina.pubsub.send_all(mensagem)
        campo_mensagem.value =""
        pagina.update()
            
    campo_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
    botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    linha_mensagem = ft.Row([campo_mensagem, botao_enviar_mensagem])
    def entrar_chat(evento):
        pagina.remove(titulo)
        pagina.remove(botao_inicial)
        janela.open = False

        pagina.add(chat)
        pagina.add(linha_mensagem)
        mensagem = f"{campo_nome_usuario.value}: entrou no chat"
        pagina.pubsub.send_all(mensagem)
        pagina.update()

    campo_nome_usuario = ft.TextField(label="Escreva seu nome no chat", on_submit=entrar_chat)
    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)
    janela = ft.AlertDialog(title=titulo_janela, content=campo_nome_usuario, actions=[botao_entrar])

    def iniciar_chat(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()
    botao_inicial = ft.ElevatedButton("Iniciar Chat", on_click=iniciar_chat)
    #adiciona o elemento na pagina
    pagina.add(titulo)
    pagina.add(botao_inicial)
#rodar o seu aplicativo
ft.app(main, view=ft.WEB_BROWSER)    