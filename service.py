import numpy as np

import bentoml
from bentoml.io import JSON
from bentoml.io import NumpyNdarray

# Model 1
#model_ref= bentoml.sklearn.get("mlzoomcamp_homework:qtzdz3slg6mwwdu5")
# Model 2
model_ref= bentoml.sklearn.get("mlzoomcamp_homework:jsi67fslz6txydu5")

model_runner = model_ref.to_runner()

svc = bentoml.Service("coolmodel", runners=[model_runner])


@svc.api(input=NumpyNdarray(), output=NumpyNdarray())
async def classify(vector):
    prediction = await model_runner.predict.async_run(vector)
    return prediction

