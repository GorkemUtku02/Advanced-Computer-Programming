from fastapi import FastAPI

app = FastAPI()

def fibonacci(n: int):
    sequence=[0,1]
    while len(sequence)<n:
        sequence.append(sequence[-1]+sequence[-2])
    return sequence[:n]

@app.get("/fibonacci/{n}")
async def generate_fibonacci(n: int):
    if n <= 0:
        return {'error': 'Count must be a positive integer.'}
    return {'fibonacci': fibonacci(n)}