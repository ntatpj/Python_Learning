#=================================================================================================
#   FILE: Enic_Muse.py
#   USAGE: python3 ENIC.py
#   DESCRIPTION: Collects basic info of hardware and Applications installed.
#   REQUIREMENTS: Pre configured RHEL + RHEL OSC
#   BUGS:     ---
#   AUTHOR: Neha Tatpuje (mailto: neha.tatpuje@rbbn.com)
#   TEAM :  ECI T3-DevOps   (mailto: T3-DevOps@rbbn.com)                                     
#   COMPANY:  Ribbon Communications aka ECI Telecom Ltd.
#   VERSION:  4
#   CREATED:  13-Nov-2024
#   UPDATED:  15-Jan-2024; 31-Jan-2024; 6-March-2025
#   UPDATES in V2:  Added collection for details of Shelfs, Cards,NE_typeCount,NE_name_and_IP
#   UPDATES in V3:  Added collection for details of Serices.
#   UPDATES in V4:  Added collection for details of Tunnels, Totalcont, few parameters in Museinfo.
#   REVISION: V4
#=================================================================================================

import csv
import json
import subprocess as sp
import os
import re

class ENIC():
   
    def __init__(self,Customer_name,Country,Account_number):
        self.disk1=sp.getoutput(" HostInfo | grep -a sectors | cut -d ',' -f 1 | cut -d ' ' -f 2 |sed -n 1p")
        self.disk2=sp.getoutput(" HostInfo | grep  -a sectors | cut -d ',' -f 1 | cut -d ' ' -f 2 |sed -n 2p")
        self.disk3=sp.getoutput(" HostInfo | grep  -a sectors | cut -d ',' -f 1 | cut -d ' ' -f 2 |sed -n 3p")
        self.NC_ver = sp.getoutput("kubectl get configmap mi-setup -o jsonpath='{.data.manifest}' | python3 -c \"import sys, yaml, json; print(json.dumps(yaml.safe_load(sys.stdin.read())))\" | jq -r '.bundles[\"nc-k8s\"].version'")
        self.NP_ver = sp.getoutput("kubectl get configmap mi-setup -o jsonpath='{.data.manifest}' | python3 -c \"import sys, yaml, json; print(json.dumps(yaml.safe_load(sys.stdin.read())))\" | jq -r '.bundles[\"pts-k8s\"].version'")
        self.Single_or_cluster=sp.getoutput("kubectl get configmap mi-setup -o jsonpath='{.data.manifest}' | python3 -c \'import sys, yaml, json; print(json.dumps(yaml.safe_load(sys.stdin.read())))' | jq -r '.cluster.kube_nodes.count'")
        self.flavor=sp.getoutput(" kubectl get configmap mi-setup -o jsonpath='{.data.manifest}' | python3 -c \'import sys, yaml, json; print(json.dumps(yaml.safe_load(sys.stdin.read())))' | jq -r '.deployment.flavor'")
        # cores=sp.getoutput("HostInfo | grep CPU | cut -d ':' -f 2 | cut -d 'x' -f 2 | cut -d 'M' -f 1")
        # freq_per_core=sp.getoutput("HostInfo | grep CPU | cut -d ':' -f 2 | cut -d 'x' -f 1 | tr -s ' '|awk '{$1=$1; print}'")
        self.RAM=sp.getoutput("HostInfo | grep -a RAM | cut -d ':' -f 2 | cut -d '(' -f 2 | cut -d ')' -f 1")
        self.total_disk= self.gb_to_tb_and_total_disk()
        self.path = sp.getoutput("pwd")
        self.hypervisor = sp.getoutput("virt-what")
        self.OSRelease = sp.getoutput("cat /etc/redhat-release")
        self.OSCRelease = sp.getoutput("CheckApps.sh 2>/dev/null | grep -E 'OSC-|ACE-' | grep -v '^$'")

    def gb_to_tb_and_total_disk(self):
        GB_toTB=1000
        Disk1_number=sp.getoutput("HostInfo | grep -a sectors | cut -d ',' -f 1 | cut -d ' ' -f 2 |sed -n 1p | cut -d 'T' -f 1 | cut -d 'G' -f 1")
        Disk2_number=sp.getoutput("HostInfo | grep  -a sectors | cut -d ',' -f 1 | cut -d ' ' -f 2 |sed -n 2p | cut -d 'T' -f 1 | cut -d 'G' -f 1")
        Disk3_number=sp.getoutput("HostInfo | grep -a sectors | cut -d ',' -f 1 | cut -d ' ' -f 2 |sed -n 3p | cut -d 'T' -f 1 | cut -d 'G' -f 1")
        # print(Disk1_number,Disk2_number,Disk3_number)
        if (self.disk1 !='null' and self.disk2 !='null' and self.disk3 !='null'):
            if "G" in self.disk1:
                Disk1_number=float(Disk1_number)/GB_toTB
            else: 
                Disk1_number=float(Disk1_number)
            if "G" in self.disk2:
                Disk2_number=float(Disk2_number)/GB_toTB
            else:
                Disk2_number=float(Disk2_number)
            if "G" in self.disk3:
                Disk3_number=float(Disk3_number)/GB_toTB
            else:
                Disk3_number=float(Disk3_number)
            return (Disk1_number+Disk2_number+Disk3_number)
        elif self.disk2 == 'null':
            if "G" in self.disk1:
                Disk1_number=float(Disk1_number)/GB_toTB
            else: 
                Disk1_number=float(Disk1_number)
            return Disk1_number
            
    def geoedundancy(self):
        Georedundancy =sp.getoutput("kubectl get configmap mi-setup -o jsonpath='{.data.manifest}' | python3 -c \'import sys, yaml, json; print(json.dumps(yaml.safe_load(sys.stdin.read())))' | jq -r '.site_role'")
        if Georedundancy == "null":
            return("No")
        else:
            return("Yes")
    
    def CPU(self):
        import subprocess as sp
        cores=sp.getoutput("HostInfo | grep -a CPU | cut -d ':' -f 2 | cut -d 'x' -f 1 | awk '{$1=$1; print}'")
        cores=cores.strip()
        # freq_per_core=re.sub(r'\x1b\[[0-9;]*m','',freq_per_core)
        cores = re.sub(r'\x1b\[[0-9;]*m', '', cores)
        # print(f"cores is",int(cores))
        # print(f"freq_per_core is", float(freq_per_core))
        cpu=int(cores)
        return cpu
    
    def choose_cluster_type(self):
        if self.Single_or_cluster == '1':
            return "Single"
        elif self.Single_or_cluster == '3':
            return "Cluster"

    def NI_ver(self):
        return self.NC_ver if (sp.getoutput("kubectl get configmap mi-setup -o jsonpath='{.data.manifest}' | python3 -c \'import sys, yaml, json; print(json.dumps(yaml.safe_load(sys.stdin.read())))' | jq -r '.muse_profile_name'")) == 'NC-with-Muse-Insights' else 'null'

    def result(self):
        Result={}
        Result['Customer Name']=Customer_name
        Result['Country']=Country
        Result['Account Number']=Account_number
        Result['Network Controller Version']= self.NC_ver
        Result['Network Insights Version']=self.NI_ver()
        Result['Network Designer Version']=self.NC_ver
        Result['Network Planner Version']= self.NP_ver
        Result['Cluster/Single VM']=self.choose_cluster_type()
        Result['Installation Flavor']= self.flavor
        Result['VM vCPU']= self.CPU()
        Result['VM RAM']=self.RAM
        Result['VM Storage in TB']=self.gb_to_tb_and_total_disk()
        Result['Geo-Redundancy']=self.geoedundancy()
        Result['Hypervisor']=self.hypervisor
        Result['os-release']=self.OSRelease
        Result['osc-release']=self.OSCRelease
        # print(Result)
        Titles=list(Result.keys())
        # print(Titles)
        with open('MuseInfo.csv','w') as csvfile:
            writer=csv.DictWriter(csvfile,fieldnames=Titles)
            writer.writeheader()
            writer.writerow(Result)
        print(f"MuseInfo.csv located at {self.path}/MuseInfo.csv")

    def Connect_to_mongoDb(self):
        #All option of mongo pods
        self.pod_names = ["mongodb-0", "mongodb-1", "mongodb-2"]
        self.selected_pod = None

        #Get MongoDB password using kubectl
        self.command_get_password = [
            "kubectl", "get", "secret", "--namespace", "mi-mongodb", "muse-password",
            "-o", "jsonpath={.data.mongodb-root-password}"
        ]

        # Step 3: Decode the password using base64


        self.command_base64_decode = ["base64", "--decode"]

        # Running the above commands together
        try:
            password = sp.check_output(self.command_get_password, stderr=sp.PIPE).decode('utf-8').strip()
            decoded_password = sp.check_output(self.command_base64_decode, input=password.encode(), stderr=sp.PIPE).decode('utf-8').strip()
            #print(f"Decoded MongoDB password: {decoded_password}")
        except sp.CalledProcessError as e:
            print(f"Error fetching password: {e.output.decode()}")
            

    # Step 4: Try connecting to each pod until successful
        for pod_name in self.pod_names:
            # Try to execute a simple bash command on each pod
            self.command_exec_pod_test = ["kubectl", "-n", "mi-mongodb", "exec", "-it", f"pod/{pod_name}", "--", "bash", "-c", "echo connected"]

            try:
                # Execute the command to check if the pod is reachable
                sp.check_call(self.command_exec_pod_test, stderr=sp.PIPE)
                # print(f"Successfully connected to {pod_name}")
                self.selected_pod = pod_name
                break  # Stop trying further pods if one succeeds
            except sp.CalledProcessError as e:
                print(f"Failed to connect to {pod_name}: {e.output.decode()}")

        # If no pod is selected, return an error
        if not self.selected_pod:
            print("Error: Could not connect to any of the pods.")
            return
        
        try:
            self.command_exec_pod = ["kubectl", "-n", "mi-mongodb", "exec", "-it", f"{self.selected_pod }", "--", "bash"]
            #print(f"connected to po {self.selected_pod}")
            
        except:
            print(f"Failed to connect to {self.selected_pod}")

        # Step 5: Connect to MongoDB and run the Mongo shell commands
        self.mongo_command = f"mongo -uroot -p{decoded_password}"
        
    def Query_for_Shelfs(self):
        # This is the script we want to execute inside the MongoDB shell
        mongo_script = '''
            use nc_eqpinventorydb;
            db.getCollection("Shelfs").find({}, { shelfType: 1, nodeManagementIp: 1, neProxyVersion: 1, _id: 0 }).toArray().map(doc => ({
                shelfType: doc.shelfType,
                nodeManagementIp: doc.nodeManagementIp,
                neProxyVersion: doc.neProxyVersion
            }));
        '''

        # Use sp to send the Mongo command
        try:
            # Open a sp to execute the kubectl exec command
            exec_process = sp.Popen(self.command_exec_pod, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE, universal_newlines=True)

            # Send Mongo command through stdin to the exec process
            output, error = exec_process.communicate(input=f"{self.mongo_command}\n{mongo_script}\n")

            if exec_process.returncode == 0:
                #print("MongoDB Command Output:")
                #print(output)  # Print raw output for debugging

                # Attempt to extract JSON part
                start_idx = output.find('[')  # Find the starting index of the JSON array
                end_idx = output.rfind(']') + 1  # Find the ending index of the JSON array

                # Check if valid JSON array is found
                if start_idx != -1 and end_idx != -1:
                    json_part = output[start_idx:end_idx]
                    # Replace 'undefined' with 'null' to make it valid JSON
                    json_part = json_part.replace('undefined', 'null')
                    try:
                        data = json.loads(json_part)
                        #print(data)  # Print the parsed data
                    except json.JSONDecodeError as e:
                        print(f"Error decoding JSON: {e}")
                        #print("Output received was:", json_part)
                else:
                    print("No valid JSON array found in the output.")
            else:
                print(f"Error executing MongoDB commands: {error}")
        except sp.CalledProcessError as e:
            print(f"Error executing kubectl exec for methos Query_for_Shelfs: {e.output.decode()}")

        # CSV export
        csv_filename = 'Shelfs.csv'
        with open(csv_filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['shelfType', 'nodeManagementIp', 'neProxyVersion'])
            writer.writeheader()
            if 'data' in locals() and data:  # Ensure 'data' is defined and not empty
                writer.writerows(data)
            else:
                print("No data to write to CSV")

        print(f"Shelfs.csv located at {self.path}/{csv_filename}")

    def Query_for_Cards(self):
        mongo_script = '''    
            use nc_eqpinventorydb;
            db.getCollection("Inventories").find({}, {
                managementIp: 1,
                nodeFamily: 1,
                "cardsInventory.actualCardType": 1,
                "cardsInventory.hardwareRevision": 1,
                "cardsInventory.commonApolloSlotType": 1,
                "cardsInventory.nptSlotType": 1,
                "cardsInventory.serialNumber": 1,
                _id: 0
            }).toArray().map(doc => {
                return doc.cardsInventory.map(card => ({
                    managementIp: doc.managementIp,
                    nodeFamily: doc.nodeFamily,
                    actualCardType: card.actualCardType || "Unknown",
                    hardwareRevision: card.hardwareRevision ||  "Unknown",
                    SlotType: card.commonApolloSlotType || card.nptSlotType || "Unknown",
                    serialNumber: card.serialNumber || "Unknown"
                }));
            }).reduce((acc, curr) => acc.concat(curr), []);
            '''
       # Use sp to send the Mongo command
        try:
            # Open a sp to execute the kubectl exec command
            exec_process = sp.Popen(self.command_exec_pod, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE, universal_newlines=True)

            # Send Mongo command through stdin to the exec process
            output, error = exec_process.communicate(input=f"{self.mongo_command}\n{mongo_script}\n")

            if exec_process.returncode == 0:
                #print("MongoDB Command Output:")
                #print(output)  # Print raw output for debugging

                # Attempt to extract JSON part
                start_idx = output.find('[')  # Find the starting index of the JSON array
                end_idx = output.rfind(']') + 1  # Find the ending index of the JSON array

                # Check if valid JSON array is found
                if start_idx != -1 and end_idx != -1:
                    json_part = output[start_idx:end_idx]
                    # Replace 'undefined' with 'null' to make it valid JSON
                    json_part = json_part.replace('undefined', 'null')
                    try:
                        data = json.loads(json_part)
                        #print(data)  # Print the parsed data
                    except json.JSONDecodeError as e:
                        print(f"Error decoding JSON: {e}")
                        print("Output received was:", json_part)
                else:
                    print(f"No valid JSON array found in the output.The returncode for tunnels query is {exec_process}")
            else:
                print(f"Error executing MongoDB commands: {error}")
        except sp.CalledProcessError as e:
            print(f"Error executing kubectl exec: {e.output.decode()}")


         # CSV export
        csv_filename = 'Cards.csv'
        with open(csv_filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['managementIp', 'nodeFamily', 'actualCardType' , 'hardwareRevision' , 'SlotType' , 'serialNumber'])
            writer.writeheader()
           # Prepare data for writing to CSV
            writer.writerows(data)

        print(f"Cards.csv located at {self.path}/{csv_filename}")

    def NE_type_count(self):
        mongo_script=''' 
                use nc_eqpinventorydb;
                db.getCollection("Shelfs").aggregate([
            {
                $group: {
                    _id: { 
                        actualShelfType: "$actualShelfType",
                        nodeFamily: "$nodeFamily"
                    },
                    count: { $sum: 1 }
                }
            },
            {
                $project: {
                    actualShelfType: "$_id.actualShelfType",
                    nodeFamily: "$_id.nodeFamily",
                    count: 1,
                    _id: 0
                }
            }
        ]).toArray().map(doc => ({
            nodeFamily: doc.nodeFamily,
            actualShelfType: doc.actualShelfType,
            count: doc.count
        }));

        '''
     # Use sp to send the Mongo command
        try:
            # Open a sp to execute the kubectl exec command
            exec_process = sp.Popen(self.command_exec_pod, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE, universal_newlines=True)

            # Send Mongo command through stdin to the exec process
            output, error = exec_process.communicate(input=f"{self.mongo_command}\n{mongo_script}\n")

            if exec_process.returncode == 0:
                #print("MongoDB Command Output:")
                #print(output)  # Print raw output for debugging

                # Attempt to extract JSON part
                start_idx = output.find('[')  # Find the starting index of the JSON array
                end_idx = output.rfind(']') + 1  # Find the ending index of the JSON array

                # Check if valid JSON array is found
                if start_idx != -1 and end_idx != -1:
                    json_part = output[start_idx:end_idx]
                    # Replace 'undefined' with 'null' to make it valid JSON
                    json_part = json_part.replace('undefined', 'null')
                    try:
                        data = json.loads(json_part)
                        #print(data)  # Print the parsed data
                    except json.JSONDecodeError as e:
                        print(f"Error decoding JSON for NE_type_count: {e}")
                        print("Output received was:", json_part)
                else:
                    print("No valid JSON array found in the output.")
            else:
                print(f"NE_type_count Error executing MongoDB commands: {error}")
        except sp.CalledProcessError as e:
            print(f"NE_type_count Error executing kubectl exec: {e.output.decode()}")

        # CSV export
        csv_filename = 'NE_typeCount.csv'
        with open(csv_filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['nodeFamily','actualShelfType','count'])
            writer.writeheader()
            if 'data' in locals() and data:  # Ensure 'data' is defined and not empty
                writer.writerows(data)
            else:
                print("NE_type_count No data to write to CSV")

        print(f"NE_typeCount.csv located at {self.path}/{csv_filename}")

    def NE_name_and_IP(self):
        mongo_script='''
            use nc_netmgrfulfilldb;
            db.getCollection("NEs").find({},{name:1 , managementIp:1, _id:0}).toArray().map(doc => ({
                name: doc.name,
                managementIp: doc.managementIp,
            }));
        '''
        # Use sp to send the Mongo command
        try:
            # Open a sp to execute the kubectl exec command
            exec_process = sp.Popen(self.command_exec_pod, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE, universal_newlines=True)

            # Send Mongo command through stdin to the exec process
            output, error = exec_process.communicate(input=f"{self.mongo_command}\n{mongo_script}\n")

            if exec_process.returncode == 0:
                #print("MongoDB Command Output:")
                #print(output)  # Print raw output for debugging

                # Attempt to extract JSON part
                start_idx = output.find('[')  # Find the starting index of the JSON array
                end_idx = output.rfind(']') + 1  # Find the ending index of the JSON array

                # Check if valid JSON array is found
                if start_idx != -1 and end_idx != -1:
                    json_part = output[start_idx:end_idx]
                    # Replace 'undefined' with 'null' to make it valid JSON
                    json_part = json_part.replace('undefined', 'null')
                    try:
                        data = json.loads(json_part)
                        #print(data)  # Print the parsed data
                    except json.JSONDecodeError as e:
                        print(f"NE_name_and_IP Error decoding JSON: {e}")
                        print("NE_name_and_IP Output received was:", json_part)
                else:
                    print("NE_name_and_IP No valid JSON array found in the output.")
            else:
                print(f"Error executing MongoDB commands: {error}")
        except sp.CalledProcessError as e:
            print(f"Error executing kubectl exec: {e.output.decode()}")

        # CSV export
        csv_filename = 'NE_name_and_IP'
        with open(csv_filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['name','managementIp'])
            writer.writeheader()
            if 'data' in locals() and data:  # Ensure 'data' is defined and not empty
                writer.writerows(data)
            else:
                print("No data to write to CSV")

        print(f"NE_name_and_IP.csv located at {self.path}/{csv_filename}")


class Services(ENIC):
    def __init__(self):
        self.States_n_counts={}
        self.Types_n_counts={}
        self.SERVICE_STATE = ["PLANNED","IN_CONFLICT","INSTALLED","INTERMEDIATE_STATE","CREATING","PENDING_REMOVAL","DELETING","PLANNED_NOT_COMPLETED"]
        self.path = sp.getoutput("pwd")

    def Service_State_counter(self,mongo_query,field,service_dict):
        for i in self.SERVICE_STATE:
            # mongo_query_Complete = mongo_query + f'''"{i}"}})'''
            mongo_query_Complete = mongo_query + f'''"{field}":"{i}"}})'''

        # Use sp to send the Mongo command
            try:
                # Open a sp to execute the kubectl exec command
                exec_process = sp.Popen(self.command_exec_pod, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE, universal_newlines=True)

                # Send Mongo command through stdin to the exec process
                output, error = exec_process.communicate(input=f"{self.mongo_command}\n{mongo_query_Complete}\n")
                #print(output)
                # print(f"THer reutn code is {exec_process.returncode}")
                if exec_process.returncode == 0:
                    #print("MongoDB Command Output:")
                    # print(output)
                    match = re.search(r'(\d+)(?=\s*bye)', output)  # This matches any digits
                    if match:
                        count = match.group(1)  # Extract the matched number
                        service_dict[i]=int(count)
                        # print(f"MongoDB Command Result  (count) of {i}: {count}")
                    else:
                        print("No count value found.")
                                            
            except:
                print("ERROR in executing k8s command {e.output.decode()}")
        # print(service_dict) 
        return service_dict

    def Types_and_count_of_Services(self,SERVICE_FLOW_TYPE,mongo_query,field):
                # print(SERVICE_FLOW_TYPE,mongo_script,field_L3VPN_TYPE)
        Types_n_counts={}
        for i in SERVICE_FLOW_TYPE:
            mongo_query_Complete = mongo_query + f'''"{field}":"{i}"}})'''
            #print(f"The complete mongo query is {mongo_query_Complete}")
        # Use sp to send the Mongo command
            try:
                # Open a sp to execute the kubectl exec command
                exec_process = sp.Popen(self.command_exec_pod, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE, universal_newlines=True)

                # Send Mongo command through stdin to the exec process
                output, error = exec_process.communicate(input=f"{self.mongo_command}\n{mongo_query_Complete}\n")
                #print(output)
                # print(f"THer reutn code is {exec_process.returncode}")
                if exec_process.returncode == 0:
                    #print("MongoDB Command Output:")
                    # print(output)
                    match = re.search(r'(\d+)(?=\s*bye)', output)  # This matches any digits
                    if match:
                        count = match.group(1)  # Extract the matched number
                        Types_n_counts[i]=int(count)
                        # print(f"MongoDB Command Result  (count) of {i}: {count}")
                    else:
                        print("No count value found.")
                                            
            except:
                print("ERROR in executing k8s command {e.output.decode()}")
        # print (Types_n_counts)
        # Define the file name
        self.Service_type_filename = "SERVICETYPE.csv"
        # Open the CSV file for writing
        with open(self.Service_type_filename, mode='a', newline='') as csvfile:
            # Create a CSV DictWriter object
            writer = csv.writer(csvfile)
            
            # Write the header (column names)
            # writer.writerow(['TYPES', 'COUNT'])
            
            # Write the dictionary items into the CSV file
            for state, count in Types_n_counts.items():
                writer.writerow([state, count])

        
        return Types_n_counts

    def Mongo_query_builder(self):
    ###############SECTION FOR SERVICE STATE QUERIES################

        L3_mongo='''use l3vpn;  
        db.getCollection("l3vpn").countDocuments({'''
        field_L3="networkElementEntities.vrf.lifeCycleState"

        L2_mongo='''use srvcfull2packetmanager;
        db.getCollection("l2service").countDocuments({'''
        feild_L2="serviceAttr.m_LifecycleState"

        EVPN_mongo='''use evpn; 
        db.getCollection("evpn").countDocuments({'''
        feild_EVPN="state"
        
        # Srv.SERVICE_STATE()
        self.States_n_counts_L3VPN={}
        self.States_n_counts_L2VPN={}
        self.States_n_counts_EVPN={}

        self.States_n_counts_L3VPN=self.Service_State_counter(L3_mongo,field_L3,self.States_n_counts_L3VPN)
        # print(f"DONE WITH States_n_counts_L3VPN{self.States_n_counts_L3VPN}")
        self.States_n_counts_L2VPN=self.Service_State_counter(L2_mongo,feild_L2,self.States_n_counts_L2VPN)
        # print(f"DONE WITH States_n_counts_L2VPN{self.States_n_counts_L3VPN}")
        self.States_n_counts_EVPN=self.Service_State_counter(EVPN_mongo,feild_EVPN,self.States_n_counts_EVPN)
        # print(f"States of services are as follows:  self.States_n_counts_L3VPN{self.States_n_counts_L3VPN},self.States_n_counts_L2VPN{self.States_n_counts_L2VPN},self.States_n_counts_EVPN{self.States_n_counts_EVPN}")

    ###############SECTION FOR SERVICE FLOW TYPE QUERIES################
        SERVICE_FLOW_TYPE_L3VPN=["ANY_TO_ANY","CUSTOM","HUB_SPOKE"]     
        L3VPN_Types_mongo_script = '''use l3vpn;          
        db.getCollection("l3vpn").countDocuments({'''
        field_L3VPN_TYPE="vpnServiceTopology"
        self.Types_n_counts_L3VPN={}

        SERVICE_FLOW_TYPE_L2VPN=["CEPP2P","CESP2P","MP2MP","P2MP","P2P"]    
        L2VPN_Types_mongo_script = '''
            use srvcfull2packetmanager;
            db.getCollection("l2service").countDocuments({'''
        field_L2VPN_TYPE="serviceAttr.m_ServiceType"
        self.Types_n_counts_L2VPN={}

        SERVICE_FLOW_TYPE_EVPN=["EVPN_MPLS","EVPN_VPWS"]
        EVPN_Types_mongo_script = '''
            use evpn;
            db.getCollection("evpn").countDocuments({'''
        field_EVPN_TYPE="metadata.serviceType"
        self.Types_n_counts_EVPN={}

        self.Types_n_counts_L3VPN=self.Types_and_count_of_Services(SERVICE_FLOW_TYPE_L3VPN,L3VPN_Types_mongo_script,field_L3VPN_TYPE)
        self.Types_n_counts_L2VPN=self.Types_and_count_of_Services(SERVICE_FLOW_TYPE_L2VPN,L2VPN_Types_mongo_script,field_L2VPN_TYPE)
        self.Types_n_counts_EVPN=self.Types_and_count_of_Services(SERVICE_FLOW_TYPE_EVPN,EVPN_Types_mongo_script,field_EVPN_TYPE)
        # print(f"Types of services are as follows:  self.Types_n_counts_L3VPN{self.Types_n_counts_L3VPN},self.Types_n_counts_L2VPN{self.Types_n_counts_L2VPN},self.Types_n_counts_EVPN{self.Types_n_counts_EVPN=}")
        print(f"{self.Service_type_filename}located at {self.path}/{self.Service_type_filename}")

    def srv_result(self):
        #############COLLECT COUNT STATE OF ALL L3VPN,L2VPN & EVPN SERVICE###############
        ALL_SERVICE_STATES={}
        ALL_SERVICE_STATES["PLANNED"]=self.States_n_counts_L3VPN["PLANNED"]+self.States_n_counts_L2VPN["PLANNED"]+self.States_n_counts_EVPN["PLANNED"]
        ALL_SERVICE_STATES["IN_CONFLICT"]=self.States_n_counts_L3VPN['IN_CONFLICT']+self.States_n_counts_L2VPN['IN_CONFLICT']+self.States_n_counts_EVPN['IN_CONFLICT']
        ALL_SERVICE_STATES["INSTALLED"]=self.States_n_counts_L3VPN['INSTALLED']+self.States_n_counts_L2VPN['INSTALLED']+self.States_n_counts_EVPN['INSTALLED']
        ALL_SERVICE_STATES["INTERMEDIATE_STATE"]=self.States_n_counts_L3VPN['INTERMEDIATE_STATE']+self.States_n_counts_L2VPN['INTERMEDIATE_STATE']+self.States_n_counts_EVPN['INTERMEDIATE_STATE']
        ALL_SERVICE_STATES["CREATING"]=self.States_n_counts_L3VPN['CREATING']+self.States_n_counts_L2VPN['CREATING']+self.States_n_counts_EVPN['CREATING']
        ALL_SERVICE_STATES["PENDING_REMOVAL"]=self.States_n_counts_L3VPN['PENDING_REMOVAL']+self.States_n_counts_L2VPN['PENDING_REMOVAL']+self.States_n_counts_EVPN['PENDING_REMOVAL']
        ALL_SERVICE_STATES["DELETING"]=self.States_n_counts_L3VPN['DELETING']+self.States_n_counts_L2VPN['DELETING']+self.States_n_counts_EVPN['DELETING']
        ALL_SERVICE_STATES["PLANNED_NOT_COMPLETED"]=self.States_n_counts_L3VPN['PLANNED_NOT_COMPLETED']+self.States_n_counts_L2VPN['PLANNED_NOT_COMPLETED']+self.States_n_counts_EVPN['PLANNED_NOT_COMPLETED']

        # print(ALL_SERVICE_STATES)

        filename = 'Service_Flow.csv'
        # Open the CSV file for writing
        with open(filename, mode='w', newline='') as csvfile:
            # Create a CSV DictWriter object
            writer = csv.writer(csvfile)
            
            # Write the header (column names)
            writer.writerow(['State', 'Count'])
            
            # Write the dictionary items into the CSV file
            for state, count in ALL_SERVICE_STATES.items():
                writer.writerow([state, count])

        print(f"{filename} located at {self.path}/{filename}")


class Tunnels(ENIC):
    def __init__(self):
        # sp.getoutput('mkdir WRK_TUNNELS')
        self.Tunnel_entity_count={}
        self.Tunnel_entity_count_final={}
        self.path = sp.getoutput("pwd")
       
    def Mongo_query_maker(self,mongo_query,tunnels_entity):
        try:
            # Open a sp to execute the kubectl exec command
            exec_process = sp.Popen(self.command_exec_pod, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE, universal_newlines=True)

            # Send Mongo command through stdin to the exec process
            output, error = exec_process.communicate(input=f"{self.mongo_command}\n{mongo_query}\n")
            # print(output)
            # print(f"THer return code is {exec_process.returncode}")
            if exec_process.returncode == 0:
                # print("MongoDB Command Output:")
                # print(output)
                match = re.search(r'(\d+)(?=\s*bye)', output)  # This matches any digits       
                if match:
                        count = match.group(1)  # Extract the matched number
                        self.Tunnel_entity_count[tunnels_entity]=int(count)
                        # print(f"MongoDB Command Result  (count) of {tunnels_entity}: {count}")
                else:
                    print("No count value found.")
                                    
        except:
            print("ERROR in executing k8s command {e.output.decode()}")
     
        
        
    def Mongo_queries(self):
        # For mplstp: script we want to execute inside the MongoDB shell
        mplstp_mongo_script_BIDIRECTIONALITY = '''use tnlmgrmplstp;
            db.getCollection("MplstpTunnels").countDocuments({"tunnelDirection":"BIDIRECTIONAL"})
        '''

        mpls_tp_mongo_script_UNIDIRECTIONALITY='''use tnlmgrmplstp;
        db.getCollection("MplstpTunnels").countDocuments({"tunnelDirection":"UNIDIRECTIONAL"})
        '''
        mplstp_mongo_script_TUNNEL_STATE_OK='''use tnlmgrmplstp;
            db.MplstpTunnels.count({"lifecycle": "INSTALLED"})
        '''

        mplstp_mongo_script_TUNNEL_STATE_INCOMPLETE='''use tnlmgrmplstp;
            db.MplstpTunnels.count({
                "lifecycle": { $ne: "INSTALLED" }
            })
        '''

        mplstp_mongo_script_TUNNEL_Count_mplstp=''''use tnlmgrmplstp;
            db.getCollection("MplstpTunnels").countDocuments({})'''



        # For nctunneldb: scrpit we want to execute inside the MongoDB shell

        nctunneldb_mongo_script_BIDIRECTIONALITY='''use nc_tunneldb; 
        db.getCollection("Tunnels").countDocuments({"directionality" : "Bidirectional"})'''

        nctunneldb_mongo_script_UNIDIRECTIONALITY='''use nc_tunneldb; 
        db.getCollection("Tunnels").countDocuments({"directionality" : "Unidirectional"})'''


        nctunneldb_mongo_script_TUNNEL_STATE_OK='''use nc_tunneldb;
        db.getCollection("Tunnels").countDocuments({"lifeCycle": "Installed"})
            '''
        
        nctunneldb_mongo_script_TUNNEL_STATE_INCOMPLETE='''use nc_tunneldb;
            db.getCollection("Tunnels").countDocuments({"lifeCycle": { $ne: "Installed"}}) '''
        
        nctunneldb_mongo_script_Tunnel_Count_nc_tunnels='''use nc_tunneldb; 
        db.getCollection("Tunnels").countDocuments({})'''

        
        
        
        self.Mongo_query_maker(mplstp_mongo_script_BIDIRECTIONALITY,'TP_BIDIRECTIONAL')
        self.Mongo_query_maker(mpls_tp_mongo_script_UNIDIRECTIONALITY,'TP_UNIDIRECTIONAL')
        self.Mongo_query_maker(mplstp_mongo_script_TUNNEL_STATE_OK,'TP_OK_STATE')
        self.Mongo_query_maker(mplstp_mongo_script_TUNNEL_STATE_INCOMPLETE,'TP_INCOMPLETE_STATE')
        self.Mongo_query_maker(mplstp_mongo_script_TUNNEL_Count_mplstp,'TP_COUNT')

        self.Mongo_query_maker(nctunneldb_mongo_script_BIDIRECTIONALITY,'NC_BIDIRECTIONAL')
        self.Mongo_query_maker(nctunneldb_mongo_script_UNIDIRECTIONALITY,'NC_UNIDIRECTIONAL')
        self.Mongo_query_maker(nctunneldb_mongo_script_TUNNEL_STATE_OK,'NC_OK_STATE')
        self.Mongo_query_maker(nctunneldb_mongo_script_TUNNEL_STATE_INCOMPLETE,'NC_INCOMPLETE_STATE')
        self.Mongo_query_maker(nctunneldb_mongo_script_Tunnel_Count_nc_tunnels,'NC_COUNT')

        self.Tunnel_entity_count_final['BIDIRECTIONALITY']=self.Tunnel_entity_count['TP_BIDIRECTIONAL']+self.Tunnel_entity_count['NC_BIDIRECTIONAL']
        self.Tunnel_entity_count_final['UNIDIRECTIONAL']=self.Tunnel_entity_count['TP_UNIDIRECTIONAL']+self.Tunnel_entity_count['NC_UNIDIRECTIONAL']
        self.Tunnel_entity_count_final['TUNNEL_STATE_OK']=self.Tunnel_entity_count['TP_OK_STATE']+self.Tunnel_entity_count['NC_OK_STATE']
        self.Tunnel_entity_count_final['TUNNEL_STATE_INCOMPLETE']=self.Tunnel_entity_count['TP_INCOMPLETE_STATE']+self.Tunnel_entity_count['NC_INCOMPLETE_STATE']
        self.Tunnel_entity_count_final['COUNT']=self.Tunnel_entity_count['TP_COUNT']+self.Tunnel_entity_count['NC_COUNT']
        # print(self.Tunnel_entity_count_final)

         # CSV export
        csv_filename = 'Tunnels.csv'
        with open(csv_filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['type','count'])
            for key, value in self.Tunnel_entity_count_final.items():
                writer.writerow([key,value])

        print(f"self.csv_filename located at {self.path}/{csv_filename}")

        # print(f'Types_n_counts dictionary is updated as {self.Tunnel_entity_count}')

class Total_counts(ENIC):
    def __init__(self):
        self.Total_count={}
    
    def Mongo_query_maker(self,mongo_query,entity):
        try:
            # Open a sp to execute the kubectl exec command
            exec_process = sp.Popen(self.command_exec_pod, stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE, universal_newlines=True)

            # Send Mongo command through stdin to the exec process
            output, error = exec_process.communicate(input=f"{self.mongo_command}\n{mongo_query}\n")
            # print(output)
            # print(f"THer return code is {exec_process.returncode}")
            if exec_process.returncode == 0:
                # print("MongoDB Command Output:")
                # print(output)
                match = re.search(r'(\d+)(?=\s*bye)', output)  # This matches any digits       
                if match:
                        count = match.group(1)  # Extract the matched number
                        # self.Total_count[entity] = count
                        return int(count)
                        print(self.Total_count)
                        print(f"MongoDB Command Result  (count) of {entity}: {count}")
                else:
                    print(f"Error executing MongoDB command for {entity}.")
                    return None  # Return None if there's an execution error  
            else: 
                print(f"No count value found for {entity}.")
                return None  # Return None if no match is found             
        except:
            print("ERROR in executing k8s command {e.output.decode()}")
    
    def Mongo_queries(self):
        # Dictionary_of_total={MANAGED_ELEMENT_mongo_q:'''use nc_tapitopologydb;
        # db.getCollection("Nodes").countDocuments({"uploadState" : "Uploaded"})'''}

        MANAGED_ELEMENT_mongo_q='''use nc_tapitopologydb;
        db.getCollection("Nodes").countDocuments({"uploadState" : "Uploaded"})'''
        
        GROUP_mongo_q='''use nc_netmgrfulfilldb;
        db.getCollection("Groups").countDocuments({})
        '''

        PHYS_LINK_mongo_q='''use nc_netmgrfulfilldb;
        db.getCollection("PhysicalLinks").countDocuments({})
        '''

        SRE_TUNNELS_mongo_q='''use nc_tunneldb;
        db.getCollection("Tunnels").countDocuments({})
        '''
        MPLS_TUNNELS_mongo_q='''use tnlmgrmplstp;
        db.getCollection("MplstpTunnels").countDocuments({})
        '''

        EVPN_mongo_q='''use evpn;
        db.getCollection("evpn").countDocuments({})
        '''

        L2VPN_mongo_q='''use srvcfull2packetmanager;
        db.getCollection("l2service").countDocuments({})
        '''

        L3VPN_mongo_q='''use l3vpn;
        db.getCollection("l3vpn").countDocuments({})
        '''

        UNMANAGED_ELEMENT_mongo_q ='''use nc_tapitopologydb;
        db.getCollection("Nodes").countDocuments({"uploadState":{$ne:"Uploaded"}})
        '''

        self.Total_count['MANAGED_ELEMENT']= self.Mongo_query_maker(MANAGED_ELEMENT_mongo_q,'MANAGED_ELEMENT')
        self.Total_count['GROUP']= self.Mongo_query_maker(GROUP_mongo_q,'GROUP')
        self.Total_count['PHYS_LINK']= self.Mongo_query_maker(PHYS_LINK_mongo_q,'PHYS_LINK')
        self.Total_count['SRE_TUNNELS']= self.Mongo_query_maker(SRE_TUNNELS_mongo_q,'SRE_TUNNELS')
        self.Total_count['MPLS_TUNNELS']= self.Mongo_query_maker(MPLS_TUNNELS_mongo_q,'MPLS_TUNNELS')
        self.Total_count['UNMANAGED_ELEMENT']= self.Mongo_query_maker(UNMANAGED_ELEMENT_mongo_q,'UNMANAGED_ELEMENT')
        Evpn_total_count=self.Mongo_query_maker(EVPN_mongo_q,'EVPN_SERVICES')
        L2VPN_total_count=self.Mongo_query_maker(L2VPN_mongo_q,'L2VPN_SERVICES')
        L3VPN_total_count=self.Mongo_query_maker(L3VPN_mongo_q,'L3VPN_SERVICES')
        self.Total_count['SERVICES']=Evpn_total_count+L2VPN_total_count+L3VPN_total_count
        # self.Mongo_query_maker(EVPN_mongo_q,'SERVICES') + self.Mongo_query_maker(L2VPN_mongo_q,'SERVICES') + self.Mongo_query_maker(L3VPN_mongo_q,'SERVICES')
        # print(Evpn_total_count,L2VPN_total_count,L3VPN_total_count)

        # print(f"the final dictionay for total count to refer is {self.Total_count}")

         # CSV export
        csv_filename = 'TotalCount.csv'
        with open(csv_filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['type','count'])
            for key, value in self.Total_count.items():
                writer.writerow([key,value])

        # print(f"self.csv_filename located at {self.path}/{csv_filename}")

        # print(f'Types_n_counts dictionary is updated as {self.Tunnel_entity_count}')

        


Customer_name=input("Enter the customer name:")
Country=input("Enter the country Name:")
Account_number=input("Enter the account number:")
Obj=ENIC(Customer_name,Country,Account_number)
Obj.Connect_to_mongoDb()
Obj.Query_for_Shelfs()
Obj.Query_for_Cards()
Obj.NE_type_count()
Obj.NE_name_and_IP()
Obj.result()

Srv= Services()
Srv.Connect_to_mongoDb()
Srv.Mongo_query_builder()
Srv.srv_result()

Tun=Tunnels()
Tun.Connect_to_mongoDb()
Tun.Mongo_queries()

Total=Total_counts()
Total.Connect_to_mongoDb()
Total.Mongo_queries()
        
        
