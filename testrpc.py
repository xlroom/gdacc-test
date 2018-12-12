#!/usr/bin/env python3
# coding=utf-8
from locust import HttpLocust,TaskSet,task
import json,time
from web3 import Web3
from eth_account import Account

fl = open("data.json",encoding="utf-8")
data = json.load(fl)
nodes = data['nodes']
nodes_len = len(nodes)


def genHeader():
	header = {"Content-Type":"application/json","User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"}
	return header

def genId():
	ct = time.time()
	tid = int(ct*1000)
	return tid

def genTxData(f,t,v):
	tid = genId()
	data = {"jsonrpc":"2.0","method":"eth_sendTransaction","params":[{
			"from":f,
			"to":t,
			"gas":"0x76c0",
			"gasPrice":"0x3be912",
			"value":v,
			"data":"",
			"type":0
	}],"id":tid}
	return data

def execPost(ctx,data,tag):
	r = ctx.client.post("",json=data,headers=genHeader(),timeout=30)
	if r.status_code == 200:
		print("%s success: %s" % (tag,r.json()))
	else:
		print("%s error: %s" % (tag, r.json()))


class UserBehavior1(TaskSet):
	@task(1)
	def transaction(self):
		tx_from = nodes[0]['validator']
		data = genTxData(tx_from,"0xF0109fC8DF283027b6285cc889F5aA624EaC1F55","0x3b9aca00")
		execPost(self,data,"transaction1")

class UserBehavior2(TaskSet):
	@task(1)
	def transaction(self):
		tx_from = nodes[1]['validator']
		data = genTxData(tx_from,"0xF0109fC8DF283027b6285cc889F5aA624EaC1F55","0x3b9aca00")
		execPost(self,data,"transaction2")

class UserBehavior3(TaskSet):
	@task(1)
	def transaction(self):
		tx_from = nodes[2]['validator']
		data = genTxData(tx_from,"0xF0109fC8DF283027b6285cc889F5aA624EaC1F55","0x3b9aca00")
		execPost(self,data,"transaction3")

class UserBehavior4(TaskSet):
	@task(1)
	def transaction(self):
		tx_from = nodes[3]['validator']
		data = genTxData(tx_from,"0xF0109fC8DF283027b6285cc889F5aA624EaC1F55","0x3b9aca00")
		execPost(self,data,"transaction3")

class UserBehavior5(TaskSet):
	@task(1)
	def transaction(self):
		tx_from = nodes[4]['validator']
		data = genTxData(tx_from,"0xF0109fC8DF283027b6285cc889F5aA624EaC1F55","0x3b9aca00")
		execPost(self,data,"transaction3")		
						

class DPOSTesting1(HttpLocust):
	task_set = UserBehavior1
	weight = 1 if nodes_len > 0 else 0
	host = nodes[0]['host'] if nodes_len > 0 else ''
	wait = nodes[0]['wait'] if nodes_len > 0 else 0
	min_wait = wait
	max_wait = wait

class DPOSTesting2(HttpLocust):
	task_set = UserBehavior2
	weight = 1 if nodes_len > 1 else 0
	host = nodes[1]['host'] if nodes_len > 1 else ''
	wait = nodes[1]['wait'] if nodes_len > 1 else 0
	min_wait = wait
	max_wait = wait

class DPOSTesting3(HttpLocust):
	task_set = UserBehavior3
	weight = 1 if nodes_len > 2 else 0
	host = nodes[2]['host'] if nodes_len > 2 else ''
	wait = nodes[2]['wait'] if nodes_len > 2 else 0
	min_wait = wait
	max_wait = wait

class DPOSTesting4(HttpLocust):
	task_set = UserBehavior4
	weight = 1 if nodes_len > 3 else 0
	host = nodes[3]['host'] if nodes_len > 3 else ''
	wait = nodes[3]['wait'] if nodes_len > 3 else 0
	min_wait = wait
	max_wait = wait

class DPOSTesting5(HttpLocust):
	task_set = UserBehavior5
	weight = 1 if nodes_len > 4 else 0
	host = nodes[4]['host'] if nodes_len > 4 else ''
	wait = nodes[4]['wait'] if nodes_len > 4 else 0
	min_wait = wait
	max_wait = wait		
