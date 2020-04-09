
import string
import copy
import autosuggestion
print('from import')
predictor = autosuggestion.Gpt2Predictor()

def predict_until_punctuation(input_str):
  if not input_str:
    raise Exception('input string required')
  output_str = copy.deepcopy(input_str)
  while len(output_str) != 0 and output_str[-1] not in [".", "!", "?"]:
    prediction = predictor.predict_json({"previous": output_str})
    print('prediction = '.format(prediction))
    output_str += prediction["words"][0]

  return output_str

def predict_from_users_input():
  str_prompt = input('Start typing: ')
  while True:
    predicted_word = predictor.predict_json({'previous' : str_prompt})['words'][0]
    print('predicted str = {}'.format(str_prompt+' '+predicted_word))
    if input('Is that correct? y/n ')=='y':
      str_prompt += ' '+predicted_word
    else:
      continuation = input('Type your  continuation ')
      str_prompt+= ' '+continuation



if __name__ == "__main__":
  print('From main')
  #text = predict_until_punctuation("System for generating multiple choice quiestions is")
  predict_from_users_input()
  #print(text)