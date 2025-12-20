from django.shortcuts import render
import requests
# Create your views here.


def index(request):
    result = None
    image_url=None

    if request.method == "POST" and request.FILES.get("image"):
        image = request.FILES["image"]

        # sending image to ML FastAPI backend
        response = requests.post(
            "http://127.0.0.1:8000/moderate-image",
            files={"file": image}
        )

        if response.status_code == 200:
            result = response.json()
            image_url = result.get("output_image_path")
        else:
            result = {"error": "ML API failed"}

    return render(request, "ui/index.html", {
        "result": result,
        "image_url": image_url
    })
