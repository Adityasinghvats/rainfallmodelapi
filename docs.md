# rainfallmodelapi
- Flask backend for the rainfall prediction model running in form of a pickle file.

---
## GET
- `http://127.0.0.1:5000`

- This is a healtcheck route.

﻿

## POST
- `http://127.0.0.1:5000/predict`
- Make the request into the specified JSON body fromat to receive a prediction for the ML model.
```javascript
{
    "pressure":101.9,
    "maxtemp":22.7, 
    "dewpoint":19.9, 
    "humidity":98, 
    "cloud":8, 
    "sunshine":50.0, 
    "winddirection":40.0, 
    "windspeed":13.7
}
```

## To run as a Docker container on port 5000
```bash
# Build the Docker image
docker build -t rainfall-prediction-api .
```
```bash
# Run the container
docker run -p 5000:5000 rainfall-prediction-api
```