# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 06:21:20 2022

@author: opera
"""

# Modulo 1  - Crea una Cadenas de Bloques

# Para Instalar
# Flask==1.2.2: pip install Flask==1.2.2
# Cliente HTTP Postman: http://www.getpostman.com/

# Importar las librerias
import datetime
import hashlib
import json
from flask import Flask, jsonfly

# Parte 1 - Crear la Cadena de Bloques
class Blockchain:
    
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')
    
    def create_block(self, proof , previous_hash):
        block = {'index' : len(self.chain)+1,
                 'timestamp' : str(datetime.datetime.now()),
                  'proof' : proof,
                  'previous_hash' : previous_hash}

        self.chain.append(block)
        return block
    
    def get_previous_block (self):
        return self.chain[-1]
    
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else: 
                new_proof += 1
        return new_proof()
        
    def hash(self, block):
        encoded_block = json.dumps(block, sor_keys = True)
        
        
        
# Parte 2 - Minado de un Bloque de la Cadena























