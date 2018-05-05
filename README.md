
# IoT-project (Vagas no Estacionamento)

- Visão geral do projeto: 

    O projeto consiste em saber se tem vagas (ou não) num estacionamento. 

    A projeto a discutir, pode ajudar às pessoas a saber onde eles podem estacionar seu veiculo (no momento), e
fazer uma estimativa a futuro se no estacionamento.


<p align="center">
  <img src="/img/img_car.png">
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
        
 - 2 CELULARES: Um para usar sua camera, e outro para usar o aplicativo, de preferência com Android OS.

  <p align="center">
  <img src="/img/celulares.png">
</p>
        
        
## Open-design (extra)


<p align="center">
  <img src="/img/diagrama.png">
</p>

# Instalação
- Em um dos celulares:
    - Instalamos o aplicativo IP Webcam e executamos. O aplicativo dá um IP (que pode ser acessado numa LAN) onde nós podemos monitorar usando qualquer navegador web (veja a seguiente pagina web https://pplware.sapo.pt/smartphones-tablets/android/ip-webcam-como-usar-o-seu-android-como-uma-webcam/ para mais dados).

- No Raspberry (deve estar na misma LAN do celular com o IP Webcam):
    - Executamos o seguinte [código em python](cod_raspberry/cam.py) que tira a imagen do IP Webcam e que é subida num host (nesse caso foi https://www.ime.usp.br/~reynaldo/phd/internet_coisas/ e processo acontece cada 1 seg.).
    
    
    
    


# Descrição da arquitetura

A seguir vamos explicar o fluxo da informação:

Cada vez que uma pessoa, quer saber se tem uma vaga no estacionamento, manda una sinal para o Arduino, 
e tira uma foto (usando o módulo ) no estacionamento, E essa foto é enviada para seu processamento (usando o módulo ).
E o sistema sabendo quantos carros tem na foto, joga o número de vagas.

Com esses dados, podemos fazer um monte de reportes: 
 - (No momento) Quantas vagas tem no estacionamento.
 - (Estimativas pro futuro) Quantas vagas vai ter, segundo aos dados anteriores? 
 
## Referências   
 - https://portal.vidadesilicio.com.br/sensor-de-luz-com-ldr/
 - https://www.filipeflop.com/produto/sensor-de-luminosidade-ldr-5mm/
 - https://portal.vidadesilicio.com.br/lm35-medindo-temperatura-com-arduino/
 - https://www.arduinoecia.com.br/2013/02/lm35-sensor-de-temperatura.html
 - https://www.filipeflop.com/blog/modulo-camera-vga-ov7670/
 - https://www.robocore.net/loja/produtos/modulo-wifi-esp8266.html
 - https://www.embarcados.com.br/modulo-esp8266/


