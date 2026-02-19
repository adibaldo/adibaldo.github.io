# Segurança de Dependências

## Estratégia

Os `package-lock.json` **não são versionados** no git para evitar poluição do histórico e permitir updates recorrentes locais.

## Manutenção Local

Rode periodicamente em cada subprojeto:

```bash
cd workspace/adibaldo.github.io && npm audit fix
cd workspace/franklinbaldo.github.io && npm audit fix
cd workspace/omunicipio.github.io && npm audit fix
cd workspace/ecos-do-pampa && npm audit fix
```

Ou em caso de vulnerabilidades que exigem breaking changes:

```bash
npm audit fix --force
```

## Notas

- GitHub Dependabot continua monitorando e alertando sobre vulnerabilidades
- Cada ambiente (dev, CI, produção) pegará as versões mais recentes ao rodar `npm install`
- Se uma vulnerabilidade específica precisa ser ignorada, documentar aqui o motivo
