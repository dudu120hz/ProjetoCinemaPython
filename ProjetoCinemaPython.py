def uncharted():
    print("\n Você escolheu Uncharted!")
    mes=str(input(" Que mês você quer?(fevereiro ou março): "))
    if mes=='fevereiro':
        print(" Você escolheu o mês de Fevereiro!")
        dia=int(input(" Que dia você quer?(digite de 17 a 28): "))
        if dia>=17 and dia<=28:
            print(" Você escolheu dia", dia, "de Fevereiro!")
            print(" Os horários disponíveis são:")
            print(" 13h45   14h20   15h15")
            print(" 16h05   17h30   18h00")
            print(" 19h15   20h35   21h05")
            print(" 22h50")
            print(" Qual horário você quer?")
            horario=int(input(" (digite os três primeiros dígitos, exemplo: '17'): "))
            if horario>=13 and horario<=22:
                if horario==13:
                    horario=str(horario)
                    horario=horario+"h45!"
                elif horario==14:
                    horario=str(horario)
                    horario=horario+"h20!"
                elif horario==15:
                    horario=str(horario)
                    horario=horario+"h15!"
                elif horario==16:
                    horario=str(horario)
                    horario=horario+"h05!"
                elif horario==17:
                    horario=str(horario)
                    horario=horario+"h30!"
                elif horario==18:
                    horario=str(horario)
                    horario=horario+"h00!"
                elif horario==19:
                    horario=str(horario)
                    horario=horario+"h15!"
                elif horario==20:
                    horario=str(horario)
                    horario=horario+"h35!"
                elif horario==21:
                    horario=str(horario)
                    horario=horario+"h05!"
                elif horario==22:
                    horario=str(horario)
                    horario=horario+"h50!"
                print(" Você escolheu o horário das", horario)
                tresd=str(input("\n Você quer com 3D?(sim ou não): "))
                if tresd=='sim':
                    print(" Você escolheu Com 3D!")
                    ingresso_inteira=float(42.00)
                    ingresso_meia=float(21.00)
                    print(" O valor do ingresso de entrada-inteira é R$",ingresso_inteira)
                    print(" O valor do ingresso de meia-entrada é R$",ingresso_meia)
                    quant_inteira=int(input(" Quantos ingressos de entrada-inteira você quer? "))
                    quant_meia=int(input(" Quantos ingressos de meia-entrada você quer? "))
                    valor_inteira=ingresso_inteira*quant_inteira
                    valor_meia=ingresso_meia*quant_meia
                    print(" O valor dos ingressos entrada-inteira fica: R$",valor_inteira)
                    print(" O valor dos ingressos meia-entrada fica: R$",valor_meia)
                    valor_final=valor_inteira+valor_meia
                    print(" O valor final de todos os ingressos fica: R$", valor_final)
                    print("\n As formas de pagamento são:")
                    print(" Cartão")
                    print(" Boleto")
                    print(" Pix")
                    pagamento=str(input(" Qual dessas formas de pagamento você quer? "))
                    if pagamento=='cartao':
                        print(" Você escolheu Cartão!")
                        cartao=int(input(" Agora digite o número do cartão: "))
                        codigo=int(input(" Agora digite o código de segurança: "))
                        print(" Pronto, tudo pago e computado no sistema!")
                        print(" Tenha um bom filme e até a próxima!")
                    elif pagamento=='boleto':
                        print(" O código de barras do Boleto é:")
                        print(" 450460632662665675710730750765835845855865870888")
                        numero=int(input(" Digite seu número de telefone (com DDD e todos os números juntos): ")) 
                        print(" Você tem 5 dias úteis para efetuar o pagamento no Boleto")                     
                        print(" Se não pagar nesse prazo, a compra será totalmente cancelada")
                        print(" Assim que o pagamento for aprovado, vicê receberá um SMS de aviso")
                        print(" Por enquanto é isso, agradecemos a sua compra e visita!")
                    elif pagamento=='pix':
                        print(" Você escolheu Pix!")
                        print(" A chave do Pix é:")
                        print(" dudu@cinema.com")
                        numero=int(input(" Digite seu número de telefone (com DDD e todos os números juntos): "))
                        print(" Você tem 5 dias úteis para efetuar o pagamento no Boleto")
                        print(" Se não pagar nesse prazo, a compra será totalmente cancelada")
                        print(" Assim que o pagamento for aprovado, vicê receberá um SMS de aviso")
                        print(" Por enquanto é isso, agradecemos a sua compra e visita!")
                elif tresd=='nao':
                    print(" Você escolheu Sem 3D!")
                    ingresso_inteira=float(34.00)
                    ingresso_meia=float(17.00)
                    print(" O valor do ingresso de entrada-inteira é R$", ingresso_inteira)
                    print(" O valor do ingresso de meia-entrada é R$", ingresso_meia)
                    quant_inteira=int(input(" Quantos ingressos de entrada-inteira você quer? "))
                    quant_meia=int(input(" Quantos ingressos de meia-entrada você quer? "))
                    valor_inteira=ingresso_inteira*quant_inteira
                    valor_meia=ingresso_meia*quant_meia
                    print(" O valor dos ingressos entrada-inteira fica: R$",valor_inteira)
                    print(" O valor dos ingressos meia-entrada fica: R$",valor_meia)
                    valor_final=valor_inteira+valor_meia
                    print(" O valor final de todos os ingressos fica: R$", valor_final)
                    print(" As formas de pagamento são:")
                    print(" Cartão")
                    print(" Boleto")
                    print(" Pix")
                    pagamento=str(input(" Qual dessas formas de pagamento você quer? "))
                    if pagamento=='cartao':
                        print(" Você escolheu Cartão!")
                        cartao=int(input(" Agora digite o número do cartão: "))
                        codigo=int(input(" Agora digite o código de segurança: "))
                        print(" Pronto, tudo pago e computado no sistema!")
                        print(" Tenha um bom filme e até a próxima!")
                    elif pagamento=='boleto':
                        print(" O código de barras do Boleto é:")
                        print(" 450460632662665675710730750765835845855865870888")
                        numero=int(input(" Digite seu número de telefone (com DDD e todos os números juntos): ")) 
                        print(" Você tem 5 dias úteis para efetuar o pagamento no Boleto")                     
                        print(" Se não pagar nesse prazo, a compra será totalmente cancelada")
                        print(" Assim que o pagamento for aprovado, vicê receberá um SMS de aviso")
                        print(" Por enquanto é isso, agradecemos a sua compra e visita!")
                    elif pagamento=='pix':
                        print(" Você escolheu Pix!")
                        print(" A chave do Pix é:")
                        print(" dudu@cinema.com")
                        numero=int(input(" Digite seu número de telefone (com DDD e todos os números juntos): "))
                        print(" Você tem 5 dias úteis para efetuar o pagamento no Boleto")
                        print(" Se não pagar nesse prazo, a compra será totalmente cancelada")
                        print(" Assim que o pagamento for aprovado, vicê receberá um SMS de aviso")
                        print(" Por enquanto é isso, agradecemos a sua compra e visita!")
                else:
                    print("\n Você digitou errado, feche o programa e tente novamente! \n")
            else:
                print("\n Você digitou errado, feche o programa e tente novamente! \n")
        else:
            print("\n Você digitou errado, feche o programa e tente novamente! \n")

    elif mes=='marco':
        print(" Você escolheu o mês de Março!")
        dia=int(input(" Que dia você quer?(digite de 1 a 17): "))
        if dia>=1 and dia<=18:
            print(" Você escolheu dia", dia, "de Março!")
            print(" Os horários disponíveis são:")
            print(" 13h45   14h20   15h15")
            print(" 16h05   17h30   18h00")
            print(" 19h15   20h35   21h05")
            print(" 22h50")
            print(" Qual horário você quer?")
            horario=int(input(" (digite os três primeiros dígitos, exemplo: '17'): "))
            if horario>=13 and horario<=22:
                if horario==13:
                    horario=str(horario)
                    horario=horario+"h45!"
                elif horario==14:
                    horario=str(horario)
                    horario=horario+"h20!"
                elif horario==15:
                    horario=str(horario)
                    horario=horario+"h15!"
                elif horario==16:
                    horario=str(horario)
                    horario=horario+"h05!"
                elif horario==17:
                    horario=str(horario)
                    horario=horario+"h30!"
                elif horario==18:
                    horario=str(horario)
                    horario=horario+"h00!"
                elif horario==19:
                    horario=str(horario)
                    horario=horario+"h15!"
                elif horario==20:
                    horario=str(horario)
                    horario=horario+"h35!"
                elif horario==21:
                    horario=str(horario)
                    horario=horario+"h05!"
                elif horario==22:
                    horario=str(horario)
                    horario=horario+"h50!"
                print(" Você escolheu o horário das", horario)
                tresd=str(input("\n Você quer com 3D?(sim ou não): "))
                if tresd=='sim':
                    print(" Você escolheu Com 3D!")
                    ingresso_inteira=float(42.00)
                    ingresso_meia=float(21.00)
                    print(" O valor do ingresso de entrada-inteira é R$",ingresso_inteira)
                    print(" O valor do ingresso de meia-entrada é R$",ingresso_meia)
                    quant_inteira=int(input(" Quantos ingressos de entrada-inteira você quer? "))
                    quant_meia=int(input(" Quantos ingressos de meia-entrada você quer? "))
                    valor_inteira=ingresso_inteira*quant_inteira
                    valor_meia=ingresso_meia*quant_meia
                    print(" O valor dos ingressos entrada-inteira fica: R$",valor_inteira)
                    print(" O valor dos ingressos meia-entrada fica: R$",valor_meia)
                    valor_final=valor_inteira+valor_meia
                    print(" O valor final de todos os ingressos fica: R$", valor_final)
                    print("\n As formas de pagamento são:")
                    print(" Cartão")
                    print(" Boleto")
                    print(" Pix")
                    pagamento=str(input(" Qual dessas formas de pagamento você quer? "))
                    if pagamento=='cartao':
                        print(" Você escolheu Cartão!")
                        cartao=int(input(" Agora digite o número do cartão: "))
                        codigo=int(input(" Agora digite o código de segurança: "))
                        print(" Pronto, tudo pago e computado no sistema!")
                        print(" Tenha um bom filme e até a próxima!")
                    elif pagamento=='boleto':
                        print(" O código de barras do Boleto é:")
                        print(" 450460632662665675710730750765835845855865870888")
                        numero=int(input(" Digite seu número de telefone (com DDD e todos os números juntos): ")) 
                        print(" Você tem 5 dias úteis para efetuar o pagamento no Boleto")                     
                        print(" Se não pagar nesse prazo, a compra será totalmente cancelada")
                        print(" Assim que o pagamento for aprovado, vicê receberá um SMS de aviso")
                        print(" Por enquanto é isso, agradecemos a sua compra e visita!")
                    elif pagamento=='pix':
                        print(" Você escolheu Pix!")
                        print(" A chave do Pix é:")
                        print(" dudu@cinema.com")
                        numero=int(input(" Digite seu número de telefone (com DDD e todos os números juntos): "))
                        print(" Você tem 5 dias úteis para efetuar o pagamento no Boleto")
                        print(" Se não pagar nesse prazo, a compra será totalmente cancelada")
                        print(" Assim que o pagamento for aprovado, vicê receberá um SMS de aviso")
                        print(" Por enquanto é isso, agradecemos a sua compra e visita!")
                elif tresd=='nao':
                    print(" Você escolheu Sem 3D!")
                    ingresso_inteira=float(34.00)
                    ingresso_meia=float(17.00)
                    print(" O valor do ingresso de entrada-inteira é R$", ingresso_inteira)
                    print(" O valor do ingresso de meia-entrada é R$", ingresso_meia)
                    quant_inteira=int(input(" Quantos ingressos de entrada-inteira você quer? "))
                    quant_meia=int(input(" Quantos ingressos de meia-entrada você quer? "))
                    valor_inteira=ingresso_inteira*quant_inteira
                    valor_meia=ingresso_meia*quant_meia
                    print(" O valor dos ingressos entrada-inteira fica: R$",valor_inteira)
                    print(" O valor dos ingressos meia-entrada fica: R$",valor_meia)
                    valor_final=valor_inteira+valor_meia
                    print(" O valor final de todos os ingressos fica: R$", valor_final)
                    print(" As formas de pagamento são:")
                    print(" Cartão")
                    print(" Boleto")
                    print(" Pix")
                    pagamento=str(input(" Qual dessas formas de pagamento você quer? "))
                    if pagamento=='cartao':
                        print(" Você escolheu Cartão!")
                        cartao=int(input(" Agora digite o número do cartão: "))
                        codigo=int(input(" Agora digite o código de segurança: "))
                        print(" Pronto, tudo pago e computado no sistema!")
                        print(" Tenha um bom filme e até a próxima!")
                    elif pagamento=='boleto':
                        print(" O código de barras do Boleto é:")
                        print(" 450460632662665675710730750765835845855865870888")
                        numero=int(input(" Digite seu número de telefone (com DDD e todos os números juntos): ")) 
                        print(" Você tem 5 dias úteis para efetuar o pagamento no Boleto")                     
                        print(" Se não pagar nesse prazo, a compra será totalmente cancelada")
                        print(" Assim que o pagamento for aprovado, vicê receberá um SMS de aviso")
                        print(" Por enquanto é isso, agradecemos a sua compra e visita!")
                    elif pagamento=='pix':
                        print(" Você escolheu Pix!")
                        print(" A chave do Pix é:")
                        print(" dudu@cinema.com")
                        numero=int(input(" Digite seu número de telefone (com DDD e todos os números juntos): "))
                        print(" Você tem 5 dias úteis para efetuar o pagamento no Boleto")
                        print(" Se não pagar nesse prazo, a compra será totalmente cancelada")
                        print(" Assim que o pagamento for aprovado, vicê receberá um SMS de aviso")
                        print(" Por enquanto é isso, agradecemos a sua compra e visita!")
                else:
                    print("\n Você digitou errado, feche o programa e tente novamente! \n")
        else:
            print("\n Você digitou errado, feche o programa e tente novamente! \n")
    else:
        print("\n Você digitou errado, feche o programa e tente novamente! \n")

def batman():
    print("\n Você escolheu Batman!")
    mes=str(input(" Que mês você quer?(março ou abril): "))
    if mes=='março':
        print(" Você escolheu o mês de Março!")
        dia=int(input(" Que dia você quer?(digite de 03 a 31): "))
        if dia>=3 and dia <=31:
            print(" Você escolheu dia", dia, "de Março!")
            print(" Os horários disponíveis são:")
            print(" 13h45   14h20   15h15")
            print(" 16h05   17h30   18h00")
            print(" 19h15   20h35   21h05")
            print(" 22h50")
            print(" Qual horário você quer?")
            horario=int(input(" (digite os três primeiros dígitos, exemplo: '17'): "))
            if horario>=13 and horario<=22:
                if horario==13:
                    horario=str(horario)
                    horario=horario+"h45!"
                elif horario==14:
                    horario=str(horario)
                    horario=horario+"h20!"
                elif horario==15:
                    horario=str(horario)
                    horario=horario+"h15!"
                elif horario==16:
                    horario=str(horario)
                    horario=horario+"h05!"
                elif horario==17:
                    horario=str(horario)
                    horario=horario+"h30!"
                elif horario==18:
                    horario=str(horario)
                    horario=horario+"h00!"
                elif horario==19:
                    horario=str(horario)
                    horario=horario+"h15!"
                elif horario==20:
                    horario=str(horario)
                    horario=horario+"h35!"
                elif horario==21:
                    horario=str(horario)
                    horario=horario+"h05!"
                elif horario==22:
                    horario=str(horario)
                    horario=horario+"h50!"
                print(" Você escolheu o horário das", horario)
                tresd=str(input("\n Você quer com 3D?(sim ou não): "))
                if tresd=='sim':
                    print(" Você escolheu Com 3D!")
                    ingresso_inteira=float(42.00)
                    ingresso_meia=float(21.00)
                    print(" O valor do ingresso de entrada-inteira é R$",ingresso_inteira)
                    print(" O valor do ingresso de meia-entrada é R$",ingresso_meia)
                    quant_inteira=int(input(" Quantos ingressos de entrada-inteira você quer? "))
                    quant_meia=int(input(" Quantos ingressos de meia-entrada você quer? "))
                    valor_inteira=ingresso_inteira*quant_inteira
                    valor_meia=ingresso_meia*quant_meia
                    print(" O valor dos ingressos entrada-inteira fica: R$",valor_inteira)
                    print(" O valor dos ingressos meia-entrada fica: R$",valor_meia)
                    valor_final=valor_inteira+valor_meia
                    print(" O valor final de todos os ingressos fica: R$", valor_final)
                    print(" As formas de pagamento são:")
                    print(" Cartão")
                    print(" Boleto")
                    print(" Pix")
                    pagamento=str(input(" Qual dessas formas de pagamento você quer? "))
                    if pagamento=='cartao':
                        print(" Você escolheu Cartão!")
                        cartao=int(input(" Agora digite o número do cartão: "))
                        codigo=int(input(" Agora digite o código de segurança: "))
                        print(" Pronto, tudo pago e computado no sistema!")
                        print(" Tenha um bom filme e até a próxima!")
                    elif pagamento=='boleto':
                        print(" O código de barras do Boleto é:")
                        print(" 450460632662665675710730750765835845855865870888")
                        numero=int(input(" Digite seu número de telefone (com DDD e todos os números juntos): ")) 
                        print(" Você tem 5 dias úteis para efetuar o pagamento no Boleto")                     
                        print(" Se não pagar nesse prazo, a compra será totalmente cancelada")
                        print(" Assim que o pagamento for aprovado, vicê receberá um SMS de aviso")
                        print(" Por enquanto é isso, agradecemos a sua compra e visita!")
                    elif pagamento=='pix':
                        print(" Você escolheu Pix!")
                        print(" A chave do Pix é:")
                        print(" dudu@cinema.com")
                        numero=int(input(" Digite seu número de telefone (com DDD e todos os números juntos): "))
                        print(" Você tem 5 dias úteis para efetuar o pagamento no Boleto")
                        print(" Se não pagar nesse prazo, a compra será totalmente cancelada")
                        print(" Assim que o pagamento for aprovado, vicê receberá um SMS de aviso")
                        print(" Por enquanto é isso, agradecemos a sua compra e visita!")
                elif tresd=='nao':
                    print(" Você escolheu Sem 3D!")
                    ingresso_inteira=float(34.00)
                    ingresso_meia=float(17.00)
                    print(" O valor do ingresso de entrada-inteira é R$", ingresso_inteira)
                    print(" O valor do ingresso de meia-entrada é R$", ingresso_meia)
                    quant_inteira=int(input(" Quantos ingressos de entrada-inteira você quer? "))
                    quant_meia=int(input(" Quantos ingressos de meia-entrada você quer? "))
                    valor_inteira=ingresso_inteira*quant_inteira
                    valor_meia=ingresso_meia*quant_meia
                    print(" O valor dos ingressos entrada-inteira fica: R$",valor_inteira)
                    print(" O valor dos ingressos meia-entrada fica: R$",valor_meia)
                    valor_final=valor_inteira+valor_meia
                    print(" O valor final de todos os ingressos fica: R$", valor_final)
                    print(" As formas de pagamento são:")
                    print(" Cartão")
                    print(" Boleto")
                    print(" Pix")
                    pagamento=str(input(" Qual dessas formas de pagamento você quer? "))
                    if pagamento=='cartao':
                        print(" Você escolheu Cartão!")
                        cartao=int(input(" Agora digite o número do cartão: "))
                        codigo=int(input(" Agora digite o código de segurança: "))
                        print(" Pronto, tudo pago e computado no sistema!")
                        print(" Tenha um bom filme e até a próxima!")
                    elif pagamento=='boleto':
                        print(" O código de barras do Boleto é:")
                        print(" 450460632662665675710730750765835845855865870888")
                        numero=int(input(" Digite seu número de telefone (com DDD e todos os números juntos): ")) 
                        print(" Você tem 5 dias úteis para efetuar o pagamento no Boleto")                     
                        print(" Se não pagar nesse prazo, a compra será totalmente cancelada")
                        print(" Assim que o pagamento for aprovado, vicê receberá um SMS de aviso")
                        print(" Por enquanto é isso, agradecemos a sua compra e visita!")
                    elif pagamento=='pix':
                        print(" Você escolheu Pix!")
                        print(" A chave do Pix é:")
                        print(" dudu@cinema.com")
                        numero=int(input(" Digite seu número de telefone (com DDD e todos os números juntos): "))
                        print(" Você tem 5 dias úteis para efetuar o pagamento no Boleto")
                        print(" Se não pagar nesse prazo, a compra será totalmente cancelada")
                        print(" Assim que o pagamento for aprovado, vicê receberá um SMS de aviso")
                        print(" Por enquanto é isso, agradecemos a sua compra e visita!")
                else:
                    print("\n Você digitou errado, feche o programa e tente novamente! \n")
        else:
            print("\n Você digitou errado, feche o programa e tente novamente! \n")
            
    elif mes=='abril':
        print(" Você escolheu o mês de Abril!")
        dia=int(input(" Que dia você quer?(digite de 1 a 4): "))
        if dia>=1 and dia<=4:
            print(" Você escolheu dia", dia, "de Abril!")
            print(" Os horários disponíveis são:")
            print(" 13h45   14h20   15h15")
            print(" 16h05   17h30   18h00")
            print(" 19h15   20h35   21h05")
            print(" 22h50")
            print(" Qual horário você quer?")
            horario=int(input(" (digite os três primeiros dígitos, exemplo: '17'): "))
            if horario>=13 and horario<=22:
                if horario==13:
                    horario=str(horario)
                    horario=horario+"h45!"
                elif horario==14:
                    horario=str(horario)
                    horario=horario+"h20!"
                elif horario==15:
                    horario=str(horario)
                    horario=horario+"h15!"
                elif horario==16:
                    horario=str(horario)
                    horario=horario+"h05!"
                elif horario==17:
                    horario=str(horario)
                    horario=horario+"h30!"
                elif horario==18:
                    horario=str(horario)
                    horario=horario+"h00!"
                elif horario==19:
                    horario=str(horario)
                    horario=horario+"h15!"
                elif horario==20:
                    horario=str(horario)
                    horario=horario+"h35!"
                elif horario==21:
                    horario=str(horario)
                    horario=horario+"h05!"
                elif horario==22:
                    horario=str(horario)
                    horario=horario+"h50!"
                print(" Você escolheu o horário das", horario)
                tresd=str(input("\n Você quer com 3D?(sim ou não): "))
                if tresd=='sim':
                    print(" Você escolheu Com 3D!")
                    ingresso_inteira=float(42.00)
                    ingresso_meia=float(21.00)
                    print(" O valor do ingresso de entrada-inteira é R$",ingresso_inteira)
                    print(" O valor do ingresso de meia-entrada é R$",ingresso_meia)
                    quant_inteira=int(input(" Quantos ingressos de entrada-inteira você quer? "))
                    quant_meia=int(input(" Quantos ingressos de meia-entrada você quer? "))
                    valor_inteira=ingresso_inteira*quant_inteira
                    valor_meia=ingresso_meia*quant_meia
                    print(" O valor dos ingressos entrada-inteira fica: R$",valor_inteira)
                    print(" O valor dos ingressos meia-entrada fica: R$",valor_meia)
                    valor_final=valor_inteira+valor_meia
                    print(" O valor final de todos os ingressos fica: R$", valor_final)
                    print(" As formas de pagamento são:")
                    print(" Cartão")
                    print(" Boleto")
                    print(" Pix")
                    pagamento=str(input(" Qual dessas formas de pagamento você quer? "))
                    if pagamento=='cartao':
                        print(" Você escolheu Cartão!")
                        cartao=int(input(" Agora digite o número do cartão: "))
                        codigo=int(input(" Agora digite o código de segurança: "))
                        print(" Pronto, tudo pago e computado no sistema!")
                        print(" Tenha um bom filme e até a próxima!")
                    elif pagamento=='boleto':
                        print(" O código de barras do Boleto é:")
                        print(" 450460632662665675710730750765835845855865870888")
                        numero=int(input(" Digite seu número de telefone (com DDD e todos os números juntos): ")) 
                        print(" Você tem 5 dias úteis para efetuar o pagamento no Boleto")                     
                        print(" Se não pagar nesse prazo, a compra será totalmente cancelada")
                        print(" Assim que o pagamento for aprovado, vicê receberá um SMS de aviso")
                        print(" Por enquanto é isso, agradecemos a sua compra e visita!")
                    elif pagamento=='pix':
                        print(" Você escolheu Pix!")
                        print(" A chave do Pix é:")
                        print(" dudu@cinema.com")
                        numero=int(input(" Digite seu número de telefone (com DDD e todos os números juntos): "))
                        print(" Você tem 5 dias úteis para efetuar o pagamento no Boleto")
                        print(" Se não pagar nesse prazo, a compra será totalmente cancelada")
                        print(" Assim que o pagamento for aprovado, vicê receberá um SMS de aviso")
                        print(" Por enquanto é isso, agradecemos a sua compra e visita!")
                elif tresd=='nao':
                    print(" Você escolheu Sem 3D!")
                    ingresso_inteira=float(34.00)
                    ingresso_meia=float(17.00)
                    print(" O valor do ingresso de entrada-inteira é R$", ingresso_inteira)
                    print(" O valor do ingresso de meia-entrada é R$", ingresso_meia)
                    quant_inteira=int(input(" Quantos ingressos de entrada-inteira você quer? "))
                    quant_meia=int(input(" Quantos ingressos de meia-entrada você quer? "))
                    valor_inteira=ingresso_inteira*quant_inteira
                    valor_meia=ingresso_meia*quant_meia
                    print(" O valor dos ingressos entrada-inteira fica: R$",valor_inteira)
                    print(" O valor dos ingressos meia-entrada fica: R$",valor_meia)
                    valor_final=valor_inteira+valor_meia
                    print(" O valor final de todos os ingressos fica: R$", valor_final)
                    print(" As formas de pagamento são:")
                    print(" Cartão")
                    print(" Boleto")
                    print(" Pix")
                    pagamento=str(input(" Qual dessas formas de pagamento você quer? "))
                    if pagamento=='cartao':
                        print(" Você escolheu Cartão!")
                        cartao=int(input(" Agora digite o número do cartão: "))
                        codigo=int(input(" Agora digite o código de segurança: "))
                        print(" Pronto, tudo pago e computado no sistema!")
                        print(" Tenha um bom filme e até a próxima!")
                    elif pagamento=='boleto':
                        print(" O código de barras do Boleto é:")
                        print(" 450460632662665675710730750765835845855865870888")
                        numero=int(input(" Digite seu número de telefone (com DDD e todos os números juntos): ")) 
                        print(" Você tem 5 dias úteis para efetuar o pagamento no Boleto")                     
                        print(" Se não pagar nesse prazo, a compra será totalmente cancelada")
                        print(" Assim que o pagamento for aprovado, vicê receberá um SMS de aviso")
                        print(" Por enquanto é isso, agradecemos a sua compra e visita!")
                    elif pagamento=='pix':
                        print(" Você escolheu Pix!")
                        print(" A chave do Pix é:")
                        print(" dudu@cinema.com")
                        numero=int(input(" Digite seu número de telefone (com DDD e todos os números juntos): "))
                        print(" Você tem 5 dias úteis para efetuar o pagamento no Boleto")
                        print(" Se não pagar nesse prazo, a compra será totalmente cancelada")
                        print(" Assim que o pagamento for aprovado, vicê receberá um SMS de aviso")
                        print(" Por enquanto é isso, agradecemos a sua compra e visita!")
                else:
                    print("\n Você digitou errado, feche o programa e tente novamente! \n")
        else:
            print("\n Você digitou errado, feche o programa e tente novamente! \n")
    else:
        print("\n Você digitou errado, feche o programa e tente novamente! \n")

def sonic():
    print("\n Você escolheu Sonic!")
    mes=str(input(" Que mês você quer?(abril ou maio): "))
    if mes=='abril':
        print(" Você escolheu o mês de Abril!")
        dia=int(input(" Que dia você quer?(digite de 7 a 30): "))
        if dia>=7 and dia<=30:
            print(" Você escolheu dia", dia, "de Abril!")
            print(" Os horários disponíveis são:")
            print(" 13h45   14h20   15h15")
            print(" 16h05   17h30   18h00")
            print(" 19h15   20h35   21h05")
            print(" 22h50")
            print(" Qual horário você quer?")
            horario=int(input(" (digite os três primeiros dígitos, exemplo: '17'): "))
            if horario>=13 and horario<=22:
                if horario==13:
                    horario=str(horario)
                    horario=horario+"h45!"
                elif horario==14:
                    horario=str(horario)
                    horario=horario+"h20!"
                elif horario==15:
                    horario=str(horario)
                    horario=horario+"h15!"
                elif horario==16:
                    horario=str(horario)
                    horario=horario+"h05!"
                elif horario==17:
                    horario=str(horario)
                    horario=horario+"h30!"
                elif horario==18:
                    horario=str(horario)
                    horario=horario+"h00!"
                elif horario==19:
                    horario=str(horario)
                    horario=horario+"h15!"
                elif horario==20:
                    horario=str(horario)
                    horario=horario+"h35!"
                elif horario==21:
                    horario=str(horario)
                    horario=horario+"h05!"
                elif horario==22:
                    horario=str(horario)
                    horario=horario+"h50!"
                print(" Você escolheu o horário das", horario)
                tresd=str(input("\n Você quer com 3D?(sim ou não): "))
                if tresd=='sim':
                    print(" Você escolheu Com 3D!")
                    ingresso_inteira=float(42.00)
                    ingresso_meia=float(21.00)
                    print(" O valor do ingresso de entrada-inteira é R$",ingresso_inteira)
                    print(" O valor do ingresso de meia-entrada é R$",ingresso_meia)
                    quant_inteira=int(input(" Quantos ingressos de entrada-inteira você quer? "))
                    quant_meia=int(input(" Quantos ingressos de meia-entrada você quer? "))
                    valor_inteira=ingresso_inteira*quant_inteira
                    valor_meia=ingresso_meia*quant_meia
                    print(" O valor dos ingressos entrada-inteira fica: R$",valor_inteira)
                    print(" O valor dos ingressos meia-entrada fica: R$",valor_meia)
                    valor_final=valor_inteira+valor_meia
                    print(" O valor final de todos os ingressos fica: R$", valor_final)
                    print(" As formas de pagamento são:")
                    print(" Cartão")
                    print(" Boleto")
                    print(" Pix")
                    pagamento=str(input(" Qual dessas formas de pagamento você quer? "))
                    if pagamento=='cartao':
                        print(" Você escolheu Cartão!")
                        cartao=int(input(" Agora digite o número do cartão: "))
                        codigo=int(input(" Agora digite o código de segurança: "))
                        print(" Pronto, tudo pago e computado no sistema!")
                        print(" Tenha um bom filme e até a próxima!")
                    elif pagamento=='boleto':
                        print(" O código de barras do Boleto é:")
                        print(" 450460632662665675710730750765835845855865870888")
                        numero=int(input(" Digite seu número de telefone (com DDD e todos os números juntos): ")) 
                        print(" Você tem 5 dias úteis para efetuar o pagamento no Boleto")                     
                        print(" Se não pagar nesse prazo, a compra será totalmente cancelada")
                        print(" Assim que o pagamento for aprovado, vicê receberá um SMS de aviso")
                        print(" Por enquanto é isso, agradecemos a sua compra e visita!")
                    elif pagamento=='pix':
                        print(" Você escolheu Pix!")
                        print(" A chave do Pix é:")
                        print(" dudu@cinema.com")
                        numero=int(input(" Digite seu número de telefone (com DDD e todos os números juntos): "))
                        print(" Você tem 5 dias úteis para efetuar o pagamento no Boleto")
                        print(" Se não pagar nesse prazo, a compra será totalmente cancelada")
                        print(" Assim que o pagamento for aprovado, vicê receberá um SMS de aviso")
                        print(" Por enquanto é isso, agradecemos a sua compra e visita!")
                elif tresd=='nao':
                    print(" Você escolheu Sem 3D!")
                    ingresso_inteira=float(34.00)
                    ingresso_meia=float(17.00)
                    print(" O valor do ingresso de entrada-inteira é R$", ingresso_inteira)
                    print(" O valor do ingresso de meia-entrada é R$", ingresso_meia)
                    quant_inteira=int(input(" Quantos ingressos de entrada-inteira você quer? "))
                    quant_meia=int(input(" Quantos ingressos de meia-entrada você quer? "))
                    valor_inteira=ingresso_inteira*quant_inteira
                    valor_meia=ingresso_meia*quant_meia
                    print(" O valor dos ingressos entrada-inteira fica: R$",valor_inteira)
                    print(" O valor dos ingressos meia-entrada fica: R$",valor_meia)
                    valor_final=valor_inteira+valor_meia
                    print(" O valor final de todos os ingressos fica: R$", valor_final)
                    print(" As formas de pagamento são:")
                    print(" Cartão")
                    print(" Boleto")
                    print(" Pix")
                    pagamento=str(input(" Qual dessas formas de pagamento você quer? "))
                    if pagamento=='cartao':
                        print(" Você escolheu Cartão!")
                        cartao=int(input(" Agora digite o número do cartão: "))
                        codigo=int(input(" Agora digite o código de segurança: "))
                        print(" Pronto, tudo pago e computado no sistema!")
                        print(" Tenha um bom filme e até a próxima!")
                    elif pagamento=='boleto':
                        print(" O código de barras do Boleto é:")
                        print(" 450460632662665675710730750765835845855865870888")
                        numero=int(input(" Digite seu número de telefone (com DDD e todos os números juntos): ")) 
                        print(" Você tem 5 dias úteis para efetuar o pagamento no Boleto")                     
                        print(" Se não pagar nesse prazo, a compra será totalmente cancelada")
                        print(" Assim que o pagamento for aprovado, vicê receberá um SMS de aviso")
                        print(" Por enquanto é isso, agradecemos a sua compra e visita!")
                    elif pagamento=='pix':
                        print(" Você escolheu Pix!")
                        print(" A chave do Pix é:")
                        print(" dudu@cinema.com")
                        numero=int(input(" Digite seu número de telefone (com DDD e todos os números juntos): "))
                        print(" Você tem 5 dias úteis para efetuar o pagamento no Boleto")
                        print(" Se não pagar nesse prazo, a compra será totalmente cancelada")
                        print(" Assim que o pagamento for aprovado, vicê receberá um SMS de aviso")
                        print(" Por enquanto é isso, agradecemos a sua compra e visita!")
                else:
                    print("\n Você digitou errado, feche o programa e tente novamente! \n")
        else:
            print("\n Você digitou errado, feche o programa e tente novamente! \n")

    elif mes=='maio':
        print(" Você escolheu o mês de Maio!")
        dia=int(input(" Que dia você quer?(digite de 1 a 8): "))
        if dia>=1 and dia<=8:
            print(" Você escolheu dia", dia, "de Maio!")
            print(" Os horários disponíveis são:")
            print(" 13h45   14h20   15h15")
            print(" 16h05   17h30   18h00")
            print(" 19h15   20h35   21h05")
            print(" 22h50")
            print(" Qual horário você quer?")
            horario=int(input(" (digite os três primeiros dígitos, exemplo: '17'): "))
            if horario>=13 and horario<=22:
                if horario==13:
                    horario=str(horario)
                    horario=horario+"h45!"
                elif horario==14:
                    horario=str(horario)
                    horario=horario+"h20!"
                elif horario==15:
                    horario=str(horario)
                    horario=horario+"h15!"
                elif horario==16:
                    horario=str(horario)
                    horario=horario+"h05!"
                elif horario==17:
                    horario=str(horario)
                    horario=horario+"h30!"
                elif horario==18:
                    horario=str(horario)
                    horario=horario+"h00!"
                elif horario==19:
                    horario=str(horario)
                    horario=horario+"h15!"
                elif horario==20:
                    horario=str(horario)
                    horario=horario+"h35!"
                elif horario==21:
                    horario=str(horario)
                    horario=horario+"h05!"
                elif horario==22:
                    horario=str(horario)
                    horario=horario+"h50!"
                print(" Você escolheu o horário das", horario)
                tresd=str(input("\n Você quer com 3D?(sim ou não): "))
                if tresd=='sim':
                    print(" Você escolheu Com 3D!")
                    ingresso_inteira=float(42.00)
                    ingresso_meia=float(21.00)
                    print(" O valor do ingresso de entrada-inteira é R$",ingresso_inteira)
                    print(" O valor do ingresso de meia-entrada é R$",ingresso_meia)
                    quant_inteira=int(input(" Quantos ingressos de entrada-inteira você quer? "))
                    quant_meia=int(input(" Quantos ingressos de meia-entrada você quer? "))
                    valor_inteira=ingresso_inteira*quant_inteira
                    valor_meia=ingresso_meia*quant_meia
                    print(" O valor dos ingressos entrada-inteira fica: R$",valor_inteira)
                    print(" O valor dos ingressos meia-entrada fica: R$",valor_meia)
                    valor_final=valor_inteira+valor_meia
                    print(" O valor final de todos os ingressos fica: R$", valor_final)
                    print(" As formas de pagamento são:")
                    print(" Cartão")
                    print(" Boleto")
                    print(" Pix")
                    pagamento=str(input(" Qual dessas formas de pagamento você quer? "))
                    if pagamento=='cartao':
                        print(" Você escolheu Cartão!")
                        cartao=int(input(" Agora digite o número do cartão: "))
                        codigo=int(input(" Agora digite o código de segurança: "))
                        print(" Pronto, tudo pago e computado no sistema!")
                        print(" Tenha um bom filme e até a próxima!")
                    elif pagamento=='boleto':
                        print(" O código de barras do Boleto é:")
                        print(" 450460632662665675710730750765835845855865870888")
                        numero=int(input(" Digite seu número de telefone (com DDD e todos os números juntos): ")) 
                        print(" Você tem 5 dias úteis para efetuar o pagamento no Boleto")                     
                        print(" Se não pagar nesse prazo, a compra será totalmente cancelada")
                        print(" Assim que o pagamento for aprovado, vicê receberá um SMS de aviso")
                        print(" Por enquanto é isso, agradecemos a sua compra e visita!")
                    elif pagamento=='pix':
                        print(" Você escolheu Pix!")
                        print(" A chave do Pix é:")
                        print(" dudu@cinema.com")
                        numero=int(input(" Digite seu número de telefone (com DDD e todos os números juntos): "))
                        print(" Você tem 5 dias úteis para efetuar o pagamento no Boleto")
                        print(" Se não pagar nesse prazo, a compra será totalmente cancelada")
                        print(" Assim que o pagamento for aprovado, vicê receberá um SMS de aviso")
                        print(" Por enquanto é isso, agradecemos a sua compra e visita!")
                elif tresd=='nao':
                    print(" Você escolheu Sem 3D!")
                    ingresso_inteira=float(34.00)
                    ingresso_meia=float(17.00)
                    print(" O valor do ingresso de entrada-inteira é R$", ingresso_inteira)
                    print(" O valor do ingresso de meia-entrada é R$", ingresso_meia)
                    quant_inteira=int(input(" Quantos ingressos de entrada-inteira você quer? "))
                    quant_meia=int(input(" Quantos ingressos de meia-entrada você quer? "))
                    valor_inteira=ingresso_inteira*quant_inteira
                    valor_meia=ingresso_meia*quant_meia
                    print(" O valor dos ingressos entrada-inteira fica: R$",valor_inteira)
                    print(" O valor dos ingressos meia-entrada fica: R$",valor_meia)
                    valor_final=valor_inteira+valor_meia
                    print(" O valor final de todos os ingressos fica: R$", valor_final)
                    print(" As formas de pagamento são:")
                    print(" Cartão")
                    print(" Boleto")
                    print(" Pix")
                    pagamento=str(input(" Qual dessas formas de pagamento você quer? "))
                    if pagamento=='cartao':
                        print(" Você escolheu Cartão!")
                        cartao=int(input(" Agora digite o número do cartão: "))
                        codigo=int(input(" Agora digite o código de segurança: "))
                        print(" Pronto, tudo pago e computado no sistema!")
                        print(" Tenha um bom filme e até a próxima!")
                    elif pagamento=='boleto':
                        print(" O código de barras do Boleto é:")
                        print(" 450460632662665675710730750765835845855865870888")
                        numero=int(input(" Digite seu número de telefone (com DDD e todos os números juntos): ")) 
                        print(" Você tem 5 dias úteis para efetuar o pagamento no Boleto")                     
                        print(" Se não pagar nesse prazo, a compra será totalmente cancelada")
                        print(" Assim que o pagamento for aprovado, vicê receberá um SMS de aviso")
                        print(" Por enquanto é isso, agradecemos a sua compra e visita!")
                    elif pagamento=='pix':
                        print(" Você escolheu Pix!")
                        print(" A chave do Pix é:")
                        print(" dudu@cinema.com")
                        numero=int(input(" Digite seu número de telefone (com DDD e todos os números juntos): "))
                        print(" Você tem 5 dias úteis para efetuar o pagamento no Boleto")
                        print(" Se não pagar nesse prazo, a compra será totalmente cancelada")
                        print(" Assim que o pagamento for aprovado, vicê receberá um SMS de aviso")
                        print(" Por enquanto é isso, agradecemos a sua compra e visita!")
                else:
                    print("\n Você digitou errado, feche o programa e tente novamente! \n")
        else:
            print("\n Você digitou errado, feche o programa e tente novamente! \n")
    else:
        print("\n Você digitou errado, feche o programa e tente novamente! \n")

def doutor():
    print("\n Você escolheu Doutor Estranho no Multiverso da Loucura!")
    mes=str(input(" Que mês você quer?(maio ou junho): "))
    if mes=='maio':
        print(" Você escolheu o mês de Maio!")
        dia=int(input(" Que dia você quer?(digite de 5 a 31): "))
        if dia>=5 and dia<=31:
            print(" Você escolheu dia", dia, "de Maio!")
            print(" Os horários disponíveis são:")
            print(" 13h45   14h20   15h15")
            print(" 16h05   17h30   18h00")
            print(" 19h15   20h35   21h05")
            print(" 22h50")
            print(" Qual horário você quer?")
            horario=int(input(" (digite os três primeiros dígitos, exemplo: '17'): "))
            if horario>=13 and horario<=22:
                if horario==13:
                    horario=str(horario)
                    horario=horario+"h45!"
                elif horario==14:
                    horario=str(horario)
                    horario=horario+"h20!"
                elif horario==15:
                    horario=str(horario)
                    horario=horario+"h15!"
                elif horario==16:
                    horario=str(horario)
                    horario=horario+"h05!"
                elif horario==17:
                    horario=str(horario)
                    horario=horario+"h30!"
                elif horario==18:
                    horario=str(horario)
                    horario=horario+"h00!"
                elif horario==19:
                    horario=str(horario)
                    horario=horario+"h15!"
                elif horario==20:
                    horario=str(horario)
                    horario=horario+"h35!"
                elif horario==21:
                    horario=str(horario)
                    horario=horario+"h05!"
                elif horario==22:
                    horario=str(horario)
                    horario=horario+"h50!"
                print(" Você escolheu o horário das", horario)
                tresd=str(input("\n Você quer com 3D?(sim ou não): "))
                if tresd=='sim':
                    print(" Você escolheu Com 3D!")
                    ingresso_inteira=float(42.00)
                    ingresso_meia=float(21.00)
                    print(" O valor do ingresso de entrada-inteira é R$",ingresso_inteira)
                    print(" O valor do ingresso de meia-entrada é R$",ingresso_meia)
                    quant_inteira=int(input(" Quantos ingressos de entrada-inteira você quer? "))
                    quant_meia=int(input(" Quantos ingressos de meia-entrada você quer? "))
                    valor_inteira=ingresso_inteira*quant_inteira
                    valor_meia=ingresso_meia*quant_meia
                    print(" O valor dos ingressos entrada-inteira fica: R$",valor_inteira)
                    print(" O valor dos ingressos meia-entrada fica: R$",valor_meia)
                    valor_final=valor_inteira+valor_meia
                    print(" O valor final de todos os ingressos fica: R$", valor_final)
                    print(" As formas de pagamento são:")
                    print(" Cartão")
                    print(" Boleto")
                    print(" Pix")
                    pagamento=str(input(" Qual dessas formas de pagamento você quer? "))
                    if pagamento=='cartao':
                        print(" Você escolheu Cartão!")
                        cartao=int(input(" Agora digite o número do cartão: "))
                        codigo=int(input(" Agora digite o código de segurança: "))
                        print(" Pronto, tudo pago e computado no sistema!")
                        print(" Tenha um bom filme e até a próxima!")
                    elif pagamento=='boleto':
                        print(" O código de barras do Boleto é:")
                        print(" 450460632662665675710730750765835845855865870888")
                        numero=int(input(" Digite seu número de telefone (com DDD e todos os números juntos): ")) 
                        print(" Você tem 5 dias úteis para efetuar o pagamento no Boleto")                     
                        print(" Se não pagar nesse prazo, a compra será totalmente cancelada")
                        print(" Assim que o pagamento for aprovado, vicê receberá um SMS de aviso")
                        print(" Por enquanto é isso, agradecemos a sua compra e visita!")
                    elif pagamento=='pix':
                        print(" Você escolheu Pix!")
                        print(" A chave do Pix é:")
                        print(" dudu@cinema.com")
                        numero=int(input(" Digite seu número de telefone (com DDD e todos os números juntos): "))
                        print(" Você tem 5 dias úteis para efetuar o pagamento no Boleto")
                        print(" Se não pagar nesse prazo, a compra será totalmente cancelada")
                        print(" Assim que o pagamento for aprovado, vicê receberá um SMS de aviso")
                        print(" Por enquanto é isso, agradecemos a sua compra e visita!")
                elif tresd=='nao':
                    print(" Você escolheu Sem 3D!")
                    ingresso_inteira=float(34.00)
                    ingresso_meia=float(17.00)
                    print(" O valor do ingresso de entrada-inteira é R$", ingresso_inteira)
                    print(" O valor do ingresso de meia-entrada é R$", ingresso_meia)
                    quant_inteira=int(input(" Quantos ingressos de entrada-inteira você quer? "))
                    quant_meia=int(input(" Quantos ingressos de meia-entrada você quer? "))
                    valor_inteira=ingresso_inteira*quant_inteira
                    valor_meia=ingresso_meia*quant_meia
                    print(" O valor dos ingressos entrada-inteira fica: R$",valor_inteira)
                    print(" O valor dos ingressos meia-entrada fica: R$",valor_meia)
                    valor_final=valor_inteira+valor_meia
                    print(" O valor final de todos os ingressos fica: R$", valor_final)
                    print(" As formas de pagamento são:")
                    print(" Cartão")
                    print(" Boleto")
                    print(" Pix")
                    pagamento=str(input(" Qual dessas formas de pagamento você quer? "))
                    if pagamento=='cartao':
                        print(" Você escolheu Cartão!")
                        cartao=int(input(" Agora digite o número do cartão: "))
                        codigo=int(input(" Agora digite o código de segurança: "))
                        print(" Pronto, tudo pago e computado no sistema!")
                        print(" Tenha um bom filme e até a próxima!")
                    elif pagamento=='boleto':
                        print(" O código de barras do Boleto é:")
                        print(" 450460632662665675710730750765835845855865870888")
                        numero=int(input(" Digite seu número de telefone (com DDD e todos os números juntos): ")) 
                        print(" Você tem 5 dias úteis para efetuar o pagamento no Boleto")                     
                        print(" Se não pagar nesse prazo, a compra será totalmente cancelada")
                        print(" Assim que o pagamento for aprovado, vicê receberá um SMS de aviso")
                        print(" Por enquanto é isso, agradecemos a sua compra e visita!")
                    elif pagamento=='pix':
                        print(" Você escolheu Pix!")
                        print(" A chave do Pix é:")
                        print(" dudu@cinema.com")
                        numero=int(input(" Digite seu número de telefone (com DDD e todos os números juntos): "))
                        print(" Você tem 5 dias úteis para efetuar o pagamento no Boleto")
                        print(" Se não pagar nesse prazo, a compra será totalmente cancelada")
                        print(" Assim que o pagamento for aprovado, vicê receberá um SMS de aviso")
                        print(" Por enquanto é isso, agradecemos a sua compra e visita!")
                else:
                    print("\n Você digitou errado, feche o programa e tente novamente! \n")
        else:
            print("\n Você digitou errado, feche o programa e tente novamente! \n")

    elif mes=='junho':
        print(" Você escolheu o mês de Junho!")
        dia=int(input(" Que dia você quer?(digite de 1 a 6): "))
        if dia>=1 and dia<=6:
            print(" Você escolheu dia", dia, "de Junho!")
            print(" Os horários disponíveis são:")
            print(" 13h45   14h20   15h15")
            print(" 16h05   17h30   18h00")
            print(" 19h15   20h35   21h05")
            print(" 22h50")
            print(" Qual horário você quer?")
            horario=int(input(" (digite os três primeiros dígitos, exemplo: '17'): "))
            if horario>=13 and horario<=22:
                if horario==13:
                    horario=str(horario)
                    horario=horario+"h45!"
                elif horario==14:
                    horario=str(horario)
                    horario=horario+"h20!"
                elif horario==15:
                    horario=str(horario)
                    horario=horario+"h15!"
                elif horario==16:
                    horario=str(horario)
                    horario=horario+"h05!"
                elif horario==17:
                    horario=str(horario)
                    horario=horario+"h30!"
                elif horario==18:
                    horario=str(horario)
                    horario=horario+"h00!"
                elif horario==19:
                    horario=str(horario)
                    horario=horario+"h15!"
                elif horario==20:
                    horario=str(horario)
                    horario=horario+"h35!"
                elif horario==21:
                    horario=str(horario)
                    horario=horario+"h05!"
                elif horario==22:
                    horario=str(horario)
                    horario=horario+"h50!"
                print(" Você escolheu o horário das", horario)
                tresd=str(input("\n Você quer com 3D?(sim ou não): "))
                if tresd=='sim':
                    print(" Você escolheu Com 3D!")
                    ingresso_inteira=float(42.00)
                    ingresso_meia=float(21.00)
                    print(" O valor do ingresso de entrada-inteira é R$",ingresso_inteira)
                    print(" O valor do ingresso de meia-entrada é R$",ingresso_meia)
                    quant_inteira=int(input(" Quantos ingressos de entrada-inteira você quer? "))
                    quant_meia=int(input(" Quantos ingressos de meia-entrada você quer? "))
                    valor_inteira=ingresso_inteira*quant_inteira
                    valor_meia=ingresso_meia*quant_meia
                    print(" O valor dos ingressos entrada-inteira fica: R$",valor_inteira)
                    print(" O valor dos ingressos meia-entrada fica: R$",valor_meia)
                    valor_final=valor_inteira+valor_meia
                    print(" O valor final de todos os ingressos fica: R$", valor_final)
                    print(" As formas de pagamento são:")
                    print(" Cartão")
                    print(" Boleto")
                    print(" Pix")
                    pagamento=str(input(" Qual dessas formas de pagamento você quer? "))
                    if pagamento=='cartao':
                        print(" Você escolheu Cartão!")
                        cartao=int(input(" Agora digite o número do cartão: "))
                        codigo=int(input(" Agora digite o código de segurança: "))
                        print(" Pronto, tudo pago e computado no sistema!")
                        print(" Tenha um bom filme e até a próxima!")
                    elif pagamento=='boleto':
                        print(" O código de barras do Boleto é:")
                        print(" 450460632662665675710730750765835845855865870888")
                        numero=int(input(" Digite seu número de telefone (com DDD e todos os números juntos): ")) 
                        print(" Você tem 5 dias úteis para efetuar o pagamento no Boleto")                     
                        print(" Se não pagar nesse prazo, a compra será totalmente cancelada")
                        print(" Assim que o pagamento for aprovado, vicê receberá um SMS de aviso")
                        print(" Por enquanto é isso, agradecemos a sua compra e visita!")
                    elif pagamento=='pix':
                        print(" Você escolheu Pix!")
                        print(" A chave do Pix é:")
                        print(" dudu@cinema.com")
                        numero=int(input(" Digite seu número de telefone (com DDD e todos os números juntos): "))
                        print(" Você tem 5 dias úteis para efetuar o pagamento no Boleto")
                        print(" Se não pagar nesse prazo, a compra será totalmente cancelada")
                        print(" Assim que o pagamento for aprovado, vicê receberá um SMS de aviso")
                        print(" Por enquanto é isso, agradecemos a sua compra e visita!")
                elif tresd=='nao':
                    print(" Você escolheu Sem 3D!")
                    ingresso_inteira=float(34.00)
                    ingresso_meia=float(17.00)
                    print(" O valor do ingresso de entrada-inteira é R$", ingresso_inteira)
                    print(" O valor do ingresso de meia-entrada é R$", ingresso_meia)
                    quant_inteira=int(input(" Quantos ingressos de entrada-inteira você quer? "))
                    quant_meia=int(input(" Quantos ingressos de meia-entrada você quer? "))
                    valor_inteira=ingresso_inteira*quant_inteira
                    valor_meia=ingresso_meia*quant_meia
                    print(" O valor dos ingressos entrada-inteira fica: R$",valor_inteira)
                    print(" O valor dos ingressos meia-entrada fica: R$",valor_meia)
                    valor_final=valor_inteira+valor_meia
                    print(" O valor final de todos os ingressos fica: R$", valor_final)
                    print(" As formas de pagamento são:")
                    print(" Cartão")
                    print(" Boleto")
                    print(" Pix")
                    pagamento=str(input(" Qual dessas formas de pagamento você quer? "))
                    if pagamento=='cartao':
                        print(" Você escolheu Cartão!")
                        cartao=int(input(" Agora digite o número do cartão: "))
                        codigo=int(input(" Agora digite o código de segurança: "))
                        print(" Pronto, tudo pago e computado no sistema!")
                        print(" Tenha um bom filme e até a próxima!")
                    elif pagamento=='boleto':
                        print(" O código de barras do Boleto é:")
                        print(" 450460632662665675710730750765835845855865870888")
                        numero=int(input(" Digite seu número de telefone (com DDD e todos os números juntos): ")) 
                        print(" Você tem 5 dias úteis para efetuar o pagamento no Boleto")                     
                        print(" Se não pagar nesse prazo, a compra será totalmente cancelada")
                        print(" Assim que o pagamento for aprovado, vicê receberá um SMS de aviso")
                        print(" Por enquanto é isso, agradecemos a sua compra e visita!")
                    elif pagamento=='pix':
                        print(" Você escolheu Pix!")
                        print(" A chave do Pix é:")
                        print(" dudu@cinema.com")
                        numero=int(input(" Digite seu número de telefone (com DDD e todos os números juntos): "))
                        print(" Você tem 5 dias úteis para efetuar o pagamento no Boleto")
                        print(" Se não pagar nesse prazo, a compra será totalmente cancelada")
                        print(" Assim que o pagamento for aprovado, vicê receberá um SMS de aviso")
                        print(" Por enquanto é isso, agradecemos a sua compra e visita!")
                else:
                    print("\n Você digitou errado, feche o programa e tente novamente! \n")
        else:
            print("\n Você digitou errado, feche o programa e tente novamente! \n")
    else:
        print("\n Você digitou errado, feche o programa e tente novamente! \n")

print("\n Atenção! Responda todos os itens só com o primeiro nome,")
print(" sem acento e siga as instruções entre ()")
print("\n Cinema's Dudu")
print(" Seja Bem-Vindo")
pergunta=str(input(" Gostaria de comprar ingressos?(sim ou não): "))
if pergunta=='sim':
    print("\n Os filmes disponíveis são:")
    print(" Uncharted: Fora do Mapa")
    print(" Batman")
    print(" Sonic 2")
    print(" Doutor Estranho no Multiverso da Loucura")
    filme=str(input(" Qual desses filmes você quer?(digite o primeiro nome do filme): "))
    if filme=='uncharted':
        uncharted()
    elif filme=='batman':
        batman()
    elif filme=='sonic':
        sonic()
    elif filme=='doutor':
        doutor()
    else:
        print("\n Você digitou errado, feche o programa e tente novamente! \n")
        
elif pergunta=='nao':
    print("\n Tudo bem então, agradecemos a sua visita! \n")
else:
    print("\n Você digitou errado, feche o programa e tente novamente! \n")