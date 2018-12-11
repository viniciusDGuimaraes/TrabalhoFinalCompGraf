# Projeto final de Computação Gráfica
----
## Instruções
* Quando você rodar o programa ele irá te pedir as seguintes entradas: um axioma, as regras, a quantidade de vezes que elas devem ser aplicadas e o valor do ângulo
* O axioma
  * O valor que inicia o programa, e o primeiro onde será aplicado uma das regras
* As regras
  * As regras devem seguir o seguinte formato: _valor que sofrerá a aplicação da regra_->_resultado da regra_
  * Exemplo: F->LF
  * É necessário que exista o simbolo ->
  * O valor do lado esquerdo da regra deve ser somente UM carácter
  * Múltiplas regras devem ser separadas por vírgula(,)
  * Os caracteres '[' e ']' são usados, respectivamente, para salvar um ponto no desenho e para voltar para esse ponto, então é necessário que exista a mesma quantidade de ambos os caracteres nas regras
* Comandos
  * F e G: Desenham uma linha
  * L: Vira para esquerda
  * R: Vira para direita
  * U: Vira para mais próximo da tela
  * D: Vira para mais distante da tela
  * [: Salva o último ponto e o ângulo em que uma linha foi desenhada
  * ]: Volta para o último ponto salvo
## Exemplos
### Árvore 2D

Axioma: F
Regras: F->F[LF][RF]
Repetições: 5
Ângulo: 25

### Árvore 3D
Axioma: F
Regras: F->F[LF][RF],L->U,R->D,U->L,D->R
Repetições: 5
Ângulo: 25

### Barnsley fern
Axioma: X
Regras: X->FR[[X]LX]LF[LFX]RX,F->FF
Repetições: 4
Ângulo: 25

### Triângulo de Sierpinski
Axioma: FRGRG
Regras: F->FRGLFLGRF,G->GG
Repetições: 4
Ângulo: 120

Ou

axioma: F
Regras: F->GRFRG,G->FLGLF
Repetições: 4
Ângulo: 60

### Curva de Koch
axioma: F
Regras: F->FLFRFRFLF
Repetições: 3
Ângulo: 90

