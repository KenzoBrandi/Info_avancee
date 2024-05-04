import argparse
import os
import lang_detector
import utils




def main(args):
   lang2data =  utils.read_references("Data/Data/Train/")
   target = utils.read_corpus(args.corpus)
   
   return lang_detector.detect_lang(lang2data, target)

def evaluation(train,test,n=-1):
    train_dic = utils.read_references(train,n)
    test_dic = utils.read_references(test,n)
    nb_correct = 0
    for key,value in test_dic.items():
       detected_lang = lang_detector.detect_lang(train_dic,value)
       if detected_lang[0] == key:
          nb_correct += 1
    return nb_correct / len(test_dic)
 



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('corpus', type=str)
    args = parser.parse_args()
    result = main(args)
    print('La langue détectée est: ',result[0])
    print('Voici le score par langue: ',result[1])         
    print('Le score de performance est de: ',evaluation("Data/Data/Train/","Data/Data/Test/"))


