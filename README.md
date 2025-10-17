# About

A very bare bones hands on project to implement RAG Python, Fastapi, Langchain, React and the CI&T Flow API.

I was worried that would not be able to finish it on time so I ended up skipping automated testing.

## Backend

The backend was developed using Python managed by uv with Fastapi and Langchain.

```BASH
uv sync
uv run fastapi dev
```

## Frontend

Since Create React App has been deprecated, I used Astro JS with the native React integration + Tailwind.

Also, the frontend is very rough looking at the moment.

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
