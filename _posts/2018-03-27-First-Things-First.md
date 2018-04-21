---
layout: general
title:  "First Things First"
date:   2018-03-27 -0300
category: elicitacao
permalink: /ftf/
source: https://github.com/QueroMais/QueroMaisConversa
image: ftf.jpg
newer: {{site.baseurl}}
older: {{site.baseurl}}
description: First Things First
---

### Histórico
_____________

<table class="mdl-data-table mdl-js-data-table  mdl-shadow--2dp">
  <thead>
    <tr>
      <th class="mdl-data-table__cell--non-numeric">Data</th>
      <th class="mdl-data-table__cell--non-numeric">Descrição</th>
      <th class="mdl-data-table__cell--non-numeric">Autor</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td class="mdl-data-table__cell--non-numeric">27/03/18</td>
      <td class="mdl-data-table__cell--non-numeric">First Things First 1.0</td>
      <td class="mdl-data-table__cell--non-numeric">Lucas Pereira e Mateus Nóbrega</td>
    </tr>
    <tr>
      <td class="mdl-data-table__cell--non-numeric">01/04/18</td>
      <td class="mdl-data-table__cell--non-numeric">First Things First 2.0</td>
      <td class="mdl-data-table__cell--non-numeric">Mateus Nóbrega e Lucas Hiroshi</td>
    </tr>
  </tbody>
</table>

______________
### Introdução
______________

Após a aplicação das técnicas de elicitação, são elicitados vários requisitos, para definir por onde começar a desenvolver, com o intuito de entregar desde o começo valor agregado ao cliente, é necessário priorizar esses requisitos. 

Para realizar a priorização uma das técnicas escolhidas foi a First Things First, que consiste em priorizar os requisitos seguindo os seguintes passos:

- **Passo 1 -** Faça uma lista de todos os requisitos, características, ou casos de uso que você deseja priorizar em uma planilha. Todos os artefatos devem estar ao mesmo nível de abstração. Se funções estão logicamente ligadas (ou seja, você só iria implementar B se A for implementada), incluir apenas o recurso A na análise.

- **Passo 2 -** Estime o benefício relativo que cada recurso fornece ao cliente ou ao negócio em uma escala de 1 a 9, onde 1 é o menos significativo e 9 o máximo. Benefícios indicam alinhamento com os requisitos de negócio. Os representantes dos clientes são as melhores pessoas para definir esta escala.

- **Passo 3 -** Estimar a penalidade que o negócio sofreria se o recurso não for incluído. Mais uma vez, usar uma escala de 1 a 9, onde 1 significa, nenhuma penalidade e 9 indica uma grande desvantagem. Por exemplo, deixar de cumprir uma regulamentação do governo pode ser uma grande penalidade, mesmo que o benefício para o cliente seja baixo.

- **Passo 4 -** A coluna Valor Total é a soma do (Benefício Relativo * Peso Relativo) e da (Penalidade Relativa * Peso Relativo). Por padrão, benefício e pena devem ser ponderados de forma igual. Como refinamento, você pode alterar os pesos para esses dois fatores.

- **Passo 5 -** Estime o custo relativo de implementação de cada característica, em uma escala que varia de um mínimo de 1 a um máximo de 9. Os desenvolvedores devem classificar os custos com base em fatores como a complexidade de implementação, a interface de usuário necessária, a capacidade potencial de reutilização de telas ou código, e os níveis de testes e documentação necessários.

- **Passo 6 -** Os desenvolvedores estimam o grau relativo de risco técnico ou outro associado a cada requisito em uma escala de 1 a 9. Uma estimativa de 1 significa que eles podem ´programar dormindo´, enquanto que 9 indica sérias preocupações sobre a viabilidade, a disponibilidade de pessoal com o conhecimento necessário, ou o uso de ferramentas e tecnologias desconhecidas. Por padrão, o custo e o risco são ponderados igualmente, e cada um tem o mesmo peso que os definidos para benefícios e penalidades. Como refinamento, você pode alterar os pesos para esses dois fatores.

- **Passo 7 -** Calcular um número de prioridade para cada requisito. A fórmula para a coluna Prioridade é: Prioridade = valor % / (custo % * Peso custo + riscos % * Peso Risco).

- **Passo 8 -** Ordenar a lista de recursos por ordem decrescente de prioridade calculada. As características no topo da lista têm o melhor o equilíbrio entre valor, custo e risco, e, portanto, deve ter uma prioridade mais elevada execução. Os principais representantes dos clientes e desenvolvedores devem rever a planilha completa e concordar com os ratings e a sequência resultante.

___________
### Versões
___________

**First Things First 1.0 -** Nossa <a href="{{site.baseurl}}/ftf/1">primeira versão</a> do First Things First foi feita priorizando os requisitos da aplicação Telegram de forma geral.


**First Things First 2.0 -** Nossa <a href="{{site.baseurl}}/ftf/2">segunda versão</a> do First Things First foi feita priorizando os requisitos de cada módulo definido no nosso <a href="{{site.baseurl}}/moscow/2">MoSCoW 2.0</a>.

### Referências
-----

[1] SIMONE DINIZ JUNQUEIRO BARBOSA, BRUNO SANTANA DA SILVA, Interação Humano-Computador, 1a Edição, Editora Campus, 2010.
