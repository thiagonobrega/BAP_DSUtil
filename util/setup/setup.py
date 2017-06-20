'''
Created on 23 de abr de 2016

@author: Thiago
'''
import pip


def install(package):
    pip.main(['install', package])

def update(package):
    pip.main(['update', package])
    
def upgradePiP():
    pip.main(['upgrade', 'pip'])

def upgrade(package):
    pip.main(['install','--upgrade' ,package])
        
if __name__ == '__main__':
    upgrade('setuptools')
    upgrade('pip')
# pyblomm
    install("numpy")
    install("matplotlib")
    install("ipython")
    install("jupyter")
    install("pandas")
    install("sympy")
    install("nose")
    install("scipy")

    

    