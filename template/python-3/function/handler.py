from fastapi import Request, Response, status

def handler(request: Request, response: Response) -> str:
    print(f"Method: {request.method}")
    response.status_code = status.HTTP_200_OK
    return "My first function !"
