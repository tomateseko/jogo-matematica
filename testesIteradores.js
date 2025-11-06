// Cria um array com nomes fictícios
const clientes = ["Amanda Lopes", "Bruno Castro", "Carla Nunes", "Diego Martins", "Elisa Rocha"];

// Usa o loop for...of para percorrer o array
for (const nome of clientes) {
  console.log(`Enviando e-mail de agradecimento para ${nome}.`);
}

// Lista de objetos com nome do cliente e data da compra
const compras = [
  { nome: "Ana Souza", dataCompra: "2025-10-20" },
  { nome: "Bruno Lima", dataCompra: "2025-09-25" },
  { nome: "Carla Mendes", dataCompra: "2025-11-01" },
  { nome: "Diego Alves", dataCompra: "2025-10-10" },
  { nome: "Eduarda Pinto", dataCompra: "2025-10-29" },
  { nome: "Felipe Rocha", dataCompra: "2025-09-30" },
  { nome: "Gabriela Torres", dataCompra: "2025-10-31" },
  { nome: "Henrique Costa", dataCompra: "2025-10-02" },
  { nome: "Isabela Moura", dataCompra: "2025-11-03" },
  { nome: "João Pedro", dataCompra: "2025-10-18" }
];

// Obtém a data atual
const hoje = new Date();

// Percorre a lista usando forEach
compras.forEach((compra) => {
  const dataCompra = new Date(compra.dataCompra);
  const diferencaDias = Math.floor((hoje - dataCompra) / (1000 * 60 * 60 * 24)); // diferença em dias

  if (diferencaDias <= 30) {
    console.log(`Cliente: ${compra.nome} — comprou há ${diferencaDias} dias.`);
  }
});

// Lista com nomes repetidos
const nomes = [
  "Lucas", "Marina", "João", "Lucas", 
  "Ana", "Pedro", "Marina", "Carla", "Ana", "Felipe"
];

// Cria um Set para remover duplicatas automaticamente
const nomesUnicos = new Set(nomes);

// Cria um iterador a partir do Set
const iterador = nomesUnicos.values();

// Exibe os nomes únicos no console
console.log("Nomes únicos encontrados:");
for (const nome of iterador) {
  console.log(nome);
}
