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
| `img/retrato.webp` | foto do perfil |
| `img/og.png` | imagem de 1200 x 630 que redes sociais mostram ao compartilhar o link |
| `favicon.svg` | ícone da aba |
| `.nojekyll` | serve os arquivos como estão, sem passar pelo Jekyll |

As figuras de escoamento saem da solução manufaturada do caso 12 do
[código da tese](https://github.com/juniormarorganista/PhD-Thesis-Organista-J-USP)
(`evaluate_case_12_exact`). O gráfico de convergência usa a tabela de erro da vorticidade
do artigo (Oldroyd-B, Wi = 1, β = 0,5), publicado sob CC BY 4.0.

## Como atualizar

1. Mude o texto nas **duas** versões, `index.html` e `en/index.html`.
2. Abra `index.html` no navegador e confira, também numa janela estreita.
3. Atualize a data do rodapé nas duas.
4. Commit e push na `main`: o GitHub Pages publica em um ou dois minutos.

Para ver localmente com os links relativos funcionando como no ar:

```powershell
py -m http.server 8000
```

e abra <http://localhost:8000/>.
