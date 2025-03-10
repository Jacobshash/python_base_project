def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

mystatus=400
print(f" {mystatus} ==> {http_error(mystatus)}")

mystatus=500
print(f" {mystatus} ==> {http_error(mystatus)}")
