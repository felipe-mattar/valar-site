# DEPLOY.md — VALAR Site

Referência operacional para deploy, DNS, HTTPS e manutenção do site valar.tec.br.

---

## Estrutura do repositório

```
site/
├── index.html            — home
├── manifesto.html
├── casos.html
├── diagnostico.html
├── obrigado.html         — noindex · pós-formulário
├── 404.html              — noindex · erro
├── privacidade.html
├── termos.html
├── styles.css            — CSS compartilhado
├── main.js               — JS compartilhado
├── favicon.svg           — ícone principal
├── og-image-v1.png       — OG 1200×630 (versionar por nome, nunca por querystring)
├── CNAME                 — valar.tec.br
└── .nojekyll             — desabilita Jekyll no GitHub Pages
```

---

## Deploy no GitHub Pages

1. Repositório público: `valar-site` (branch `main`)
2. Settings → Pages → Source: `Deploy from a branch` → `main` → `/` (root)
3. Custom domain: `valar.tec.br`
4. GitHub gera certificado Let's Encrypt automaticamente após DNS configurado

---

## HTTPS forçado

Após o certificado Let's Encrypt estar emitido (aguardar ~10 min após DNS propagado):

```bash
gh api -X PUT repos/<owner>/valar-site/pages \
  -f https_enforced=true
```

Verificar via: `gh api repos/<owner>/valar-site/pages | jq .https_enforced`

---

## DNS — Registro.br

### Registros A (IPv4 do GitHub Pages)

```
Tipo    Nome    Valor
A       @       185.199.108.153
A       @       185.199.109.153
A       @       185.199.110.153
A       @       185.199.111.153
```

### Registro CNAME (www → apex)

```
CNAME   www     valar.tec.br
```

### Verificação de DNS

```bash
dig valar.tec.br +noall +answer
nslookup valar.tec.br
```

---

## Monitoramento de domínio e DNS

### Renovação do domínio

| Item                      | Detalhe                                      |
|---------------------------|----------------------------------------------|
| Domínio                   | valar.tec.br                                 |
| Registrar                 | Registro.br                                  |
| E-mail de lembretes       | verificar que o e-mail cadastrado no Registro.br está ativo |
| Renovação automática      | ativar no painel do Registro.br              |
| Próxima verificação manual| anotar data de expiração no calendário com 90 dias de antecedência |

**Risco crítico:** perda do domínio derruba o site e o e-mail contato@valar.tec.br imediatamente.

### Como verificar data de expiração

```bash
whois valar.tec.br | grep -i expir
```

---

## Email — decisão de exposição

**Decisão adotada (maio 2026):** manter `contato@valar.tec.br` em texto puro no HTML.

**Justificativa:** público-alvo B2B com menor exposição a bots de formulário.
Mitigação via filtros do provedor de e-mail (Google Workspace ou similar).

**Reavaliação:** se volume de spam superar 10 mensagens/dia não filtradas, avaliar:
- Substituição por formulário Formspree (já planejado no Sprint 3)
- Ofuscação JS: `data-email` renderizado via script

---

## Variáveis de ambiente / segredos

Não há variáveis de ambiente nem segredos no site estático.
Quando o formulário Formspree for ativado, o endpoint público do Formspree
(ex.: `https://formspree.io/f/xxxxxxxk`) vai diretamente no HTML — é público por design.

---

## Rollback

Qualquer versão anterior está acessível no histórico do Git:

```bash
git log --oneline
git checkout <hash> -- site/index.html
git commit -m "rollback index.html para <hash>"
git push
```

---

## Configuração pós-deploy (primeira vez)

### Analytics — Plausible

O script já está em todos os HTML. Para ativar:
1. Criar conta em plausible.io
2. Adicionar domínio `valar.tec.br`
3. O tracker já está no `<body>` de todas as páginas — não requer configuração adicional no código

### Google Search Console

1. Acessar [search.google.com/search-console](https://search.google.com/search-console)
2. Adicionar propriedade `https://valar.tec.br`
3. Verificar via arquivo HTML (adicionar à pasta site/) ou DNS TXT record
4. Submeter sitemap: `https://valar.tec.br/sitemap.xml`

### Formspree

1. Criar conta em [formspree.io](https://formspree.io)
2. Criar novo form → copiar o ID (ex.: `xxxxxxxk`)
3. Em `diagnostico.html`, substituir `YOUR_FORM_ID` pelo ID real
4. Testar envio completo do formulário
5. Confirmar que `/obrigado.html` é carregada após envio

### UptimeRobot

1. Criar conta em [uptimerobot.com](https://uptimerobot.com)
2. Adicionar monitor HTTP para `https://valar.tec.br`
3. Intervalo: 5 minutos
4. Alertas: e-mail para `contato@valar.tec.br`

---

## Checklist pré-lançamento

- [ ] HTTPS ativo e `https_enforced=true` confirmado
- [ ] `og:image-v1.png` disponível e validada no Facebook Sharing Debugger
- [ ] `robots.txt` e `sitemap.xml` criados e acessíveis
- [ ] Formulário Formspree testado com envio real
- [ ] `/obrigado.html` confirmada com `noindex`
- [ ] `/404.html` servida pelo GitHub Pages para URLs inexistentes
- [ ] Lighthouse ≥ 95 performance, ≥ 95 accessibility, ≥ 90 SEO
- [ ] Nenhum link `href="#"` ativo no nav ou footer (exceto LinkedIn pendente)
- [ ] DNS propagado (checar em dnschecker.org)
- [ ] Domínio com renovação automática ativa no Registro.br
