import smtplib,ssl


def send_email(message):
    username="kit.23.19bec068@gmail.com"
    password="jlps aojf llsp hqwb"
    host ="smtp.gmail.com"
    port=465
    context=ssl.create_default_context()
    receiver="kit.23.19bec068@gmail.com"
    with smtplib.SMTP_SSL(host,port,context=context)as server:
        server.login(username,password)
        server.sendmail(username,receiver,message)