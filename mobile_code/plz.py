import urllib2
import json
import android
 
SERVER_IP = '192.168.1.5'
SERVER_PORT = 6543
 
 
def get_info_projects():
    "Fetches info projects list from server and returns as a python list"
 
    url = "http://{server_ip}:{port}/json/project_list".format(server_ip=SERVER_IP, port=SERVER_PORT)
    json_data = urllib2.urlopen(url).read()
 
    return json.loads(json_data)
  
#def display_info_projects_items(selected_project):
    "Fetches info projects list from server and returns as a python list"
 #   project_name = selected_project
  #  data = json.dumps([project_name])
   # url = "http://{server_ip:{port}/json/project_details/".format(server_ip=SERVER_IP, port=SERVER_PORT)
    #req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
    
    
    #json_data = urllib2.urlopen(url).read()
    #l=json_data
   
 
 
 
def select_info_project(droid, project_list):
 
    droid.dialogCreateAlert("Select Info Project")
    droid.dialogSetItems(project_list)
    droid.dialogShow()
    response = droid.dialogGetResponse().result
 
    #{u'item': 0}
    project = project_list[response['item']]
   
    url = "http://{server_ip}:{port}/json/project_details/ppp ".format(server_ip=SERVER_IP, port=SERVER_PORT)
    json_data = urllib2.urlopen(url).read()
 
    p=json.loads(json_data)
    return p

 
    
 
 
if '__main__' == __name__:
 
    droid = android.Android()
 
    info_projects = get_info_projects()
    selected_project = select_info_project(droid, info_projects.keys())
    #droid.makeToast("Selected Project is: " + selected_project)
    
    #l = []
    #l = display_info_projects_items(selected_project)
    #return json.loads(json_data)
    droid.makeToast("Selected Project items are: " + "".join(str(x) for x in selected_project))
 