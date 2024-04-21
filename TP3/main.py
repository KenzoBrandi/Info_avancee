import argparse
import os
import lang_detector
import utils




def main(args):
   lang2data =  utils.read_references("Data\\Data\\Train\\")
   target = utils.read_corpus(args.corpus)
   
   return lang_detector.detect_lang(lang2data, target)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('corpus', type=str, default='world')
    args = parser.parse_args()

    print(main(args)) 


