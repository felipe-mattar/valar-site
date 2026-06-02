# MAINTENANCE.md — Operação contínua do site VALAR

Checklist de rotinas para manter o site saudável após o lançamento.
Complementa o [DEPLOY.md](DEPLOY.md).

---

## Rotina mensal

| Tarefa | Como fazer | Onde |
|--------|-----------|------|
| Validar OG image no Facebook Debugger | [developers.facebook.com/tools/debug](https://developers.facebook.com/tools/debug) | og-image-v1.png |
| Validar OG image no LinkedIn Inspector | [linkedin.com/post-inspector](https://www.linkedin.com/post-inspector/) | og-image-v1.png |
| Rodar Lighthouse na home | PageSpeed Insights → URL: valar.tec.br | index.html |
| Conferir UptimeRobot | painel UptimeRobot | uptime |
| Ler Search Console | Google Search Console → valar.tec.br | SEO |
| Conferir erros JS no Sentry (se ativo) | painel Sentry | runtime |
| Verificar submissões Formspree | painel Formspree | formulário |

---

## Rotina trimestral

| Tarefa | Como fazer |
|--------|-----------|
| Auditar links quebrados | `npx linkinator https://valar.tec.br --recurse` |
| Atualizar `lastmod` no sitemap.xml | editar datas das URLs públicas |
| Revisar copy do hero | comparar com métricas reais disponíveis |
| Checar compatibilidade de browsers | [caniuse.com](https://caniuse.com) para features usadas |
| Revisar Schema.org JSON-LD | [validator.schema.org](https://validator.schema.org) |
| Testar formulário de diagnóstico ponta a ponta | envio real + verificar recebimento |

---

## Rotina semestral

| Tarefa | Como fazer |
|--------|-----------|
| Revisar Política de Privacidade | atualizar se mudou coleta de dados, terceiros ou finalidade |
| Revisar Termos de Uso | atualizar se mudou oferta de serviços |
| Incrementar versão e data nas páginas legais | editar `privacidade.html` e `termos.html` |
| Avaliar opção de self-hosting de fontes | substituir Google Fonts por /fonts/ locais |
| Avaliar Cloudflare na frente do GitHub Pages | cache headers, WAF, analytics avançado |
| Testar com NVDA (Windows) e VoiceOver iOS | navegação completa por leitor de tela |

---

## Rotina anual

| Tarefa | Como fazer |
|--------|-----------|
| Verificar renovação do domínio | [Registro.br](https://registro.br) — confirmar data e renovação automática |
| Atualizar Copyright footer | alterar `© AAAA` em todos os HTML |
| Revisar valores comerciais nas três camadas ARDA | atualizar `11_CANAIS_DIGITAIS/web_institucional/index.html` e `03_COMERCIAL` quando política mudar |
| Snapshot de configurações | registrar: DNS atual, Formspree endpoint, Plausible domínio, UptimeRobot monitors |
| Revisar OG image | verificar se a marca evoluiu — versionar nome do arquivo ao atualizar |

---

## Rotina pós-publicação de conteúdo

Sempre que publicar novo conteúdo (casos, manifesto, etc.):

1. Atualizar `lastmod` do URL correspondente no `sitemap.xml`
2. Submeter sitemap atualizado no Google Search Console
3. Validar OG tags da página no Facebook Debugger
4. Publicar no LinkedIn pessoal com link direto
5. Se for um caso novo: atualizar Schema.org Service no `index.html`

---

## Acesso a ferramentas

| Ferramenta | URL | Propósito |
|-----------|-----|-----------|
| GitHub Pages | github.com → Settings → Pages | Deploy e HTTPS |
| Formspree | formspree.io/dashboard | Formulário de diagnóstico |
| Plausible | plausible.io/valar.tec.br | Analytics |
| UptimeRobot | uptimerobot.com | Monitoramento de uptime |
| Google Search Console | search.google.com/search-console | SEO e indexação |
| Registro.br | registro.br | Domínio valar.tec.br |

---

*Documento mantido por: contato@valar.tec.br*
*Última revisão: maio 2026*
