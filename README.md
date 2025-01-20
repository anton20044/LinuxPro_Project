Проектная работа по курсу Administrator Linux. Professional.

  Тема проекта "Реализация отказоустойчивой инфраструктуры платежного приложения"


Проект разворачивает 14 ВМ: 
  
  - 3 с ролью кластера etcd
  - 2 с ролью СУБД PostgreSQL
  - 2 с ролью HaProxy + VIP
  - 2 с ролью DNS
  - 1 с ролью мониторинга
  - 1 с ролью центрального сбора логов
  - 1 с ролью сервера резервного копирования СУБД
  - 2 с ролью сервера приложений
  - 2 с ролью пограничного маршрутизатора

!!! Перед разворачиванием в VirtualBox должен быть создан bringe интерфейс.

### Восстановление любой ВМ (за исключением ВМ из кластера ETCD, приложений и СУБД):
```

  - vagrant destroy -f [name_vm]
  - vagrant up [name_vm]
  - ansible-playbook -i ansible/hosts ansible/playbook -l [name_vm]
```

### Восстановления ноды ETCD:
```
  - Выставить значение переменной raft_restore в 1, в файле ansible/group_vars/raft.yml
  - Указать имя живой ноды в кластере, на которой будем проводить маникуляции по удалению отказавшей и добавлению новой новы. Переменая node_restore_from, в файле ansible\group_vars\raft.yml
  - Указать 1 для переменной vm_restore,  это переменная хоста и для хоста etcd03 она хранится в файле ansible/host_vars/etcd03.yml
  - vagrant destroy -f [name_vm]
  - vagrant up [name_vm]
  - ansible-playbook -i ansible/hosts ansible/playbook -l [name_vm]
ИЛИ
  - ansible-playbook -i ansible/hosts ansible/playbook -l [name_vm] -e raft_restore=1 -e node_restore_from=etcd01 -e vm_restore=1
```
### Восстановления ноды сервера приложений
```
 - Выставить значение переменной app_make_migr в 0, в файле ansible/host_vars/app01.yml
 - Выставить значение переменной load_test_data в 0, в файле ansible/host_vars/app01.yml
 - ansible-playbook -i ansible/hosts ansible/playbook -l [name_vm]
ИЛИ
  - ansible-playbook -i ansible/hosts ansible/playbook -l [name_vm] -e app_make_migr=0 -e load_test_data=0
```
Восстановление ноды кластера СУБД
```
  - Выставить значение переменной pg_state в replica, в файле ansible/host_vars/pg01.yml
  - ansible-playbook -i ansible/hosts ansible/playbook -l [name_vm]
ИЛИ
  - ansible-playbook -i ansible/hosts ansible/playbook -l [name_vm] -e pg_state=replica
``` 
