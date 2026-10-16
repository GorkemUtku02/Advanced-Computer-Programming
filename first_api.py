from fastapi import FastAPI, HTTPException

app=FastAPI()

@app.get("/hello")
def hello_world():
    return {"message": "Hello, World!"}

@app.get("/square/{number}")
def square_number(number:float):
    return {"number": number, "square": number**2}

@app.get("/length/{text}")
def string_length(text:str):
    return{"text":text,"length":len(text)}

@app.get("/sum")
def two_sum(a:float,b:float):
    return{"a": a,"b": b,"sum": a + b}

@app.get("/prime/{number}")
def prime_number(number:int):
    if number < 0:
        raise HTTPException(status_code=400, detail="Prime number can not be negaitve number")
    if number < 2:
        is_prime = False
    else:
        is_prime = True
        i = 2
        while i*i <= number:
            if number % i == 0:
                is_prime = False
                break
            i += 1
    return{"number": number, "is_prime": is_prime}