# InfinityAI Vercel loader

This small Vercel project shows a branded loading screen while the InfinityAI
Render service wakes up. It redirects to the Streamlit application as soon as
the Render health endpoint reports that the service is ready.

## Vercel project settings

- Framework Preset: `Other`
- Root Directory: `vercel-loader`
- Build Command: leave blank
- Output Directory: leave blank

No environment variables are required for this loader.
