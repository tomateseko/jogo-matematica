// Desafio 1: medir o tamanho da palavra

let palavra = prompt("Digite uma palavra com mais de 8 letras:");

while (palavra.length <= 8) {
  palavra = prompt("Palavra muito curta! Digite outra com mais de 8 letras:");
}

console.log("A palavra aceita foi:", palavra);
console.log("Ela tem", palavra.length, "letras.");

// Desafio 2: acumular valores imprevisíveis

let soma = 0;

while (soma <= 500) {
  let numero = Math.floor(Math.random() * 100); // gera número aleatório de 0 a 99
  soma += numero;
  console.log("Gerado:", numero, "| Soma atual:", soma);
}

console.log("Soma final ultrapassou 500! Total:", soma);

// Desafio 3: verificar se um número está dentro de uma faixa indicada

let tamanho = parseInt(prompt("Digite o tamanho do seu calçado (entre 34 e 44):"));

while (isNaN(tamanho) || tamanho < 34 || tamanho > 44) {
  tamanho = parseInt(prompt("Valor inválido! Digite um número entre 34 e 44:"));
}

console.log("Tamanho válido:", tamanho);

// Desafio 4: testar múltiplas condições

let numero = 0;

while (numero % 3 !== 0 || numero % 5 !== 0 || numero === 0) {
  numero = Math.floor(Math.random() * 100); // gera número aleatório entre 0 e 99
  console.log("Gerado:", numero);
}

console.log("Número múltiplo de 3 e 5 encontrado:", numero);

// Desafio 6: verificar presença de caracteres

let senha = prompt("Digite uma senha que contenha pelo menos 1 letra e 1 número:");

let temLetra = /[a-zA-Z]/.test(senha);  // verifica se há letra
let temNumero = /[0-9]/.test(senha);    // verifica se há número

while (!temLetra || !temNumero) {
  senha = prompt("Senha inválida! Digite uma senha com pelo menos 1 letra e 1 número:");
  temLetra = /[a-zA-Z]/.test(senha);
  temNumero = /[0-9]/.test(senha);
}

console.log("Senha aceita:", senha);
