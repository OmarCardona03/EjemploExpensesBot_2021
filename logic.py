##############################################################

def get_about_this(VERSION):
    response = (
        f"Simple Expenses Bot (pyTelegramBot) v{VERSION}"
        "\n\n"
        "Desarrollado por Omar Cardona <joseo.cardonag@autonoma.edu.co>"
    )
    return response

##############################################################

def get_help_message ():
    response = (
        "Estos son los comandos y órdenes disponibles:\n"
        "\n"
        "*/start* - Inicia la interacción con el bot (obligatorio)\n"
        "*/help* - Muestra este mensaje de ayuda\n"
        "*/about* - Muestra detalles de esta aplicación\n"
        "*gane|gané|g {cantidad}* - Registra un saldo positivo\n"
        "*gaste|gasté|gg {cantidad}* - Registra un saldo negativo\n"
        "*listar ganancias|lg en {índice_mes} de {año}* - Lista las ganancias de un mes/año\n"
        "*listar gastos|lgg en {mes} de {año}* - Lista los gastos de un    mes/año\n"
        "*obtener saldo|s* - Muestra el saldo actual (disponible)\n"
        "*remover|r ganancia|g|gasto|gg {índice}* - Remueve una ganancia o un gasto según su índice\n"
        "*listar cuentas|lc* - Lista las cuentas registradas (sólo   admin)\n"
    )
    return response