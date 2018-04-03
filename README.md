
# IoT-project (Fundamentos da Internet das Coisas)

- Visão geral do projeto: 

O projeto consiste em saber que coisas (insumos) têm ou não têm dentro de refrigerador. 

A projeto a discutir, pode ajudar às pessoas no momento de saber as compras, proporcionando uma lista
das coisas que tinham no refrigerador e que agora não tem. Assim, também é possível saber que insumos 
são consumidos muito rápido para recomendar sua compra em maior quantidade.

- Público alvo: 

Toda pessoa que tem um refrigerador. 

# Descrição técnica
- Sensores: 

  - Sensor de Luminosidade LDR 5mm (Modelo: GL5528)
O LDR (Light Dependent Resistor) é um componente cuja resistência varia de acordo com a intensidade da luz. Quanto mais luz incidir sobre o componente, menor a resistência. Este sensor de luminosidade pode ser utilizado em projetos com arduino e outros microcontroladores para alarmes, automação residencial, sensores de presença e etc.
  
     - Especificações:      
        - Diâmetro: 5mm
        - Tensão máxima: 150VDC
        - Potência máxima: 100mW
        - Tensão de operação:  -30°C a 70°C
        - Espectro: 540nm
        - Comprimento com terminais: 32mm
        - Resistência no escuro: 1 MΩ (Lux 0)
        - Resistência na luz: 10-20 KΩ (Lux 10)
      - Características:
        - muaja
        - muaja
      
      
  - O sensor temperatura (Modelo LM35) 
é um sensor de precisão que apresenta uma saída de tensão linear proporcional à temperatura em que ele se encontrar no momento, tendo em sua saída um sinal de 10mV para cada Grau Célsius de temperatura.

      - Especificações:      
        - Tensão de Alimentação:  4-30V;
        - Escala Linear: + 10.0 mV/˚C;
        - Temperatura de trabalho em modo básico: 2 a 150ºC;
        - Temperatura de trabalho em range completo: -55 a +150º C;
        - Baixa impedância de saída
      - Características:
        - Diâmetro: 5mm
        
- Módulos:

  - O módulo câmera VGA OV7670 é um módulo que permite a captura e armazenamento de imagens coloridas pelo seu Arduino, com        uma taxa de atualização de até 30 frames por segundo, com resolução máxima de 640 x 480 Pixels.
      - Especificações:      
        - Tensão de Alimentação:  4-30V;
        - Escala Linear: + 10.0 mV/˚C;
        - Temperatura de trabalho em modo básico: 2 a 150ºC;
        - Temperatura de trabalho em range completo: -55 a +150º C;
        - Baixa impedância de saída
      - Características:
        - Diâmetro: 5mm
        - 
        <img src="http://lmsotfy.com/so.png" "width=50%"/>
      ![stack Overflow](http://lmsotfy.com/so.png)
      
## Open-design (extra)
(Apresentar o design técnico do projeto utilizando alguma ferramenta de diagrama ou mesmo um desenho à mão. Sugestão de ferramentas: Draw.io, Fritzing.org, Gimp.)


# Descrição da arquitetura
A seguir vamos explicar o fluxo da informação:

1).- Cada vez que uma pessoa abre um refrigerador, a luz dele é ligada. É nesse instante que nosso sensor de luminosidade
é ativado e manda uma sinal para a câmera e tirar uma foto. 
