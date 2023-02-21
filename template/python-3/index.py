from fastapi import FastAPI, Request, Response
from function.handler import handler
import os

app = FastAPI()


@app.get("/")
@app.get("/{path:path}")
@app.post("/")
@app.post("/{path:path}")
@app.put("/")
@app.put("/{path:path}")
@app.patch("/")
@app.patch("/{path:path}")
@app.delete("/")
@app.delete("/{path:path}")
def get_or_create_task(request: Request, response: Response):
    return handler(request, response)


port = int(os.environ.get("PORT", 3000))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("index:app", host="0.0.0.0", port=port, log_level="info")
