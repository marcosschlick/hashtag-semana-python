import flet as ft  # Importa a biblioteca Flet para criar interfaces gráficas.

# Passo 1: Configurar a página principal da aplicação
def main(pagina):  # Função principal que configura a página da aplicação.
    # Passo 2: Criar o título do chat
    texto = ft.Text("Hashzap")  # Cria um texto com o nome do chat "Hashzap".

    # Passo 3: Criar a área de mensagens do chat
    chat = ft.Column()  # Cria uma coluna para armazenar as mensagens do chat.

    # Passo 4: Criar o campo de texto para o nome do usuário
    nome_usuario = ft.TextField(label="Escreva seu nome")  # Cria um campo de texto para o usuário inserir seu nome.

    # Passo 5: Configurar a função para lidar com mensagens enviadas ou entrada de novos usuários
    def enviar_mensagem_tunel(mensagem):
        # Identifica o tipo de mensagem (mensagem ou entrada de usuário)
        tipo = mensagem["tipo"]  
        if tipo == "mensagem":  # Se for uma mensagem de chat
            texto_mensagem = mensagem["texto"]
            usuario_mensagem = mensagem["usuario"]
            chat.controls.append(ft.Text(f"{usuario_mensagem}: {texto_mensagem}"))  # Adiciona a mensagem ao chat.
        else:  # Se for a entrada de um novo usuário
            usuario_mensagem = mensagem["usuario"]
            chat.controls.append(ft.Text(f"{usuario_mensagem} entrou no chat", 
                                         size=12, italic=True, color=ft.colors.ORANGE_500))  # Formatação especial.
        pagina.update()  # Atualiza a página para refletir as mudanças no chat.

    # Passo 6: Assinar a função de envio de mensagens para eventos
    pagina.pubsub.subscribe(enviar_mensagem_tunel)  # Assina a função de envio de mensagens.

    # Passo 7: Criar a função para enviar mensagens ao pressionar "Enviar"
    def enviar_mensagem(evento):
        pagina.pubsub.send_all({"texto": campo_mensagem.value, "usuario": nome_usuario.value,
                                "tipo": "mensagem"})  # Envia a mensagem para todos os usuários.
        campo_mensagem.value = ""  # Limpa o campo de mensagem.
        pagina.update()  # Atualiza a página para refletir a mensagem enviada.

    # Passo 8: Criar o campo de texto e botão para enviar mensagens
    campo_mensagem = ft.TextField(label="Digite uma mensagem", on_submit=enviar_mensagem)  # Campo de texto.
    botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)  # Botão de envio.

    # Passo 9: Configurar a função para entrada de um novo usuário no chat
    def entrar_popup(evento):
        pagina.pubsub.send_all({"usuario": nome_usuario.value, "tipo": "entrada"})  # Mensagem de entrada.
        pagina.add(chat)  # Adiciona o chat à página.
        popup.open = False  # Fecha o popup de boas-vindas.
        pagina.remove(botao_iniciar)  # Remove o botão "Iniciar chat".
        pagina.remove(texto)  # Remove o título "Hashzap".
        pagina.add(ft.Row([campo_mensagem, botao_enviar_mensagem]))  # Adiciona o campo e botão de mensagem.
        pagina.update()  # Atualiza a página para refletir as mudanças.

    # Passo 10: Criar o popup de boas-vindas para entrada do nome do usuário
    popup = ft.AlertDialog(
        open=False, 
        modal=True,
        title=ft.Text("Bem vindo ao Hashzap"),
        content=nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_popup)],  # Botão "Entrar".
    )

    # Passo 11: Configurar a função para exibir o popup ao pressionar "Iniciar chat"
    def entrar_chat(evento):
        pagina.dialog = popup  # Define o popup na página.
        popup.open = True  # Abre o popup.
        pagina.update()  # Atualiza a página para mostrar o popup.

    # Passo 12: Criar o botão "Iniciar chat"
    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=entrar_chat)

    # Passo 13: Adicionar elementos iniciais à página
    pagina.add(texto)  # Adiciona o texto "Hashzap".
    pagina.add(botao_iniciar)  # Adiciona o botão "Iniciar chat".

# Passo 14: Executar a aplicação Flet
ft.app(target=main, view=ft.WEB_BROWSER, port=8000)