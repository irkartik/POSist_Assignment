# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

def _createHash():
    """This function generate 10 character long hash"""
    hash = hashlib.sha1()
    hash.update(str(time.time()))
    return  hash.hexdigest()[:-10]


class Data(models.Model): 
	"""THIS MODEL IMPLEMENTS THE DATA THAT IS LINKED ONETOONE WITH THE NODE"""
	owner_id = models.CharField(max_length=100, blank=True, null=True)
	value = models.FloatField()
	owner_name = models.CharField(max_length=100, blank=True, null=True)
	hash_1 = models.CharField(max_length=10,default=_createHash,unique=True)

	def save(self, *args, **kwargs):
        self.value = round(self.value, 2)
        super(Data, self).save(*args, **kwargs)


class Node(models.Model):
	'''IMPLEMENTATION OF A NODE'''
	nodeNumber = models.AutoField(primary_key=True)
	nodeId = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4) #THIS GENERATES UNIQUE ID FOR THE NODE
	timestamp = models.DateTimeField(auto_add_now = True) #DEFAULTS TO THE TIMESTAMP WHEN THE NODE IS CREATED
 	data = models.ForeignKey(Data) 	#MAPS TO THE DATA MODEL
	referenceNodeId = models.OneToOneField(Node, related_name="address of parent node", blank=True, null=True)		#ADDRESS OF PARENT NODE
	childReferenceNodeId = models.ManyToManyField(Node, related_name="addresses of child nodes", blank=True, null=True)	#ADDERSSES OF CHILD NODE
	genesisReferenceNodeId = models.ForeignKey(Node, related_name="root node", blank=True, null=True)	#GENESIS REFERENCE NODE ADDRESS
	hash_1 = models.CharField(max_length=10,default=_createHash,unique=True)	#UNIQUE HASH VALUE FOR A NODE

