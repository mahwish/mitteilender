import urllib2
import json
import android

SERVER_IP = '192.168.1.6'
SERVER_PORT = 6543


def display_info_projects_items():
    "Fetches info projects list from server and returns as a python list"

    url = "http://{server_ip:{port}/json/project_details/{pname}".format(server_ip=SERVER_IP, port=SERVER_PORT)
    json_data = urllib2.urlopen(url).read()

    return json.loads(json_data)





if '__main__' == __name__:

    droid = android.Android()

    #info_projects = get_info_projects()
    #selected_project = select_info_project(droid, info_projects.keys())
     
     
    l=[]
    l=display_info_projects_items()
    " "".join function convert list into string " 
    droid.makeToast("Selected Project items are: " + "".join(str(x) for x in l))
