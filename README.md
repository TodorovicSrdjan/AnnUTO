# AnnUTO
Automated feed-forward artificial neural network 

Features:
- formats (atm): csv
- different methods for parsing dataset: url or file (multipart)
- model training (clasification or regression)
- results for training or testing set
- statistical indicators
- correlation matrix (image)
- feature (input) encoding and scaling
- custom architecture (layers, activation functions, number of nodes, weight initializers)
- hyperparameters configuration (algorithm, optimizer, learning rate)
- different metrics
- fill NaNs
    - mean
    - median
    - most frequent
    - fill with constant (number or string)
- modify dataset
- real-time reporting using sockets

# Setup

1. Download repo 
```
git clone https://github.com/TodorovicSrdjan/AnnUTO.git
```
2. Set current working directory to downloaded folder (`AnnUTO`)
3. (Optional) Create virtual environment and activate it
```
python -m venv path/to/some/folder

// linux; bash
source path/to/some/folder/bin/activate
```
4. Install project dependencies
```
pip install -r requirements.txt
```
5. Run app
```
python src/ann_server.py
```

# Usage

You can see API specification at: `localhost:10003/docs`

API (atm) does not have it's own database. After parsing dataset (url or file) API
returns dataset in internal json format.

Other endpoints can only work with that returned dataset. It's provided as url for
`stored_dataset` parameter.

You can configure some things like urls and ports in file `config.py`