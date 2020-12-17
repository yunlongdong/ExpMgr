import time
import json
import os
import sys
from copy import copy
from .constants import results_dir

class Monitor:
    def __init__(self, name_info=''):
        self.timestamp = str(int(round(time.time() * 1000)))
        self.date = time.strftime("%Y-%m-%d %H_%M")
        self.json = {}
        self.name_info = name_info
        self.results_dir = results_dir
        if not os.path.exists(self.results_dir):
            os.mkdir(self.results_dir)
            
    def load_args(self, args):
        """
        load args, dict needed
        """
        self.json = copy(args)
        self.json['date'] = self.date
        
    def track(self, step, value, name):
        """
        track the value at step, with name. ExpMgr will add prefix log_ before name
        """ 
        name = 'log_' + name
        if name in self.json:
            self.json[name].append([step, value])
        else:
            self.json[name] = []

    def save(self):
        fn = self.results_dir + '/' +self.timestamp + self.name_info + '.json'
   
        with open(fn, 'w') as fp:
            json.dump(self.json, fp)
            

if __name__ == "__main__":
    m = Monitor()
    
    args = {'lr':1e-4, 'bs':256}
    
    m.load_args(args)
    
    for i in range(10):
        m.track(i, i+2, 'loss')
        
    m.save()    
            