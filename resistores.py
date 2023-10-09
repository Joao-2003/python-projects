try:
    q_leds = int(input("Digite a quantidade de leds: "))
    s_ou_p = input("Digite p se o circuito for em paralelo e s se for em serie: ")
    t_fonte = int(input("Digite a tensão da fonte: "))
    t_led = int(input("Digite a tensão dos leds: "))
    i = int(input("Digite a corrente (em mili Amperes): "))
except:
    print("Os valores digitados sao invalidos")

if s_ou_p in "SsseriesérieSERIESÉRIESerieSérie":
    r = (t_fonte - (q_leds * t_led))/(i/1000)
    print("A quantidade de resistores eh 1 e a resistencia eh igual a ",r)
elif s_ou_p in "PpparaleloParaleloPARALELO":
    r = (t_fonte - t_led)/(i/1000)
    print("A quantidade de resistores eh ",q_leds," e a resistencia eh igual a ",r)
else:
    print("Tipo de circuito invalido")
