import urllib2
import json
import android

SERVER_IP = '192.168.1.4'
SERVER_PORT = 6543


def get_info_projects():
    "Fetches info projects list from server and returns as a python list"

    url = "http://{server_ip}:{port}/json/project_list".format(server_ip=SERVER_IP, port=SERVER_PORT)
    json_data = urllib2.urlopen(url).read()

    return json.loads(json_data)


def select_info_project(droid, project_list):

    droid.dialogCreateAlert("Select Info Project")
    droid.dialogSetItems(project_list)
    droid.dialogShow()
    response = droid.dialogGetResponse().result

    #{u'item': 0}
    project = project_list[response['item']]

    return project


if '__main__' == __name__:

    droid = android.Android()

    info_projects = get_info_projects()
    selected_project = select_info_project(droid, info_projects.keys())
    droid.makeToast("Selected Project is: " + selected_project)
