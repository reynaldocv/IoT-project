
# IoT-project (Vagas no Estacionamento)

- Visão geral do projeto: 

    O projeto consiste em saber se tem vagas (ou não) num estacionamento. 

    A projeto a discutir, pode ajudar às pessoas a saber onde eles podem estacionar seu veiculo (no momento), e
fazer uma estimativa a futuro se no estacionamento.


<p align="center">
  <img height="200" src="/img/img_car.jpeg">    
   
</p>


# Descrição técnica
  
- RASPBERRY PI 3 MODEL B: É um computador de baixo custo e que tem o tamanho de um cartão de crédito desenvolvido no Reino Unido pela Fundação Raspberry Pi. Para usá-lo, basta plugar um teclado e um mouse padrão a ele e conectar tudo isso a um monitor ou a uma televisão. Os modelos custam entre US$ 25 e US$ 35.

<p align="center">
  <img src="/img/Raspberry.png">
</p>


      - Especificações:      
        - A 1.2GHz 64-bit quad-core ARMv8 CPU
        - 802.11n Wireless LAN
        - Bluetooth 4.1 & Bluetooth Low Energy (BLE)
        - BCM2837, 1.2GHz 64-bit quad-core ARM Cortex-A53
        - 1GB RAM
        - 10/100 Ethernet port
        - 802.11n WiFi NIC
        - Bluetooth 4.1 & Bluetooth Low Energy (BLE)
        - HDMI port
        - USB 2.0 interface x 4
        - Micro SD card slot
        - Combined 3.5mm audio jack and composite video
        - 40-pin GPIO interface
        - Camera interface (CSI)
        - Display interface (DSI)
        - Upgraded power management
        - supports more peripherals (requires a 2.5A - 3.0A power supply)Tensão de Alimentação:  4-30V;
        
 - 2 Câmeras: Usamos dois tipos: uma de um celular e outra com conexão USB.
   - Camera Multilaser WC040

  <p align="center">
  <img height="200" src="/IoT project - slides/img/slide_cam1.jpeg">    
   - Celular LG G3
  <img height="200" src="/IoT project - slides/img/slide_cam2.jpg">
  </p>
        
        
## Open-design (extra)


<p align="center">
   <img height="600" src="/IoT project - slides/img/estrutura.jpeg">
</p>

# Instalação
- Em um dos celulares:
    
    - Instalamos o aplicativo IP Webcam e executamos. O aplicativo dá um IP (que pode ser acessado numa LAN) onde nós podemos monitorar usando qualquer navegador web (veja a seguiente pagina web https://pplware.sapo.pt/smartphones-tablets/android/ip-webcam-como-usar-o-seu-android-como-uma-webcam/ para mais dados).

- No Raspberry (deve estar na misma LAN do celular com o IP Webcam):
    
    - Executamos o seguinte [código em python](cod_raspberry/cam.py) que tira a imagen do IP Webcam e que é subida num host (nesse caso foi https://www.ime.usp.br/~reynaldo/phd/internet_coisas/ e processo acontece cada 1 seg.).
    
- No https://www.pythonanywhere.com/:
    
    - Criamos os seguintes APIs executando o seguinte [código em python](cod_pythonanywhere/app_flask.py) que tem comandos para fazer consultas na "API de Pesquisa de Visual Computational" (Veja as seguintes paginas web https://techtutorialsx.com/2016/12/27/python-anywhere-deploying-a-flask-server-on-the-cloud/ e https://azure.microsoft.com/pt-br/services/cognitive-services/computer-vision/ para mais dados). Os servicios criados foram:
        
        - http://reynaldocv.pythonanywhere.com/add/<text1>
        - http://reynaldocv.pythonanywhere.com/dataset/
        - http://reynaldocv.pythonanywhere.com/futuro/<dia>/<hora>/<minutos>
        
- No outro celular:

    - Instalamos o [Android APP](/cod_android/app_debug.apk) que foi fieto en Android Studio (java) usando as bibliotecas Picasso (mostrar imagens da web) e Retrofit (consumo de API services) (http://square.github.io/picasso/ e http://blog.matheuscastiglioni.com.br/consumindo-web-service-no-android-com-retrofit). O código do app está localizado em 
    [cod_android](/cod_android/).


# Descrição da arquitetura

O raspberry tira as imagens de um dos celulares que tem instalado do IP Webcam y joga na internet, Isso é feito cada certo tempo (por exemplo: cada 2 segundos).

Com o outro celular, fazemos uso de um API service https://reynaldocv.pythonanywhere.com. esse servicio pega a imagem da internet e faz um análise con o API de Pesquisa em Visual Computational para saber a descricao da imagem. e no celular é so mostrar.

# Exemplo 1

 <p align="center">
  <img src="/img/exemplo.png">
</p>

# Exemplo 2

 <p align="center">
  <img src="/img/vagas.png">
</p>


