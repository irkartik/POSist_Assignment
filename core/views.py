# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Node, Data


# Create your views here.

def createGenesisNode(request):
	''' THIS VIEW TAKES INPUT FROM USERS VIA API ENDPOINT AND CREATES A GENESIS NODE '''
	'''
		input values {
			data {
				value (floating point value)
			}
			referenceNodeId 
			childReferenceNodeId
			genesisReferenceNodeId
		}
	'''
	
	#VALUES RECIEVED FROM THE API
	value = request.POST.get('value')

	data = Data.objects.create(value=value)
	temp_node = Node.objects.create(data = data)

	return HttpResponse("Genesis Node Created")


def createChildNode(request):
	'''
	THIS VIEW TAKES INPUT FROM USERS VIA API ENDPOINT AND CREATES A CHILD NODE
	
	input values {
			data {
				value (floating point value)
			}
			referenceNodeId 
			childReferenceNodeId
			genesisReferenceNodeId
		}

	'''

	#VALUES RECIEVED FROM THE API
	value = request.POST.get('value')
	referenceNodeId = request.POST.get('referenceNodeId')
	genesisReferenceNodeId = request.POST.get('genesisReferenceNodeId')

	# TAKING THE PREVIOUSLY CREATED GENESIS NODE / PARENT NODE TO EMBED ID'S OF THE CHILD NODE CREATED
	genesisReferenceNode = Node.objects.get(nodeId= genesisReferenceNodeId)
	parent_node = Node.objects.get(nodeId = referenceNodeId) #TAKING THE PARENT NODE SPECIFIED BY THE USER WHERE THE CHILD WILL BE APPENDED


	# CREATING A NEW CHILD NODE

	data = Data.objects.create(value=value)
	child_node = Node()
	child_node.data = data
	child_node.referenceNodeId=parent_node
	child_node.genesisReferenceNodeId=genesisReferenceNodeId


	# APPENDING THE CREATED CHILD ID TO THE PARENT'S CHILDREFERENCENODEID ATTRIBUTE
	sum = 0
	for children in parent_node.childReferenceNodeId:
		sum += children.data.value

	if child_node.value <= sum:
		child_node.save()		# SAVE THE CHILD ONLY IF THE VALUE OF CHILD NODE IS SMALLER THAN THE VALUE (PARENT_VALUE - (SUM OF ALL CHILD VALUES))


def editNode(request):
	'''
	USER PROVIDES THE NODEID OF THE NODE TO BE EDITED 
		# USERS SELECT THE NODE FROM THE DROPDOWN MENU AT THE FRONTEND
		
		

	'''
