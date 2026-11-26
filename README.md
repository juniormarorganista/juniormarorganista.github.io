# juniormarorganista.github.io

Página pessoal de Juniormar Organista, servida pelo GitHub Pages em
<https://juniormarorganista.github.io/> (português) e
<https://juniormarorganista.github.io/en/> (inglês).

HTML e CSS escritos à mão, sem framework, sem script e sem nada carregado de fora. As
fontes são as do sistema; o gráfico é SVG embutido no HTML.

| Arquivo | O que é |
|---|---|
| `index.html` | versão em português |
| `en/index.html` | versão em inglês, com o mesmo conteúdo |
| `estilo.css` | estilo das duas, com tema claro e escuro conforme o sistema |
| `img/correntes.svg` | linhas de nível da função corrente e da vorticidade de uma solução manufaturada da tese, usadas como máscara no topo (a cor vem do CSS) |
| `img/vorticidade.webp` | vorticidade exata da mesma solução, no cartão do código da tese |
| `img/ces-janela.png` | janela do CES, copiada de `docs/` do repositório dele |
| `img/cnpj-mapa.webp`, `img/cnpj-capa.webp` | páginas 6 e 1 do carrossel do CNPJ Analytics já publicado no LinkedIn |
| `img/retrato.webp` | foto do perfil |
| `dados/portfolio.toml` | postagens publicadas no LinkedIn, que formam a seção "Portfólio" |
| `ferramentas/portfolio.py` | monta a seção "Portfólio" das duas páginas a partir do arquivo acima |
| `img/og.png` | imagem de 1200 x 630 que redes sociais mostram ao compartilhar o link |
| `favicon.svg` | ícone da aba |
| `.nojekyll` | serve os arquivos como estão, sem passar pelo Jekyll |

As figuras de escoamento saem da solução manufaturada do caso 12 do
[código da tese](https://github.com/juniormarorganista/PhD-Thesis-Organista-J-USP)
(`evaluate_case_12_exact`). O gráfico de convergência usa a tabela de erro da vorticidade
do artigo (Oldroyd-B, Wi = 1, β = 0,5), publicado sob CC BY 4.0.

## Postagem nova no LinkedIn

Toda postagem publicada no LinkedIn entra no portfólio do site:

1. Acrescente um bloco `[[postagem]]` no topo de `dados/portfolio.toml`, com data,
   projeto, título e resumo nas duas línguas, imagem e o link da postagem (o comentário
   no começo do arquivo explica cada campo). A imagem vai antes para `img/`, e só
   imagem que já saiu na postagem.
2. Rode `py ferramentas/portfolio.py`. Ele reescreve só o trecho entre
   `<!-- portfolio:inicio -->` e `<!-- portfolio:fim -->` das duas páginas.
3. `py ferramentas/portfolio.py --conferir` sai com 1 se alguma página ficou para trás.

Projeto de código privado entra descrito pelo que a postagem disse, sem link para o
repositório.

## Como atualizar

1. Mude o texto nas **duas** versões, `index.html` e `en/index.html`. O tom é o do
   resumo do Lattes: terceira pessoa, frases como "Possui formação...", "Atua em...".
2. Mudou o `estilo.css`? Aumente o número em `estilo.css?v=` nas duas páginas. O
   GitHub Pages manda o navegador guardar o CSS por 10 minutos; sem o número novo,
   quem já visitou o site recebe o HTML novo com o CSS antigo, e a página desmonta.
   Vale o mesmo para uma imagem que mude sem mudar de nome.
3. Abra `index.html` no navegador e confira em tela larga (1920 px), em notebook
   (1366 px) e numa janela estreita.
4. Atualize a data do rodapé nas duas.
5. Commit e push na `main`: o GitHub Pages publica em um ou dois minutos.

Para ver localmente com os links relativos funcionando como no ar:

```powershell
py -m http.server 8000
```

e abra <http://localhost:8000/>.
