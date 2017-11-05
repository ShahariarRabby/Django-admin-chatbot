import json, requests
from pprint import pprint


PAGE_ACCESS_TOKEN = "EAAGqvw8s9JcBAF9ZAc9kuR1iNhZBgnAFshroLfWfYZBwun3wleLUDalDSZB9QGrMwJe344XhkoxZCRYIE7yze1EiKkQkJ55F7Sla2ReLJZCMaInhuKZCAUvGwvECJZCSwedFAKF8Qlx05p7XuJ44zVRlA59nRMcVkurgaZARJTIJ2iVB8rYlDznrj"



def post_facebook_message(sender_id, message):
    data = {
    'recipient': {'id': sender_id},
    'message': message
            }
    pprint(message)
    qs = 'access_token=' + PAGE_ACCESS_TOKEN
    resp = requests.post('https://graph.facebook.com/v2.6/me/messages?' + qs,
                         json=data)
    pprint(resp.content)




def get_user_information(fbid):
    GRAPH_URL = ("https://graph.facebook.com/v2.7/{fbid}")
    user_info_url = GRAPH_URL.format(fbid=fbid)
    payload = {}
    payload['fields'] = 'first_name,last_name,profile_pic,locale,timezone,gender'
    payload['access_token'] = PAGE_ACCESS_TOKEN
    user_info = requests.get(user_info_url, payload).json()
    print user_info
    return user_info


class AttachmentTemplate:
    def __init__(self, url='', type='file'):
        self.template = {
    		"attachment": {
      			"type":"image",
      			"payload":  {
        		"url":"https://petersapparel.com/img/shirt.png"
      						}
    					  }
                        }
        self.url = url
        self.type = type
        # image / audio / video / file
    def get_message(self):
        self.template['attachment']['payload']['url'] = self.url
        self.template['attachment']['type'] = self.type
        return self.template