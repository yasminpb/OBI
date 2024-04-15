'''Cada consoante deve ser substituída por exatamente três letras, na seguinte ordem:
a própria consoante (vamos chamar de consoante original);
a vogal mais próxima da consoante original no alfabeto, 
com a regra adicional de que se a consoante original está à mesma distância de duas vogais, 
então a vogal mais próxima do início do alfabeto é usada. 

Por exemplo, se a consoante original é d, a vogal que deve ser usada é e, pois esta é a vogal mais próxima; 
se a consoante original é c, a vogal que deve ser utilizada é a, porque c está à mesma distância de a e e, e a é mais próxima do início do alfabeto.
a consoante que segue a consoante original, na ordem do início ao fim do alfabeto.
 
Por exemplo, se a consoante original é d, a consoante a ser utilizada é f. 
No caso de a consoante original ser z, deve ser utilizada a própria letra z.
As vogais não são modificadas.
Nesta tarefa, o alfabeto é: a b c d e f g h i j k l m n o p q r s t u v x z
e as vogais são: a e i o u'''

array_de_consoantes = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "z"]
array_de_vogais = ["a", "e", "i", "o", "u"]

palavra = input("Escreva uma palavra: ")

for(int i=0; i >)