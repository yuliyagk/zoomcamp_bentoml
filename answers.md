## Homework


## Question 1

* Install BentoML
* What's the version of BentoML you installed?
* Use `--version` to find out

### Answer

```bash
$ bentoml --version
bentoml, version 1.0.7
```

## Question 2

Run the notebook which contains the xgboost model from module 6 i.e previous module and save the xgboost model with BentoML. To make it easier for you we have prepared this [notebook](https://github.com/alexeygrigorev/mlbookcamp-code/blob/master/course-zoomcamp/07-bentoml-production/code/train.ipynb). 


How big approximately is the saved BentoML model? Size can slightly vary depending on your local development environment.
Choose the size closest to your model.

* 924kb
* 724kb
* ***114kb***
* 8kb

### Answer

```bash
$ bentoml models list
Tag                                 Module           Size        Creation Time
credit_risk_model:cc3k7jstyo2ssjje  bentoml.xgboost  197.80 KiB  2022-10-24 10:41:18
credit_risk_model:tedcajcta62ssjje  bentoml.xgboost  197.77 KiB  2022-10-23 12:19:21
credit_risk_model:6nwa2bcta22ssjje  bentoml.xgboost  197.77 KiB  2022-10-23 12:14:43
```

Answer = 114kb


## Question 3

Say you have the following data that you're sending to your service:

```json
{
  "name": "Tim",
  "age": 37,
  "country": "US",
  "rating": 3.14
}
```

What would the pydantic class look like? You can name the class `UserProfile`.

### Answer:

```python
from pydantic import BaseModel

class UserProfile(BaseModel):
    name: str
    age: int
    country: str
    rating: float
```

## Question 4

We've prepared a model for you that you can import using:

```bash
curl -O https://s3.us-west-2.amazonaws.com/bentoml.com/mlzoomcamp/coolmodel.bentomodel
bentoml models import coolmodel.bentomodel
```

What version of scikit-learn was this model trained with?

* ***1.1.1***
* 1.1.2
* 1.1.3
* 1.1.4
* 1.1.5

### Answer

```bash
$ bentoml models get  mlzoomcamp_homework:qtzdz3slg6mwwdu5
name: mlzoomcamp_homework
version: qtzdz3slg6mwwdu5
module: bentoml.sklearn
labels: {}
options: {}
metadata: {}
context:
  framework_name: sklearn
  framework_versions:
    scikit-learn: 1.1.1
  bentoml_version: 1.0.7
  python_version: 3.9.12
signatures:
  predict:
    batchable: false
api_version: v1
creation_time: '2022-10-13T20:42:14.411084+00:00'
```

## Question 5

Create a bento out of this scikit-learn model. The output type for this endpoint should be `NumpyNdarray()`

Send this array to the Bento:

```
[[6.4,3.5,4.5,1.2]]
```

You can use curl or the Swagger UI. What value does it return? 

* 0
* ***1***
* 2
* 3

### Answer : 1

(Make sure your environment has Scikit-Learn installed) 


## Question 6

Ensure to serve your bento with `--production` for this question

Install locust using:

```bash
pip install locust
```

Use the following locust file: [locustfile.py](locustfile.py)

Ensure that it is pointed at your bento's endpoint (In case you didn't name your endpoint "classify")

<img src="resources/classify-endpoint.png">

Configure 100 users with ramp time of 10 users per second. Click "Start Swarming" and ensure that it is working.

Now download a second model with this command:

```bash
curl -O https://s3.us-west-2.amazonaws.com/bentoml.com/mlzoomcamp/coolmodel2.bentomodel
```

Or you can download with this link as well:
[https://s3.us-west-2.amazonaws.com/bentoml.com/mlzoomcamp/coolmodel2.bentomodel](https://s3.us-west-2.amazonaws.com/bentoml.com/mlzoomcamp/coolmodel2.bentomodel)

Now import the model:

```bash
bentoml models import coolmodel2.bentomodel
```

Update your bento's runner tag and test with both models. Which model allows more traffic (more throughput) as you ramp up the traffic?

**Hint 1**: Remember to turn off and turn on your bento service between changing the model tag. Use Ctl-C to close the service in between trials.

**Hint 2**: Increase the number of concurrent users to see which one has higher throughput

Which model has better performance at higher volumes?

* ***The first model***
* The second model

### Answer:
Model 1


## Email from marketing

Hello ML person! I hope this email finds you well. I've heard there's this cool new ML model called Stable Diffusion.
I hear if you give it a description of a picture it will generate an image. We need a new company logo and I want it
to be fierce but also cool, think you could help out?

Thanks,

Mike Marketer


## Question 7 (optional)

Go to this Bento deployment of Stable Diffusion: http://54.176.205.174/ (or deploy it yourself)

Use the txt2image endpoint and update the prompt to: "A cartoon dragon with sunglasses". 
Don't change the seed, it should be 0 by default

What is the resulting image?

### #1
<img src="resources/dragon1.jpeg">

### #2 
<img src="resources/dragon2.jpeg">

### #3 
<img src="resources/dragon3.jpeg">

### #4
<img src="resources/dragon4.jpeg">


## Submit the results

* Submit your results here: https://forms.gle/Hh9FWy6LGXk3wJYs8
* You can submit your solution multiple times. In this case, only the last submission will be used 
* If your answer doesn't match options exactly, select the closest one


## Deadline

The deadline for submitting is **24 October 2022 (Monday), 23:00 CEST (Berlin time)**. 

After that, the form will be closed.
