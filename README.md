# juniormarorganista.github.io

Página pessoal de Juniormar Organista, servida pelo GitHub Pages em
<https://juniormarorganista.github.io/> (português) e
<https://juniormarorganista.github.io/en/> (inglês).

HTML e CSS escritos à mão, sem framework, sem script e sem nada carregado de fora: a
página inteira são dois arquivos HTML, uma folha de estilo e um ícone.

| Arquivo | O que é |
|---|---|
| `index.html` | versão em português |
| `en/index.html` | versão em inglês, com o mesmo conteúdo |
| `estilo.css` | estilo das duas, com tema claro e escuro conforme o sistema |
| `favicon.svg` | ícone da aba |
| `.nojekyll` | serve os arquivos como estão, sem passar pelo Jekyll |

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
