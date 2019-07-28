model_path = "/home/jilei/Bert_Model/Bert_Pytorch_Model"

from bert import Ner

model = Ner(model_path)

output = model.predict("功能失调性子宫出血 高血压 糖尿病病")

print(output)
# ('Steve', {'tag': 'B-PER', 'confidence': 0.9981840252876282})
# ('went', {'tag': 'O', 'confidence': 0.9998939037322998})
# ('to', {'tag': 'O', 'confidence': 0.999891996383667})
# ('Paris', {'tag': 'B-LOC', 'confidence': 0.9991968274116516})
