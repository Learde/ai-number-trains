from fastapi.middleware.cors import CORSMiddleware
from io import BytesIO
from fastapi import FastAPI, File, UploadFile
import random
import datetime

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8008",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/")
def upload(file: UploadFile = File(...)):

    result = {}
    result['is_completed'] = True
    result['numbers']=[
        {
            'confidence': random.random() * 100,
            'digits':[
                {
                    "confidence": random.random() * 100,
                    "digit_center_x": random.randint(0, 1920),
                    "digit_center_y": random.randint(0, 1080),
                    "height": random.randint(0, 400),
                    "is_valid": True,
                    "value": str(random.randint(0, 9)),
                    "width": random.randint(0, 400)
                },
                {
                    "confidence": random.random() * 100,
                    "digit_center_x": random.randint(0, 1920),
                    "digit_center_y": random.randint(0, 1080),
                    "height": random.randint(0, 400),
                    "is_valid": True,
                    "value": str(random.randint(0, 9)),
                    "width": random.randint(0, 400)
                },
                {
                    "confidence": random.random() * 100,
                    "digit_center_x": random.randint(0, 1920),
                    "digit_center_y": random.randint(0, 1080),
                    "height": random.randint(0, 400),
                    "is_valid": True,
                    "value": str(random.randint(0, 9)),
                    "width": random.randint(0, 400)
                },
                {
                    "confidence": random.random() * 100,
                    "digit_center_x": random.randint(0, 1920),
                    "digit_center_y": random.randint(0, 1080),
                    "height": random.randint(0, 400),
                    "is_valid": True,
                    "value": str(random.randint(0, 9)),
                    "width": random.randint(0, 400)
                },
                {
                    "confidence": random.random() * 100,
                    "digit_center_x": random.randint(0, 1920),
                    "digit_center_y": random.randint(0, 1080),
                    "height": random.randint(0, 400),
                    "is_valid": True,
                    "value": str(random.randint(0, 9)),
                    "width": random.randint(0, 400)
                },
                {
                    "confidence": random.random() * 100,
                    "digit_center_x": random.randint(0, 1920),
                    "digit_center_y": random.randint(0, 1080),
                    "height": random.randint(0, 400),
                    "is_valid": True,
                    "value": str(random.randint(0, 9)),
                    "width": random.randint(0, 400)
                },
                {
                    "confidence": random.random() * 100,
                    "digit_center_x": random.randint(0, 1920),
                    "digit_center_y": random.randint(0, 1080),
                    "height": random.randint(0, 400),
                    "is_valid": True,
                    "value": str(random.randint(0, 9)),
                    "width": random.randint(0, 400)
                },
                {
                    "confidence": random.random() * 100,
                    "digit_center_x": random.randint(0, 1920),
                    "digit_center_y": random.randint(0, 1080),
                    "height": random.randint(0, 400),
                    "is_valid": True,
                    "value": str(random.randint(0, 9)),
                    "width": random.randint(0, 400)
                },
            ],
            "height": random.randint(0, 400),
            "img_height": random.randint(0, 1080),
            "img_name": "name.jpg",
            "img_type": "jpg",
            "img_width": random.randint(0, 1920),
            "is_rule_complete": True,
            "is_valid": True,
            "number": "28822880",
            "number_center_x": random.randint(0, 1920),
            "number_center_y": random.randint(0, 1080),
            "width": random.randint(0, 400)
        }
    ]
    result["timestamp"] = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

    return result