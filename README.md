# instal lib
sudo python3 -m pip install lib_name


comparar o paralelismo paralelizando os dados das colunas e dividindo em colunas em si
comparara a eecução na minha maquina e no raspberry


https://gist.github.com/yong27/7869662

# Limpeza

- dividido o conjunto de elementos em *n* partes, onde cada parte é enviada para um processo efetuar a limpeza dos dados

# Transformação

- media, desvio padrão, variância: (cálculo dos valores é independente) dividido o conjunto de elementos em *n* partes, onde cada parte é enviada para um processo efetuar o cálculo, depois os resultados são somados e o total é dividido pela quantidade de elementos

# Dúvidas

- é melhor rodar cada paralelização independente ou dividir o conjunto em *n* partes e efetuar a limpeza e transformação todos em uma execução?
