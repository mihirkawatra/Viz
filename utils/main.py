from .get_json import get_json
import requests,json,time
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("-u", help="URL of the page")
# parser.add_argument("-t", help="Template name")
headers = {
    'Authorization': 'Token 6236181a5ad9e64b18a2c8968bc1c8d9a8afb9a2',
    'Content-Type': 'application/json'
}
get_url="https://beta.vizard.in/exports/"
post_url="https://beta.vizard.in/makevideo/"



def fetch_url(templateName,url,currency):
    raw,reason = get_json(templateName,url,currency)
    if(raw!=None):
        json_data=json.loads(raw)
        response = requests.post(post_url, headers=headers, json=json_data).json()
        exportId =  response['exportId']
        print("Export ID: " + exportId)

        if(exportId != None):
            url=get_url+str(exportId)+"/"
            print("Creating video...")
            t = time.time()
            while True:
                response=requests.get(url, headers=headers).json()
                if(response['progress']==100):
                    break
                # if(time.time()-t > 60.0):
                #     return None,"Timeout Error while creating the video."
                print(str(response['progress'])+"%...")
                time.sleep(5)
            return response['output'],None
        else:
            return None,"An error occured while creating the video."
    else:
        return None,"Couldn't send request to video server. <br>" + reason


#
# if __name__ == '__main__':
#     args = parser.parse_args()
#     if args.t != None and args.u != None:
#         template = args.t
#         url = args.u
#         output = fetch_url(makevideo(template,url))
#         if(output != None):
#             print(output)
#     else:
#         print("Please enter the url with -u and template with -t.")
