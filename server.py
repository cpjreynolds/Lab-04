from flask import Flask, request

def trial_division(n):
    factors = []
    # handle 0 and 1
    if n < 2:
        return factors
    # Handle 2 separately
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # Check odd numbers up to sqrt(n)
    p = 3
    while p * p <= n:
        while n % p == 0:
            factors.append(p)
            n //= p
        p += 2
    if n > 1:
        factors.append(n)
    return factors

app = Flask(__name__)

@app.route("/")
def hello():
   return "you rang?\n"

@app.route("/echo", methods=['POST'])
def echo():
   return "You said: " + request.form['text']

@app.route("/factor", methods=["POST"])
def factor():
    inint = int(request.form["inINT"])
    return trial_division(inint)

if __name__ == "__main__":
   app.run()