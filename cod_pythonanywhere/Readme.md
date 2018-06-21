O arquivo "cod_raspberry.py" deve ser subido no Pythonanywhere y ser executado (para maior detalhe, pode ser de ajuda o seguinte pagina web https://blog.pythonanywhere.com/121/)

O arquivo faz o seguinte, faz modificação no arquivo ``dataset.txt``: 
- tem o módulo add/<text1>, que salva o valor de text1 no final do arquivo ''dataset.txt'' 
  (http://reynaldocv.pythonanywhere.com/add/2018-06-20 20:31:53.115132,2,20,31,3)
- tem o módulo dataset/, que devolve toda a informação do ``dataset.txt``
  (http://reynaldocv.pythonanywhere.com/dataset)
- tem o módulo futuro/<dia>/<hora>/<minutos>, que devolve a predição de quantas vagas vai ter no dia, hora e minutos especificados, usando o ''dataset.txt`` como informação base
e usando um algoritmo de Machine Learning. 
  (http://reynaldocv.pythonanywhere.com/futuro/3/14/39)
