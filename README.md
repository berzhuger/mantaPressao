#Projeto Manta de Pressão
- Definições da coleta de dados da manta de pressão:
 - A comunicação vai ser feita via Web Service desenvolvido em python
 - Sera feita a comunicação via Protocolo HTTP/HTTPS sendo enviado uma requisição POST no determinado endpoint:
     - ceted.feevale.br:{porta}/dados_coleta/ (porta a definir)
 - Segue a estrutura que deve ser enviado, todos os campos listados são obrigatorios.
 - Estrutura em JSON:
 ```json
{
    "nome":"Igor Viana",
    "id_avaliacao":4,
    "data_nascimento":"1950-01-01",
    "data_hora_inicio":"2018-01-01 15:56:23",
    "data_hora_fim":"2018-01-01 15:59:23",
    "dados_sensor": {
        "sensor_01":45,
        "sensor_02":45,
        "sensor_03":45,
        "sensor_04":45,
        "sensor_05":45,
        "sensor_06":45,
        "sensor_07":45,
        "sensor_08":45,
        "sensor_09":45,
        "sensor_10":45,
        "sensor_11":45,
        "sensor_12":45,
        "sensor_13":45,
        "sensor_14":45,
        "sensor_15":45,
        "sensor_16":45,
        "sensor_17":45,
        "sensor_18":45,
        "sensor_19":45,
        "sensor_20":45,
        "sensor_21":45,
        "sensor_22":45,
        "sensor_23":45,
        "sensor_24":45,
        "sensor_25":45,
        "sensor_26":45,
        "sensor_27":45,
        "sensor_28":45,
        "sensor_29":45,
        "sensor_30":45,
        "sensor_31":45,
        "sensor_32":45,
        "sensor_33":45,
        "sensor_34":45,
        "sensor_35":45,
        "sensor_36":45,
        "sensor_37":45,
        "sensor_38":45,
        "sensor_39":45,
        "sensor_40":45,
        "sensor_41":45,
        "sensor_42":45,
        "sensor_43":45,
        "sensor_44":45,
        "sensor_45":45,
        "sensor_46":45,
        "sensor_47":45,
        "sensor_48":45,
        "sensor_49":45,
        "sensor_50":45,
        "sensor_51":45,
        "sensor_52":45,
        "sensor_53":45,
        "sensor_54":45,
        "sensor_55":45,
        "sensor_56":45
    }
}
