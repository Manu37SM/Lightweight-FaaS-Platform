Lightweight FaaS Execution Runtime (Minimal)
Run: `python runtime_host.py` (optionally set USER_FUNC_PATH or FUNC_NAME env vars)
POST JSON to localhost:8080 and it will call handle(request) from user_function.py

Example CURL 
curl -X POST http://127.0.0.1:8080 -H "Content-Type: application/json" -d "{\"message\":\"arya\"}"
