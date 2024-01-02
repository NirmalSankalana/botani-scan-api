# botani-scan-api

## Model

Resnet-50 is used as the baseline model. Weights of resnet finetuned using 10 datasets.

### Dataset

| Dataset                      | no of Samples | no of classes | Link                                                                                  | Source                                                                                       |
| ---------------------------- | ------------- | ------------- | ------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| JMuBEN Coffee Dataset        | 58500         | 5             | [JMuBEN Coffee Dataset](https://data.mendeley.com/datasets/tgv3zb82nd/1)              | Chuka University, University of Embu, Jomo Kenyatta University of Agriculture and Technology |
| Cassava Leaf Disease Dataset | 21400         | 5             | [Cassava Leaf Disease Dataset](https://tensorflow.google.cn/datasets/catalog/cassava) | Ernest Mwebaze and Timnit Gebru and Andrea Frome and Solomon Nsumba and Jeremy Tusubira      |
| Rice Leaf Disease Images     | 5932          | 4             | [Rice Leaf Disease Images](https://data.mendeley.com/datasets/fwcj7stb8r/1)           | Sethy, P. K., Barpanda, N. K., Rath, A. K., & Behera, S. K.                                  |
| PlantVillage                 | 54303         | 38            | [PlantVillage](https://www.tensorflow.org/datasets/catalog/plant_village)             | David P. Hughes and Marcel Salath                                                            |
| Potato Leaf Disease          | 4072          | 3             | [Potato Leaf Disease](https://www.mdpi.com/2079-9292/10/17/2064)                      | images collected from the Central Punjab region of Pakistan                                  |

## How to set up the project.

### Create environment

1. Install python 3.8 or above
2. Create and actiate virtual environment inside project folder
3. Install required libraries : `pip3 install -r requirements.txt`

### Run the project

1. uvicorn `uvicorn app.main:app --reload`
2. Swagger documentation is available at : `http://{host}:{port}/docs#`

### Save Dependancies

1. Run `pip3 freeze > requirements.txt` after installing any pip package
