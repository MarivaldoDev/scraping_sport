import yagmail


def envio(user: str, password: str, mensagem: str) -> None:
    yag = yagmail.SMTP(
        user=user, 
        password=password
    )

    destinatario = 'pedromarivaldo10@gmail.com'
    assunto = 'JOGO DO SPORT'

    yag.send(to=destinatario, subject=assunto, contents=mensagem)

    print('E-mail enviado!')