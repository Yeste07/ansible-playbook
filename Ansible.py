Ansible.py


#Ad hoc : command

Ansible this
Ansible that 

#exemple :

ansible hosts -m module [ -a 'module arguments'] [-i inventory]

#To create the user lisa on all clients :

ansible all -m user -a "name=lisa"

#To remove the user lisa on all clients

ansible all -m user -a "name=lisa state=absent"

#To verify if the user lisa still exist :

ansible all -m command -a "id lisa"


#all ansible module 
ansible-doc -l 

#
ansible all -m ping 



#ansible Raw : use Raw roles without python needand not managed with ansible
ansible-doc raw






#Playbooks synthax : Yaml syntax 

---
- name :
  task
   - name :
     module
        arguments1
        arguments2
   - name :
     ******

- name2 :    
  task
   - name :
     module

#Exemple Playbooks :

---
 - name: install vsftpd on clients
   hosts: ansible1 
   task: 
   - name: install vsftpd
     yum: name=vsftpd
     service: vsftpd enabled=true

...

   #Ansible check syntax playbooks:

   ansible-playbook --syntax-check vsftpd.yml 

   #Ansible check playbook with more details :

   ansible-playbook -vvvv vsftpd.yml 




# To check if httpd packages are installed 
  ansible ansible1 -m shell -a "rpm -qa | grep 'httpd'"


# simple playbook to create a user using variable
---
name: create a user using variable
hosts: all
vars: 
  user: yassine
tasks:
  -	name: create user {{ user }}
	user:
      name: {{ users }}
...


#ansible vault


  ansible-vault create secret.yml
  cat secret.yml (contain username and passwordhash) 
  ansible-playbook --ask-vault-pass create-user.yml 
  vim create-user.yml
  ansible-playbook --ask-vault-pass create-user.yml 
  ansible all -m user -a "id SFR"
  ansible all -m command -a "id SFR"
  echo password > vault-pass
  cat vault-pass 

#ansible fact 

 ansible -m setup -a 'filter=ansible_default_ipv4.address' all
 #to show all informations
 ansible -m setup all
 #to show ip v4 address 
 ansible -m setup -a 'filter=ansible_default_ipv4' all



#ansible loops vs items

 items_* ansible version before than 2.5 
 loops   ansible version 2.5 and latest


with_items : loop keywords 
with_files : the item contains a file, wich contents is used to loop through
with_sequence : generates a list of values based on a numeric sequence

Some exemples:

-	name: create a users 
    hosts: ansible1
    tasks:
     - name: create users
       users:
        name: {{ item.name }}
        state: present
        group: {{ item.group }}
       
    loop:
       - name: anna
         groups: wheel
       - name: linda
         groups: users
       - name: bob
         groups: users
---------------------------------------------------
- name: start some services 
  hosts: ansible1
  vars:
    my_services:
      - crond
      - sshd
      - httpd
      - smb
  tasks:
  - name: enable services
    service:
      name: "{{ item }}"
      state: started
    with_items: "{{ my_services }}"









