# Certificados
- Certificado de conclução da sprint 3
![Data & Analytics - PB - AWS sprint3](<CERTIFICADOS/Data & Analytics - PB - AWS sprint3.jpg>)


A partir da versão 3.10 do Python foi introduzida na linguagem uma nova estrutura de controle que tem o comportamento da estrutura switch: a estrutura match case

A sintaxe básica dessa estrutura é a seguinte:

```python
match valor:

    case <padrao_1>:
        <codigo_caso_padrao_1>
	  case <padrao_2>:
        <codigo_caso_padrao_2>
		case <padrao_3>:
        <codigo_caso_padrao_3>
    case _:
        <codigo_caso_nenhum_padrao_definido>
```
Essa estrutura irá comparar um valor com vários valores diferentes (a documentação trás o termo padrão) e executará o código correspondente ao valor da variável que está sendo usada na comparação. Para facilitar o entendimento, deixamos abaixo os exemplos das duas últimas aulas refeitos com a estrutura match case

Simulando SWITCH #01

```python
def get_dia_semana(dia):
    match dia:
        case 1:
            return 'Domingo'
        case 2:
            return 'Segunda'
        case 3:
            return 'Terça'
        case 4:
            return 'Quarta'
        case 5:
            return 'Quinta'
        case 6:
            return 'Sexta'
        case 7:
            return 'Sabado'
        case _:
            return '** inválido **'

            
    
 
if __name__ == '__main__':
    for dia in range(0, 9):
        print(f'{dia}: {get_dia_semana(dia)}')
```

Simulando SWITCH #02

```python
def get_tipo_dia(dia):
    match dia:
        case 2 | 3 | 4 | 5 | 6 :
            return 'Dia de semana'
        case 1 | 7:
            return 'Fim de semana'
        case _:
            return '** inválido **'
            
 
 
if __name__ == '__main__':
    for dia in range(0, 9):
        print(f'{dia}: {get_tipo_dia(dia)}')
```