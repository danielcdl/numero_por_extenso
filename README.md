# Número por extenso
Módulo para escrever números por extenso (número real e monetário)

## Instalação
```python
pip install numero-por-extenso
```
## Como usar

A entrada pode ser um número do tipo int, float, ou str(com o número no formato brasileiro), e o retorno é uma string com o número por extenso no formato de numérico(real) ou monetário.

* Entrada do tipo int:

```python
numero1 = numero_por_extenso.real(25)
# 'vinte e cinco'

numero2 = numero_por_extenso.monetario(45)  
# 'quarenta e cinco reais'
```

* Entrada do tipo float:

```python
numero3 = numero_por_extenso.real(15.86)   
# 'quinze inteiros e oitenta e seis centésimos' 

numero4 = numero_por_extenso.real(59.87)   
# 'cinquenta e nove inteiros e oitenta e sete centésimos'
```

* Entrada do tipo str:

```python
numero5 = numero_por_extenso.real("692") 
# 'seiscentos e noventa e dois'

numero6 = numero_por_extenso.monetario("2000") 
# 'dois mil reais'

numero7 = numero_por_extenso.real("9870,56")
# 'nove mil oitocentos e setenta inteiros e cinquenta e seis centésimos'

numero8 = numero_por_extenso.monetario("260,99") 
# 'duzentos e sessenta reais e noventa e nove centavos'
```
OBS.: No caso de uma string, entrada deve posuir apenas o separador da parte inteira com a decimal, que é pode ser a virgula(,) ou o ponto(.)
