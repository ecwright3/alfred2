import requests
import config
import json
import sqlite3


def get_droplets(dropletId):
    #Get List of Droplets
    url = "https://api.digitalocean.com/v2/droplets/" + str(dropletId)
    r = requests.get(
        url,
        auth = (config.Mytoken,"")
    )
    DropletData = r.json()

    return DropletData['droplet']

def create_droplet(name=None):
    #Build the droplet
    if name == None:
        name = "Alfred-Test-Server"

    r = requests.post(
        "https://api.digitalocean.com/v2/droplets",
        auth = (config.Mytoken, ""),
        headers = {"Content-Type": "application/json"},
        data = json.dumps({
            "name": name,
            "region": "nyc3",
            "size": "s-1vcpu-1gb",
            "image": "ubuntu-16-04-x64",
            "ssh_keys": [18403716],
            "backups": False,
            "ipv6": False,           
            "user_data": None,
            "private_networking": None,
            "volumes"   : None
        })
    )

    if r.status_code == 202:
        dropletId = r.json()['droplet']['id']
        #print(dropletId)
        #print(r.json())

    #print(r.status_code)

    #Get Firewall Details if Creation was successfull
    if r.status_code == 202:
        r = requests.get(
            "https://api.digitalocean.com/v2/firewalls",
            auth = (config.Mytoken, ""),
            headers = {"Content-Type": "application/json"}
        )
        
        FirewallId = r.json()['firewalls'][0]['id']
        
        #Place the droplet behind the firewall
        FirewallUrl = "https://api.digitalocean.com/v2/firewalls/" + FirewallId + "/droplets"

        r = requests.post(
            FirewallUrl,
            auth = (config.Mytoken, ""),
            headers = {"Content-Type": "application/json"},
            data = json.dumps({
                "droplet_ids" : [dropletId],
            })
        )

        #Get Droplet Details
        Droplet = get_droplets(dropletId) 
        DropletData = {
            "id" : Droplet['id'],
            "name": Droplet['name'],
            "created_at" : Droplet['created_at'],
            "ip_address" : Droplet['networks']['v4'][0]['ip_address']
        }

        return DropletData

#create_droplet()

def delete_droplet(id):
    url = "https://api.digitalocean.com/v2/droplets/" + id
    r = requests.delete(
         url,
         auth = (config.Mytoken, ""),
         headers = {"Content-Type": "application/json"}
    )

    #print(r.headers)
    if r.status_code == 204:
        status =  id + " has been deleted sucessfully!!"
        #print(status)
        return status
#delete_droplet()  
 
def get_sshkeys():
    r = requests.get(
        "https://api.digitalocean.com/v2/account/keys",
        auth = (config.Mytoken, ""),
        headers = {"Content-Type": "application/json"},
    ) 
    return r.json()

#get_sshkeys()   


def list_images():
    r = requests.get(
        "https://api.digitalocean.com/v2/images",
        auth = (config.Mytoken, ""),
        headers = {"Content-Type": "application/json"},        
    )
    images = r.json()["images"]
    lastpage = int((r.json()["links"]["pages"]["last"]).split("page=")[1])

    for i in range(2,lastpage):
        page = str(i)
        url = "https://api.digitalocean.com/v2/images?page=" + page
        r = requests.get(
               url,
                auth = (config.Mytoken, ""),
                headers = {"Content-Type": "application/json"},        
            )

        images.append(r.json()["images"])
             
    #print(images)
    return images
#list_images()


def list_droplets():
    r = requests.get(
        "https://api.digitalocean.com/v2/droplets",
        auth = (config.Mytoken, ""),
        headers = {"Content-Type": "application/json"},
    )
    droplets = r.json()['droplets']
    total = int(r.json()['meta']['total'])

    for i in range(2,total):
        page = str(i)
        r = requests.get(
            "https://api.digitalocean.com/v2/droplets?page=%s&per_page=1"%page,
            auth = (config.Mytoken, ""),
            headers = {"Content-Type": "application/json"},
        )
        droplets.append(r.json()['droplets'])
    return droplets    
    
#list_droplets()

        

