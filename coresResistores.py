def resistor_color_bands(resistance):
    color_codes = ['preto', 'marrom', 'vermelho', 'laranja', 'amarelo', 'verde', 'azul', 'roxo', 'cinza', 'branco']
    return color_codes[int(resistance[0])], color_codes[int(resistance[1])], color_codes[len(resistance) - 2]

resistance = input("Enter the resistance value (in ohms): ")
color_bands = resistor_color_bands(resistance)
print("The color bands of the resistor are:", color_bands)
