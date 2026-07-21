const APP_HEALTH_URL =
  "https://infinityai-app.onrender.com/_stcore/health";

export default async function handler(request, response) {
  response.setHeader("Cache-Control", "no-store, max-age=0");

  try {
    const upstream = await fetch(APP_HEALTH_URL, {
      cache: "no-store",
      signal: AbortSignal.timeout(8000),
    });
    const body = await upstream.text();
    const ready = upstream.ok && body.trim().toLowerCase() === "ok";

    return response.status(ready ? 200 : 503).json({ ready });
  } catch (error) {
    return response.status(503).json({ ready: false });
  }
}
