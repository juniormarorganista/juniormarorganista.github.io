"""Monta a seção "Portfólio" das duas páginas a partir de dados/portfolio.toml.

    py ferramentas/portfolio.py              reescreve a seção em index.html e en/index.html
    py ferramentas/portfolio.py --conferir   só confere; sai com 1 se alguma página estiver
                                             desatualizada em relação aos dados

Usa só a biblioteca padrão (Python 3.11 ou mais novo, por causa do tomllib).
A seção fica entre os marcadores <!-- portfolio:inicio --> e <!-- portfolio:fim -->;
nada fora deles é tocado.
"""

from __future__ import annotations

import argparse
import re
import sys
import tomllib
from html import escape
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DADOS = RAIZ / "dados" / "portfolio.toml"
INICIO, FIM = "<!-- portfolio:inicio -->", "<!-- portfolio:fim -->"
PERFIL_ATIVIDADE = "https://www.linkedin.com/in/juniormar-organista-1762802a/recent-activity/all/"
CAMPOS = ("data", "projeto", "titulo_pt", "titulo_en", "resumo_pt", "resumo_en",
          "imagem", "alt_pt", "alt_en", "link")
MESES = {
    "pt": ("janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho",
           "agosto", "setembro", "outubro", "novembro", "dezembro"),
    "en": ("January", "February", "March", "April", "May", "June", "July",
           "August", "September", "October", "November", "December"),
}
PAGINAS = {
    "pt": (RAIZ / "index.html", "", "Ver no LinkedIn"),
    "en": (RAIZ / "en" / "index.html", "../", "View on LinkedIn"),
}
DATA = re.compile(r"^(\d{4})-(0[1-9]|1[0-2])$")
RECUO = " " * 8


class ErroDeDados(ValueError):
    """Problema em dados/portfolio.toml, com mensagem voltada a quem edita."""


def carregar() -> list[dict]:
    postagens = tomllib.loads(DADOS.read_text(encoding="utf-8")).get("postagem", [])
    if not postagens:
        raise ErroDeDados(f"{DADOS.name}: nenhuma [[postagem]] encontrada")
    for n, post in enumerate(postagens, 1):
        faltando = [c for c in CAMPOS if c not in post]
        if faltando:
            raise ErroDeDados(f"postagem {n}: faltam os campos {', '.join(faltando)}")
        if not DATA.match(post["data"]):
            raise ErroDeDados(f"postagem {n}: data {post['data']!r} não está como AAAA-MM")
        if not (RAIZ / post["imagem"]).is_file():
            raise ErroDeDados(f"postagem {n}: imagem {post['imagem']} não existe no site")
    return postagens


def quando(data: str, lingua: str) -> str:
    ano, mes = DATA.match(data).groups()
    nome = MESES[lingua][int(mes) - 1]
    return f"{nome} de {ano}" if lingua == "pt" else f"{nome} {ano}"


def montar(postagens: list[dict], lingua: str) -> str:
    _, prefixo, rotulo_link = PAGINAS[lingua]
    linhas = [f'{RECUO}<ol class="portfolio">']
    for post in postagens:
        link = post["link"] or PERFIL_ATIVIDADE
        linhas += [
            f"{RECUO}  <li>",
            f'{RECUO}    <img src="{escape(prefixo + post["imagem"])}" width="320" height="180" '
            f'loading="lazy" alt="{escape(post["alt_" + lingua])}">',
            f"{RECUO}    <div>",
            f'{RECUO}      <p class="quando"><time datetime="{post["data"]}">'
            f'{quando(post["data"], lingua)}</time> · {escape(post["projeto"])}</p>',
            f'{RECUO}      <h3>{escape(post["titulo_" + lingua])}</h3>',
            f'{RECUO}      <p>{escape(post["resumo_" + lingua])}</p>',
            f'{RECUO}      <a class="ver" href="{escape(link)}">{rotulo_link}</a>',
            f"{RECUO}    </div>",
            f"{RECUO}  </li>",
        ]
    linhas.append(f"{RECUO}</ol>")
    return "\n".join(linhas)


def aplicar(texto: str, secao: str, pagina: Path) -> str:
    padrao = re.compile(re.escape(INICIO) + r".*?" + re.escape(FIM), re.S)
    if len(padrao.findall(texto)) != 1:
        raise ErroDeDados(f"{pagina.relative_to(RAIZ)}: os marcadores {INICIO} e {FIM} "
                          "precisam aparecer uma vez cada")
    return padrao.sub(lambda _: f"{INICIO}\n{secao}\n{RECUO}{FIM}", texto)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--conferir", action="store_true",
                    help="não grava; sai com 1 se alguma página estiver desatualizada")
    args = ap.parse_args()

    try:
        postagens = carregar()
        desatualizadas = []
        for lingua, (pagina, _, _) in PAGINAS.items():
            atual = pagina.read_text(encoding="utf-8")
            novo = aplicar(atual, montar(postagens, lingua), pagina)
            if novo != atual:
                desatualizadas.append(pagina.relative_to(RAIZ).as_posix())
                if not args.conferir:
                    pagina.write_text(novo, encoding="utf-8", newline="\n")
    except ErroDeDados as erro:
        print(f"erro: {erro}", file=sys.stderr)
        return 2

    if args.conferir:
        if desatualizadas:
            print("desatualizadas: " + ", ".join(desatualizadas))
            return 1
        print(f"ok: {len(postagens)} postagens, as duas páginas em dia")
        return 0
    feitas = ", ".join(desatualizadas) or "nenhuma (já estavam em dia)"
    print(f"{len(postagens)} postagens; páginas reescritas: {feitas}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
