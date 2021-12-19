from django.http import HttpResponse
from ninja import NinjaAPI
from .my_profiler import profile
import logging

logger = logging.getLogger("django")
logger.setLevel(logging.CRITICAL+1)

api = NinjaAPI()


@api.get("")
@profile
def index(request):
    return HttpResponse(status=200)


@api.get("user/{id}")
@profile
async def get_user(request, id: str):
    return HttpResponse(id)


@api.post("user")
@profile
async def create_user(request):
    return HttpResponse(status=200)
