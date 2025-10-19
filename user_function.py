
def handle(request):
    # simple echo handler that uppercases 'message' field
    msg = request.get('message', 'hello')
    return {'echo': str(msg).upper()}
