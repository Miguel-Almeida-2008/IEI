import customtkinter as ctk
import pyshorteners

ctk.set_appearance_mode("dark")

# Instancia o encurtador globalmente
s = pyshorteners.Shortener()


# FUNÇÃO PARA COPIAR PARA A ÁREA DE TRANSFERÊNCIA
def copiar_para_clipboard(link):
    app.clipboard_clear()
    app.clipboard_append(link)
    # Altera temporariamente o texto do botão para dar feedback visual
    return app.clipboard_get()

def clipboard_action(link, button):
    copiar_para_clipboard(link)
    button.configure(text="Copied!", fg_color="green"),



def encurtar_link(link):
    return s.tinyurl.short(link)


# FUNÇÃO PARA ENCURTAR
def menu_encurtamento(entry_widget, feedback_widget, janela):
    try:
        link = entry_widget.get().strip()
        if not link:
            feedback_widget.configure(
                text="Please paste a link first!", text_color="yellow"
            )
            return
        novo_link = encurtar_link(link)
        feedback_widget.configure(
            text=f"Your shortened link is:\n{novo_link}", text_color="green"
        )

        # Cria o botão de copiar dinamicamente se ele ainda não existir
        if not hasattr(janela, "btn_copy"):
            janela.btn_copy = ctk.CTkButton(
                janela, text="Copy Link", fg_color="#1f538d"
            )
            janela.btn_copy.pack(pady=10)

        # Configura a ação do botão de copiar com o novo link
        janela.btn_copy.configure(
            command=lambda: clipboard_action(novo_link, janela.btn_copy),
            text="Copy Link",
            fg_color="#1f538d",
        )

    except Exception:
        feedback_widget.configure(
            text="Error shortening link. Check URL.", text_color="red"
        )


def alongar_link(link):
    return s.tinyurl.expand(link)


# FUNÇÃO PARA ALONGAR
def menu_alongamento(entry_widget, feedback_widget, janela):
    try:
        link = entry_widget.get().strip()
        if not link:
            feedback_widget.configure(
                text="Please paste a link first!", text_color="yellow"
            )
            return
        novo_link = alongar_link(link)
        feedback_widget.configure(
            text=f"Your lengthened link is:\n{novo_link}", text_color="green"
        )

        # Cria o botão de copiar dinamicamente se ele ainda não existir
        if not hasattr(janela, "btn_copy"):
            janela.btn_copy = ctk.CTkButton(
                janela, text="Copy Link", fg_color="#1f538d"
            )
            janela.btn_copy.pack(pady=10)

        # Configura a ação do botão de copiar com o novo link
        janela.btn_copy.configure(
            command=lambda: clipboard_action(novo_link, janela.btn_copy),
            text="Copy Link",
            fg_color="#1f538d",
        )

    except Exception:
        feedback_widget.configure(
            text="Error lengthening link. Check URL.", text_color="red"
        )


# Função do botão da Janela Principal
def main():
    choice = resposta.get().strip()

    if choice == "0":
        janela_encurtamento = ctk.CTkToplevel(app)
        janela_encurtamento.title("Link shortener")
        janela_encurtamento.geometry("400x450")
        janela_encurtamento.lift()
        janela_encurtamento.attributes("-topmost", True)

        label = ctk.CTkLabel(
            janela_encurtamento, text="Copy the link you want to shorten:"
        )
        label.pack(pady=20)

        entry = ctk.CTkEntry(
            janela_encurtamento, placeholder_text="Copy it here", width=300
        )
        entry.pack(pady=20)

        feedback_janela = ctk.CTkLabel(janela_encurtamento, text="")
        feedback_janela.pack(pady=10)

        button1 = ctk.CTkButton(
            janela_encurtamento,
            text="Shorten link",
            command=lambda: menu_encurtamento(
                entry, feedback_janela, janela_encurtamento
            ),
        )
        button1.pack(pady=10)

    elif choice == "1":
        janela_alongar = ctk.CTkToplevel(app)
        janela_alongar.title("Link lengthener")
        janela_alongar.geometry("400x450")
        janela_alongar.lift()
        janela_alongar.attributes("-topmost", True)

        label = ctk.CTkLabel(janela_alongar, text="Copy the link you want to lengthen:")
        label.pack(pady=20)

        entry = ctk.CTkEntry(janela_alongar, placeholder_text="Copy it here", width=300)
        entry.pack(pady=20)

        feedback_janela = ctk.CTkLabel(janela_alongar, text="")
        feedback_janela.pack(pady=10)

        button2 = ctk.CTkButton(
            janela_alongar,
            text="Lengthen link",
            command=lambda: menu_alongamento(entry, feedback_janela, janela_alongar),
        )
        button2.pack(pady=10)
    else:
        feedback.configure(
            text="Your choice is invalid. Please try again and type either 0 or 1.",
            text_color="red",
        )


# Criar a janela principal
app = ctk.CTk()
app.title("Link modifier")
app.geometry("600x400")

pergunta1 = ctk.CTkLabel(
    app,
    text="Type 0 if you want to shorten your link\n\nType 1 if you want to lengthen it instead",
)
pergunta1.pack(pady=20)

resposta = ctk.CTkEntry(app, placeholder_text="Enter your choice here", width=200)
resposta.pack(pady=10)

button = ctk.CTkButton(app, text="Confirm Choice", command=main)
button.pack(pady=20)

feedback = ctk.CTkLabel(app, text="")
feedback.pack(pady=10)
if __name__ == "__main__":
    app.mainloop()
