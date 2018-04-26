from django.shortcuts import render,HttpResponse
import hashlib

token = "RICHRICH"
# Create your views here.
def verify(request):
    data = request.GET
    echostr = data.get("echostr")
    signature = data.get('signature')
    timestamp = data.get('timestamp')
    nonce = data.get('nonce')

    temp = [token,timestamp,nonce]
    temp.sort()

    temp = "".join(temp)
    sig = hashlib.sha1(temp).hexdigest()

    if sig == signature:
        return HttpResponse(echostr)
    else:
        return HttpResponse('error', 403)




