# About

A very bare bones hands on project to implement RAG using Python, Fastapi, Langchain, React and the CI&T Flow API.

I was worried that I would not be able to finish it on time so I ended up skipping automated testing for now.

## Backend

The backend was developed using Python managed by [uv](https://docs.astral.sh/uv/) with Fastapi and Langchain.

Make sure [uv is installed](https://docs.astral.sh/uv/getting-started/installation/), then run:

```BASH
uv sync
uv run fastapi dev
```

## Frontend

Since Create React App has been deprecated, I used Astro JS with the native React integration + Tailwind.

But I barely added any CSS so the frontend is looking very rough at the moment.

```BASH
npm install
npm run dev
```

## Todos/Improvements

- api
  - add an uvicorn entrypoint for production environment
  - add automated tests
  - add caching the Flow token
  - Replace requests with httpx
  - Use more async methods
  - troubleshoot installing torch on a Mac OS 15 with Intel CPU
-frontend
  - add automated tests
  - scroll the messages automatically
  - improve the UI
