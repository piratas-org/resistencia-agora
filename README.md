# resistencia-agora

[Agora Voting](https://agoravoting.com/) deployment for [Resistencia](https://github.com/confederacion-pirata/resistencia) servers.

If you want to collaborate: fork, change, pull request, repeat. All contributions will be reviewed as soon as possible. Thanks!

This is a [Confederación Pirata](http://confederacionpirata.org/) project.

## Usage

```
# mkdir -p myserver.example.com/roles
# cat > myserver.example.com/localhost <<EOF
127.0.0.1 ansible_connection=local
EOF
# cat > myserver.example.com/site.yml <<EOF
---
- hosts: all
  vars:
    - hostname: myserver.example.com
    - admin: { user: admin,
               name: 'Your Name',
               email: admin@thirdparty.com,
               key: URGPGKEY,
               internal_email: "root@{{hostname}}" }
  roles:
    - resistencia
    - resistencia-agora
EOF
# cat > myserver.example.com/ansible.cfg <<EOF
[defaults]
transport=ssh
hash_behaviour=merge

[ssh_connection]
pipelining=True
EOF
# git clone https://github.com/confederacion-pirata/resistencia myserver.example.com/roles/resistencia
# git clone https://github.com/confederacion-pirata/resistencia-agora myserver.example.com/roles/resistencia-agora
# ansible-playbook -i myserver.example.com/localhost myserver.example.com/site.yml
```
