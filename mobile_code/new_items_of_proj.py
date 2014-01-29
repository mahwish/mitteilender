import urllib2
import json
import android

SERVER_IP = '192.168.1.2'
SERVER_PORT = 6543


def get_info_projects():
    "Fetches info projects list from server and returns as a python list"

    url = "http://{server_ip}:{port}/json/project_list".format(server_ip=SERVER_IP, port=SERVER_PORT)
    json_data = urllib2.urlopen(url).read()

    return json.loads(json_data)


def select_info_project(droid, project_list):

    droid.dialogCreateAlert("Select Info Project")
    dialog_items = []
    for P in project_list:
        dialog_items.append(P['name'])

    droid.dialogSetItems(dialog_items)
    droid.dialogShow()
    response = droid.dialogGetResponse().result

    #{u'item': 0}
    project = project_list[response['item']]['name']
    url = ("http://{server_ip}:{port}/json/project_details/" + project).format(server_ip=SERVER_IP, port=SERVER_PORT)
    json_data = urllib2.urlopen(url).read()

    p = json.loads(json_data)
    return p


def display_project_items(project_details):
    """
    Given a list of project items, displays them and returns the selected item
    """

    display_list = []
    for item in project_details:
        item_type = item['item_type'].lower()
        if 'section' == item_type:
            s = "{item_name} >>".format(**item)
        elif 'image' == item_type:
            s = "{item_name} (image)".format(**item)
        elif 'url' == item_type:
            s = "{item_name} (url):\n {item_value}".format(**item)
        elif 'cell' == item_type:
            s = "{item_name} (cell):\n {item_value}".format(**item)
        elif 'email' == item_type:
	    s = "{item_name} (email):\n {item_value}".format(**item)
	elif 'call' == item_type:
	    s = "{item_name} (call):\n {item_value}".format(**item)    
        elif 'sms' == item_type:
	    s = "{item_name} (sms):\n {item_value}".format(**item)    
        else:
            s = "{item_name}:\n {item_value}".format(**item)

        display_list.append(s)

    droid.dialogCreateAlert("Project Items")
    droid.dialogSetItems(display_list)
    droid.dialogShow()
    result = droid.dialogGetResponse().result

    return project_details[result['item']]


def display_project(items):

    selected_item = display_project_items(items)
    if 'text' == selected_item['item_type']:
        droid.makeToast("You selected: " + selected_item['item_name'])
    elif 'image' == selected_item['item_type']:
        image_url = ("http://{server_ip}:{port}/{image_url}").format(server_ip=SERVER_IP,
                                                                     port=SERVER_PORT,
                                                                     image_url=selected_item['item_value'])
        droid.view(image_url, "image/*")
    elif 'cell' == selected_item['item_type']:
      droid.phoneCallNumber(selected_item['item_value'])
    elif 'call' == selected_item['item_type']:
      droid.phoneCallNumber(selected_item['item_value'])
    elif 'sms' == selected_item['item_type']:
      droid.dialogCreateInput("Message", "Please type your message")
      droid.dialogSetPositiveButtonText("OK")
      droid.dialogShow()
      result = droid.dialogGetResponse().result
      
      print(result)
          
      num=selected_item['item_value'] 
      print num
      droid.smsSend(num, result[u'value'])
      #droid.smsSend([selected_item['item_value']],result[u'value'])  
      
      
    elif 'email' == selected_item['item_type']:
      str = selected_item['item_value']
      droid.sendEmail(str,"","")
      #droid.sendEmail([selected_item['item_value']],"hi","")
      
      
      
    elif 'url' == selected_item['item_type']:
      droid.view(selected_item['item_value'])    
    elif 'section' == selected_item['item_type']:
        display_project(selected_item['subitems'])

if '__main__' == __name__:

    droid = android.Android()
    info_projects = get_info_projects()
    project_details = select_info_project(droid, info_projects)
    display_project(project_details)

#    if 'item' in result:
#
#        if (result["item"] == 0): 
#            option = ['Message','Call']
#            droid.dialogCreateAlert("Select any one option from the following:")
#            droid.dialogSetItems(option)
#            droid.dialogShow()
#            result=droid.dialogGetResponse().result
#            if (result["item"] == 0):
#      droid.dialogCreateInput("Message", "Please type your message")
#          droid.dialogSetPositiveButtonText("OK")
#          droid.dialogShow()
#          result = droid.dialogGetResponse().result
#          print(result)
#          droid.smsSend(listt['cell_num'], result[u'value'])
#        elif (result["item"] == 1):  
#          droid.phoneCallNumber(listt['cell_num'])
#        else:
#          droid.makeToast("neutral")
#      elif (result["item"] == 5):
#    droid.phoneCallNumber(listt['landline'])
#      elif (result["item"] == 6):
#    droid.sendEmail(listt['email'],"","")
#    
#    
#      elif (result["item"] == 1):
#    droid.view("/home/mahwish/mitteilender/mitteilender/static/exhibition_marquee_floor_plan_20130320_1894935057.jpg","image/*")
#      #droid.makeToast("nooo")
    

      
    #droid.dialogShow()
    #response = droid.dialogGetResponse().result
    #droid.makeToast("Selected Project is: " + selected_project)
    
    #l = []
    #l = display_info_projects_items(selected_project)
    #return json.loads(json_data)
    #droid.makeToast("Selected Project items are: " + "".join(str(x) for x in selected_project))