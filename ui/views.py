from django.shortcuts import render
import requests
# Create your views here.

def index(request):
    image_result = None
    text_result = None
    error = None

    # IMAGE MODERATION
    if request.method == "POST" and request.FILES.get("image"):
        image = request.FILES["image"]

        try:
            response = requests.post(
                "https://fastapi-backend-p6p0.onrender.com/api/image-moderate",
                files={"file": image},
                timeout=60
            )

            if response.status_code == 200:
                image_result = response.json()
            else:
                error = "Image moderation failed"

        except Exception as e:
            error = str(e)

    # TEXT SENTIMENT
    if request.method == "POST" and request.POST.get("text"):
        text = request.POST.get("text")

        try:
            response = requests.post(
                "https://fastapi-backend-p6p0.onrender.com/api/sentiment",
                json={"text": text},
                timeout=30
            )

            if response.status_code == 200:
                text_result = response.json()
            else:
                error = "Sentiment analysis failed"

        except Exception as e:
            error = str(e)

    return render(request, "ui/index.html", {
        "image_result": image_result,
        "text_result": text_result,
        "error": error
    })
