import flet as ft 

def main(pagina):
    titulo = ft.Text("Hashzap")

    # websocket - túnel de comunicação entre 2 usuarios
    def enviar_mensagem_tunel(mensagem):
        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()
    
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        nome_usuario = caixa_nome.value
        texto_campo_mensagem = campo_enviar_mensagem.value
        mensagem = f"{nome_usuario}: {texto_campo_mensagem}"
        pagina.pubsub.send_all(mensagem)
        campo_enviar_mensagem.value = ""
        pagina.update()

        pagina.update()

    campo_enviar_mensagem = ft.TextField(label = "Digite aqui a sua mensagem")
    botao_enviar = ft.ElevatedButton("Enviar mensagem", on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])

    chat = ft.Column()

    def entrar_chat(evento):
        popup.open = False
        pagina.remove(titulo)
        pagina.remove(botao)
        pagina.update()
        pagina.add(chat)
        pagina.add(linha_enviar)
        nome_usuario = caixa_nome.value
        texto_mensagem = ft.Text(f"{nome_usuario} entrou no chat")
        chat.controls.append(texto_mensagem)
        pagina.update()


    titulo_popup = ft.Text("Bem visdo ao Hashzap")
    caixa_nome = ft.TextField(label="Digite o seu nome")
    botao_popup =  ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)

    popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome, actions=[botao_popup])

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
        print("Clicou no botão")

    botao = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)


    pagina.add(titulo)
    pagina.add(botao)



# ft.app(main) -> app desktop

ft.app(main, view=ft.WEB_BROWSER)

