# Cinelasta Log: Pattern Over Stuff

**Data**: 2026-02-18
**Música**: Pattern Over Stuff
**Status**: Código Pronto (Renderização Pendente em ambiente local)

## Detalhes Técnicos
- **Framework**: Remotion
- **Componentes**:
  - `Waveform.tsx`: Visualização de áudio baseada em amplitude (mirrored path).
  - `Lyrics.tsx`: Exibição de letras sincronizada por duração total (time-based interpolation).
  - `Cover.tsx`: Capa com blur e overlay.
- **Estilo**: Minimalista, fundo preto, fonte JetBrains Mono, waveform branco.

## Desafios
- A renderização completa (4min) excede o timeout do ambiente de sandbox.
- Sincronização de letras feita por distribuição uniforme de tempo, pois não há metadados de timestamp precisos.

## Próximos Passos
- Executar `npx remotion render src/index.ts PatternOverStuff out.mp4` em uma máquina com GPU/CPU mais robusta.
