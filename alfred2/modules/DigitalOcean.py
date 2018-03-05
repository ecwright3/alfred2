import requests
import json

class InfrastructureService():

    def get_server(self, token, dropletId):
        #Get List of Droplets
        url = "https://api.digitalocean.com/v2/droplets/" + str(dropletId)
        r = requests.get(
            url,
            auth = (token,"")
        )
        DropletData = r.json()

        return DropletData['droplet']

    def create_server(self,token, name=None):
        #Build the droplet
        if name == None:
            name = "Alfred-Test-Server"

        r = requests.post(
            "https://api.digitalocean.com/v2/droplets",
            auth = (token, ""),
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

        #Get Firewall Details if Creation was successfull
        if r.status_code == 202:
            r = requests.get(
                "https://api.digitalocean.com/v2/firewalls",
                auth = (token, ""),
                headers = {"Content-Type": "application/json"}
            )
            
            FirewallId = r.json()['firewalls'][0]['id']
            
            #Place the droplet behind the firewall
            FirewallUrl = "https://api.digitalocean.com/v2/firewalls/" + FirewallId + "/droplets"

            r = requests.post(
                FirewallUrl,
                auth = (token, ""),
                headers = {"Content-Type": "application/json"},
                data = json.dumps({
                    "droplet_ids" : [dropletId],
                })
            )

            #Get Droplet Details
            Droplet = self.get_server(token = token, dropletId=dropletId) 
            DropletData = {
                "id" : Droplet['id'],
                "name": Droplet['name'],
                #split time and convert from UTC local time
                #raw 'created_at' output:'2018-03-05T10:15:06Z'
                #
                "created_at" : Droplet['created_at'], 
                "type" : "server",
                "ip_address" : Droplet['networks']['v4'][0]['ip_address']
            }
            
            return DropletData

    def delete_server(self, token, id):
        url = "https://api.digitalocean.com/v2/droplets/" + id
        r = requests.delete(
            url,
            auth = (token, ""),
            headers = {"Content-Type": "application/json"}
        )

        #print(r.headers)
        if r.status_code == 204:
            status =  id + " has been deleted sucessfully!!"
            #print(status)
            return status
    
    def get_sshkeys(self, token):
        r = requests.get(
            "https://api.digitalocean.com/v2/account/keys",
            auth = (token, ""),
            headers = {"Content-Type": "application/json"},
        ) 
        return r.json()
    
    def list_images(self, token):
        r = requests.get(
            "https://api.digitalocean.com/v2/images",
            auth = (token, ""),
            headers = {"Content-Type": "application/json"},        
        )
        images = r.json()["images"]
        lastpage = int((r.json()["links"]["pages"]["last"]).split("page=")[1])

        for i in range(2,lastpage):
            page = str(i)
            url = "https://api.digitalocean.com/v2/images?page=" + page
            r = requests.get(
                url,
                    auth = (token, ""),
                    headers = {"Content-Type": "application/json"},        
                )

            images.append(r.json()["images"])
                
        #print(images)
        return images

    def list_servers(self, token):
        r = requests.get(
            "https://api.digitalocean.com/v2/droplets",
            auth = (token, ""),
            headers = {"Content-Type": "application/json"},
        )
        droplets = r.json()['droplets']
        total = int(r.json()['meta']['total'])

        for i in range(2,total):
            page = str(i)
            r = requests.get(
                "https://api.digitalocean.com/v2/droplets?page=%s&per_page=1"%page,
                auth = (token, ""),
                headers = {"Content-Type": "application/json"},
            )
            droplets.append(r.json()['droplets'])
        return droplets    
        


            

