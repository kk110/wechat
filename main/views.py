from django.shortcuts import render,HttpResponse
import hashlib

token = "RICHRICH"
# Create your views here.
def verify(request):
    echostr = request.GET.get("echostr")
    signature = request.GET.get('signature')
    timestamp = request.GET.get('timestamp')
    nonce = request.GET.get('nonce')

    print('echostr',echostr)
    print('signature', signature)
    print('timestamp', timestamp)
    print('nonce', nonce)

    temp = [token,timestamp,nonce]
    temp.sort()

    temp = "".join(temp)
    print('------',temp)
    temp = temp.encode()

    sig = hashlib.sha1(temp).hexdigest()

    if sig == signature:
        return HttpResponse(echostr)
    else:
        return HttpResponse('error')




