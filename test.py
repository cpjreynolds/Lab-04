import httpx

url = "http://127.0.0.1:5000/"

mydata = {
    "inINT": 42
}

def test_factoring():
    data = [
            (7, [7]),
            (12, [2, 2, 3]),
            (42, [2,3,7]),
            (24, [2, 2, 2, 3]),
            (360, [2,2,2,3,3,5]),
            (31, [31]),
            ]

    for inp, expect in data:
        response = httpx.post(url+"factor", data={"inINT": inp})
        resplist = eval(response.text)
        print(f"inINT: {inp} => expect: {expect}, recv: {resplist}")
        # I know I'm executing an http response and that's A Very Bad Idea (tm)
        assert(resplist == expect)

test_factoring()