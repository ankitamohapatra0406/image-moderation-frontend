from django.shortcuts import render
import requests
# Create your views here.


def index(request):
    result = None
    error = None

    if request.method == "POST" and request.FILES.get("image"):
        image = request.FILES["image"]

        try:
            response = requests.post(
                "http://127.0.0.1:8000/moderate-image",
                files={"file": image},
                timeout=30
            )

            if response.status_code == 200:
                result = response.json()
            else:
                error = "Moderation failed"

        except Exception as e:
            error = str(e)

    return render(request, "ui/index.html", {
        "result": result,
        "error": error
    })
