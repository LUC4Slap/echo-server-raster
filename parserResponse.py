class ParserResponse(object):
    def __init__(self):
        self.hdr = ""
        self.imei = ""
        self.cmd_atualizado = ""
        self.gps_ligado_desligado = ""
        self.data_hex = ""
        self.hora_hex = ""
        self.lat_hex = ""
        self.lng_hex = ""
        self.velocidade_hex = ""
        self.direcao_hex = ""
        self.status = ""
        self.sinal = ""
        self.bat_interna = ""
        self.combustivel = ""
        self.hodometro_hex = ""
        self.altitude = ""
        self.dados_GPS = ""
        self.RDFI = ""
        self.temperatura = ""
        self.bat_externa = ""
        self.qtd_satelites = ""

    def hex_to_lat_or_lng_string(self, hex_lat_or_lng):
        negativo = False
        if hex_lat_or_lng.startswith("8"):
            hex_lat_or_lng = hex_lat_or_lng[1:]
            negativo = True

        decimal_lat_or_lng = int(hex_lat_or_lng, 16) / 600000.0

        if negativo:
            decimal_lat_or_lng *= -1

        string_lat_or_lng = f"{decimal_lat_or_lng:.6f}"

        return string_lat_or_lng

    def parser_afeter_save(self, response):
        dados = response.split(",")
        if "*ET" in dados:
            self.parserBW3(dados)

    def parserBW3(self, dados):
        if "*ET" and "HB" in dados:
            # AQUI É QUANDO O RASTREADOR MANDA A STRING COM A LATITUDO E LONGITUDE
            self.hdr = dados[0]
            self.imei = dados[1]
            self.cmd_atualizado = dados[2]
            self.gps_ligado_desligado = dados[3]
            self.data_hex = dados[4]
            self.hora_hex = dados[5]
            self.lat_hex = self.hex_to_lat_or_lng_string(dados[6])
            self.lng_hex = self.hex_to_lat_or_lng_string(dados[7])
            self.velocidade_hex = dados[8]
            self.direcao_hex = dados[9]
            self.status = dados[10]
            self.sinal = dados[12]
            self.bat_interna = dados[13]
            self.combustivel = dados[14]
            self.hodometro_hex = dados[15]
            self.altitude = dados[16]
            self.dados_GPS = dados[17]
            self.RDFI = dados[18]
            self.temperatura = dados[19]
            self.bat_externa = dados[20]
            # self.qtd_satelites = dados[21]
            print(self.lat_hex)
            print(self.lng_hex)
        elif "*ET" and "JZ" in dados:
            print("JZ")
        elif "*ET" and "TX" in dados:
            print("TX")
