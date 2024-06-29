<p align="center">
    <img src="https://user-images.githubusercontent.com/74038190/216122028-c05b52fb-983e-4ee8-8811-6f30cd9ea5d5.png" alt="Comet" width="120" />
</p>

<p align="center">
    <b>Retrieve asteroids based on their closest approach to Earth data extractor from NASA API.</b>
</p>


### Introduction
This repository provides an example of a data extractor etl:

* Extracts data from [Asteroids - NeoWs API](https://api.nasa.gov//).
`GET https://api.nasa.gov/neo/rest/v1/feed?start_date=START_DATE&end_date=END_DATE&api_key=API_KEY`
* Transform the JSON object, then load the csv file into a `gs://bucket`
* Load to Big Query from Google Cloud Storage

### Prerequisites

Ensure you have the following:

- Python 3.8 or later installed
- Google Cloud SDK installed and configured
- A Google Cloud project with billing enabled

### Setup

1. Clone the repository:
```bash
git clone https://github.com/rubnsbarbosa/nasa-asteroids-extractor.git
cd nasa-asteroids-extractor
```

2. Create a virtual environment and install dependencies:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### License
MIT.
