import numpy as np
import simplejson
import scipy.special
from time import sleep
from google.protobuf import text_format
import campaignProto_pb2
import time
from datetime import datetime,timedelta
#-----Kafka Producer ----------
__author__ = 'user'

from kafka.client import KafkaClient
from kafka.producer import SimpleProducer
from datetime import datetime

kafka =  KafkaClient("localhost:9092")

producer = SimpleProducer(kafka)

producer.send_messages("test", "This is message sent from python client " + str(datetime.now().time()) )
#----Kafka Producer ends ----------

"""
Global Variables are initiallized
"""
campaignHandle=campaignProto_pb2.CampaignParam()
text_format.Merge(open("campaignText.prototxt").read(),campaignHandle)
configHandle=campaignProto_pb2.ConfigParam()
text_format.Merge(open("config.txt").read(),configHandle)
busy=1;

"""
This function is trying to give index of array corrosp to its weight
"""
def generate_data(w):
	w=np.array(w,dtype=np.float32);
	w=np.cumsum(w/np.sum(w))
	for idx,elem in enumerate(w):
	    if(np.random.rand()<elem):return idx
"""
bias : max trafic, mean traffic, correlation, bursts/hr, burstary=[]
"""
def generate_single_entry():
	camp_weights=[c.w for c in campaignHandle.campaign]
	campaign=campaignHandle.campaign[generate_data(camp_weights)]
	prod_weights=[p.w for p in campaign.product]
	product=campaign.product[generate_data(prod_weights)]
	stage='e'+str(1+generate_data(configHandle.stage_w))+'00'

	single_entry={"advId":campaign.advId,"campId":campaign.campId,"prodId":"","stage":stage,"timestamp":str(time.time())}
	if(int(stage[1])>=3):single_entry["prodId"]=product.prodId
	return single_entry;
def next_burst():
	return configHandle.time_duration_milli*np.random.poisson(int(float(configHandle.burst_seperation_min)/float(configHandle.time_duration_milli)))
 

def next_no_traffic():
	return configHandle.time_duration_milli*np.random.poisson(int(float(configHandle.no_traffic_seperation_min)/float(configHandle.time_duration_milli)))

def send_data(data):
	producer.send_messages("test",str(data))


def time_indexed_data(start_time):
	mean=configHandle.mean_traffic;
	st=datetime.fromtimestamp(start_time)
	burst_start=next_burst()
	no_traffic_start=next_no_traffic()
	for i in range(1000000):
		sleep(float(configHandle.time_duration_milli)/1000)
		r=float(configHandle.mean_traffic)/float(configHandle.max_traffic)
		if(i>int(float(burst_start)/float(configHandle.time_duration_milli))):
			for j in range(int(float(configHandle.burst_duration_sec)/float(configHandle.time_duration_milli))):
				sleep(float(configHandle.time_duration_milli)/1000)
				count=int(configHandle.max_traffic*np.power(np.random.rand(),1/.95-1))
				for k in range(count):
					entry=generate_single_entry()
					entry["timestamp"]=str(time.mktime(st.timetuple()))
					send_data(entry)
				st=st+timedelta(milliseconds=configHandle.time_duration_milli)
			burst_start=burst_start+next_burst()

		elif(i>int(float(no_traffic_start)/float(configHandle.time_duration_milli))):
			for j in range(int(float(configHandle.no_traffic_duration_sec)/float(configHandle.time_duration_milli))):
				sleep(float(configHandle.time_duration_milli)/1000)
				count=int(configHandle.max_traffic*np.power(np.random.rand(),1/.95-1))
				for k in range(count):
					entry=generate_single_entry()
					entry["timestamp"]=str(time.mktime(st.timetuple()))
					send_data(entry)
				st=st+timedelta(milliseconds=configHandle.time_duration_milli)
			no_traffic_start=no_traffic_start+next_no_traffic()	
		else:
			count=int(configHandle.max_traffic*np.power(np.random.rand(),1/r-1))
			mean=9*float(mean/10)+float(count)/10
			for j in range(count):
				entry=generate_single_entry()
				entry["timestamp"]=str(time.mktime(st.timetuple()))
				send_data(entry)
		
			#print entry
			st=st+timedelta(milliseconds=configHandle.time_duration_milli)


time_indexed_data(time.time())



