#!/usr/bin/env python3
"""
sync_manifesto.py

Converte MANIFESTO.md para o bloco de conteúdo em manifesto.html.
Mantém nav, head e footer intactos — só atualiza a seção #manifesto-content.

Uso:
    python scripts/sync_manifesto.py [--manifesto-path PATH] [--html-path PATH]

Padrão (a partir da raiz do repo site/):
    manifesto-path: ../10_ESTRATEGIA/MANIFESTO.md  (ou MANIFESTO.md se existir localmente)
    html-path:      manifesto.html
"""

import argparse
import re
import sys
from pathlib import Path

try:
    import markdown
except ImportError:
    print("Erro: instale a dependência com: pip install markdown")
    sys.exit(1)

NAV_FOOTER_NOTICE = (
    "<!-- ATENÇÃO: este bloco é gerado automaticamente por scripts/sync_manifesto.py "
    "a partir de MANIFESTO.md. Não edite manualmente. -->"
)

SECTION_START = '<section id="manifesto-content">'
SECTION_END = "    </section>"


def md_to_prose_html(md_text: str) -> str:
    """Converte Markdown para HTML usando a classe .prose."""
    # Remove frontmatter YAML
    md_text = re.sub(r"^---.*?---\n", "", md_text, flags=re.DOTALL)

    # Remove linha de título H1 (já está no page-hero)
    md_text = re.sub(r"^# .*\n", "", md_text, count=1)

    # Remove linhas de texto-fonte (nota interna do MANIFESTO.md)
    md_text = re.sub(r"^Texto-fonte.*\n\n?", "", md_text)

    html = markdown.markdown(
        md_text,
        extensions=["extra"],
        output_format="html5",
    )

    # Adicionar classes prose e ajustar meta
    meta_line = '<p class="prose-meta">escrito em abril de 2026 · versão 1.0</p>'

    return meta_line + "\n" + html


def update_manifesto_html(html_path: Path, md_path: Path) -> None:
    if not md_path.exists():
        print(f"Erro: arquivo não encontrado: {md_path}")
        sys.exit(1)

    if not html_path.exists():
        print(f"Erro: arquivo não encontrado: {html_path}")
        sys.exit(1)

    md_text = md_path.read_text(encoding="utf-8")
    html_content = html_path.read_text(encoding="utf-8")

    prose_html = md_to_prose_html(md_text)

    new_section = (
        f'{SECTION_START}\n'
        f'      {NAV_FOOTER_NOTICE}\n'
        f'      <div class="container">\n'
        f'        <div class="prose">\n'
        f'{prose_html}\n'
        f'          <div class="prose-cta">\n'
        f'            <a href="diagnostico.html" class="btn-primary">Solicitar diagnóstico →</a>\n'
        f'            <a href="casos.html" class="btn-secondary" style="margin-left: 16px;">Ver casos</a>\n'
        f'          </div>\n'
        f'        </div>\n'
        f'      </div>\n'
        f'    {SECTION_END}'
    )

    # Substituir bloco entre SECTION_START e próximo SECTION_END
    pattern = re.compile(
        re.escape(SECTION_START) + r".*?" + re.escape(SECTION_END),
        re.DOTALL,
    )

    if not pattern.search(html_content):
        print(f"Erro: marcador '{SECTION_START}' não encontrado em {html_path}")
        sys.exit(1)

    updated = pattern.sub(new_section, html_content)
    html_path.write_text(updated, encoding="utf-8")
    print(f"Atualizado: {html_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Sincroniza MANIFESTO.md com manifesto.html")
    parser.add_argument(
        "--manifesto-path",
        type=Path,
        default=Path(__file__).parent.parent / "MANIFESTO.md",
        help="Caminho para MANIFESTO.md (default: site/MANIFESTO.md)",
    )
    parser.add_argument(
        "--html-path",
        type=Path,
        default=Path(__file__).parent.parent / "manifesto.html",
        help="Caminho para manifesto.html",
    )
    args = parser.parse_args()

    print(f"Origem: {args.manifesto_path}")
    print(f"Destino: {args.html_path}")
    update_manifesto_html(args.html_path, args.manifesto_path)


if __name__ == "__main__":
    main()
