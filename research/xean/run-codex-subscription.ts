// Run with the separately installed Bun runtime. Credentials never enter settings.
import { readFile } from "node:fs/promises";
import { homedir } from "node:os";
import { join, resolve } from "node:path";

async function main(): Promise<number> {
  const args = process.argv.slice(2);
  const codexDirectory = process.env.CODEX_HOME || join(homedir(), ".codex");
  let auth: { auth_mode?: string; tokens?: { access_token?: string } };
  try {
    auth = JSON.parse(await readFile(join(codexDirectory, "auth.json"), "utf8"));
  } catch {
    console.error("Codex subscription credentials are unavailable. Sign in with codex login and make the updated login available in this environment.");
    return 78;
  }
  const token = auth.tokens?.access_token;
  if (auth.auth_mode !== "chatgpt" || typeof token !== "string") {
    console.error("A ChatGPT subscription login is required. Run codex login; an API key is not used by this launcher.");
    return 78;
  }
  let claims: { exp?: number; [key: string]: unknown };
  try {
    const parts = token.split(".");
    if (parts.length !== 3) throw new Error("Invalid credential format");
    claims = JSON.parse(Buffer.from(parts[1]!, "base64url").toString("utf8"));
    const account = claims["https://api.openai.com/auth"] as { chatgpt_account_id?: unknown } | undefined;
    if (typeof account?.chatgpt_account_id !== "string" || !account.chatgpt_account_id) throw new Error("Missing subscription account");
  } catch {
    console.error("The mounted subscription access token cannot be used by Xean's native Codex provider. Restore a valid codex login; no model call was made.");
    return 78;
  }
  if (typeof claims.exp !== "number" || !Number.isFinite(claims.exp) || claims.exp * 1000 <= Date.now()) {
    console.error("The subscription access token has expired. Refresh the native Codex login before running Xean; no model call was made.");
    return 78;
  }
  if (args.length === 1 && args[0] === "--check-auth") {
    console.log(JSON.stringify({ provider: "openai-codex", credentialFormatValid: true, tokenUnexpired: true, liveModelCallVerified: false }));
    return 0;
  }
  if (!args.length) {
    console.error("Pass Xean CLI arguments, or --check-auth. Use settings.codex-subscription.json when initializing a campaign.");
    return 64;
  }
  const checkout = resolve(process.env.XEAN_CHECKOUT_DIR || "/workspace/xean");
  const child = Bun.spawn([process.execPath, join(checkout, "packages/cli/src/index.ts"), ...args], {
    cwd: process.cwd(),
    env: { ...process.env, XEAN_CODEX_SUBSCRIPTION_TOKEN: token },
    stdin: "inherit",
    stdout: "inherit",
    stderr: "inherit",
  });
  return await child.exited;
}

try {
  process.exitCode = await main();
} catch {
  console.error("The subscription launcher failed before completion. No credentials are included in this diagnostic.");
  process.exitCode = 1;
}
