# -*- coding: utf-8 -*-
"""
   Module to define CONSTANTS used across the project
"""

from os import path

# identify basedir for the package
BASE_DIR = path.dirname(path.normpath(path.dirname(__file__)))
Dog_RemoteStorage = 'rshare:/Datasets/dogs_breed/'
Dog_RemoteShare = 'https://nc.deep-hybrid-datacloud.eu/s/D7DLWcDsRoQmRMN/download?path=%2F&files='
Dog_DataDir = 'dogImages'
Dog_LabelsFile = path.join(BASE_DIR, 'data','dog_names.txt')


machine_info = { 'cpu': '',
                 'gpu': '',
                 'memory_total': '',
                 'memory_available': ''
               }

# Dict of dicts with the following structure to feed the deepaas API parser:
#{ 'arg1' : {'default': 1,       # deafult value
#            'help': '',         # can be an empty string
#            'required': False   # bool
#            },
#  'arg2' : {...
#            },
#...
#}
train_args = { 'num_epochs': {'default': 10,
                              'help': 'Number of epochs to train on',
                              'required': False
                             },
               'network':   {'default': 'Resnet50',
                             'choices': ['Resnet50', 'InceptionV3', 'VGG16', 'VGG19'],
                             'help': 'Neural model to use',
                             'required': False
                           },
               'run_info': {'default': False,
                            'choices': [True, False],
                            'help': 'Print information about the run (e.g. cpu, gpu, memory)',
                            'required': False
                           },
}
predict_args = {'network':   {'default': 'Resnet50',
                             'choices': ['Resnet50', 'InceptionV3', 'VGG16', 'VGG19'],
                             'help': 'Neural model to use',
                             'required': False
                           },

}

