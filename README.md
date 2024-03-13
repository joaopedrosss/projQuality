# Projeto de Qualidade de Software

## Aplicação do Padrão de Projeto State para uma aplicação de aluguel de carros

Neste projeto aplicou-se um padrão de projeto chamado State num projeto previamente feito a fim de tornar o código orignal mais limpo e escalável 

### Classe Context: UsuarioState

É a classe original que referencia objetos da classe State.

### Classe State: State

É a classe que define a interface dos métodos das Classes Concretas. Se os objetos das classes concretas dividem a mesma interface, há melhor reuso de código.

### Classes Concretas: UsuarioSemLogin,UsuarioComum e UsuarioAdmin

Definem os diferentes estados que um objeto da classe UsuarioState (Context) podem assumir.




