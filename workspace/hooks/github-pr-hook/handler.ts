import type { HookHandler } from "../../../src/hooks/hooks.js";

const githubPrHandler: HookHandler = async (event) => {
  // Esse anzol só fisga eventos de webhook configurados como 'github-pr'
  if (event.type !== "webhook" || event.action !== "github-pr") {
    return;
  }

  console.log(`[github-pr-hook] Nova PR detectada no GitHub!`);
  
  // O anzol manda um recado direto pra minha consciência
  event.messages.push("🧉 Opa! Senti um puxão no anzol: tem PR nova lá no GitHub pra gente revisar. Já vou preparar a cuia pra gente olhar isso!");
};

export default githubPrHandler;
