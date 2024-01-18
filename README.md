# BotaniScan API

BotaniScan API is a REST API that provides a simple interface for recognise diseases of plants using images.

## Model

Efficient Net is used as the baseline model. Weights of Efficient Net finetuned using 10 datasets.

### Dataset

| Dataset                      | no of Samples | no of classes | Link                                                                                                 | Source                                                                                  |
| ---------------------------- | ------------- | ------------- | ---------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Cassava Leaf Disease Dataset | 21400         | 5             | [Cassava Leaf Disease Dataset](https://tensorflow.google.cn/datasets/catalog/cassava)                | Ernest Mwebaze and Timnit Gebru and Andrea Frome and Solomon Nsumba and Jeremy Tusubira |
| Rice Leaf Disease Images     | 5932          | 4             | [Rice Leaf Disease Images](https://data.mendeley.com/datasets/fwcj7stb8r/1)                          | Sethy, P. K., Barpanda, N. K., Rath, A. K., & Behera, S. K.                             |
| PlantVillage                 | 54303         | 38            | [PlantVillage](https://www.tensorflow.org/datasets/catalog/plant_village)                            | David P. Hughes and Marcel Salath                                                       |
| Potato Leaf Disease          | 4072          | 3             | [Potato Leaf Disease](https://www.mdpi.com/2079-9292/10/17/2064)                                     | images collected from the Central Punjab region of Pakistan                             |
| Plant Pathelogy              | 2700          | 3             | [Plant Pathelogy](https://www.kaggle.com/c/plant-pathology-2020-fgvc7/data)                          |
| ESCA-dataset                 | 1768          | 2             | [ESCA-dataset](https://data.mendeley.com/datasets/89cnxc58kj/1)                                      |                                                                                         |
| Sugercane Leaf Image Dataset | 2569          | 5             | [Sugercane Leaf Image Dataset](https://data.mendeley.com/datasets/9424skmnrk/1)                      |
| Potato Leaf Disease          | 1500          | 3             | [Potato Leaf Disease](https://www.kaggle.com/datasets/muhammadardiputra/potato-leaf-disease-dataset) |                                                                                         |

### Model Performance

### Features

1. Login/ SignUp
1. Authentication(user/ admin)
1. Get/ Post/ Put/ Delete Crops
1. Get/ Post/ Put/ Delete Diseases
1. Get/ Post/ Put/ Delete Users
1. Get Predictions

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
