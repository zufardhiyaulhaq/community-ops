# Migration tutorial

###
```bash
KUBECONFIG=~/.kube/config-server kubectl --context=kubernetes-cluster-02 -n default scale --replicas=0 deployment/examples-helloworld-v1
```

##### 1. Check the services
```bash
KUBECONFIG=~/.kube/config-server kubectl --context=kubernetes-cluster-01 get nodes -L 'topology.kubernetes.io/region,topology.kubernetes.io/zone'
KUBECONFIG=~/.kube/config-server kubectl --context=kubernetes-cluster-02 get nodes -L 'topology.kubernetes.io/region,topology.kubernetes.io/zone'

KUBECONFIG=~/.kube/config-server kubectl --context=kubernetes-cluster-01 -n default get pod
KUBECONFIG=~/.kube/config-server kubectl --context=kubernetes-cluster-02 -n default get pod
```

##### 2. curl to public gateway in kubernetes-cluster-01
```bash
while true
do date;curl https://helloworld.zufardhiyaulhaq.dev/hello --resolve helloworld.zufardhiyaulhaq.dev:443:88.198.50.247; echo; sleep 2;
done
```

##### 3. scale up helloworld service in kubernetes-cluster-02
```bash
KUBECONFIG=~/.kube/config-server kubectl --context=kubernetes-cluster-02 -n default scale --replicas=1 deployment/examples-helloworld-v1
```

##### 4. monitor curl, it's should start load balance the traffic

##### 5. scale down helloworld service in kubernetes-cluster-01
```bash
KUBECONFIG=~/.kube/config-server kubectl --context=kubernetes-cluster-01 -n default scale --replicas=0 deployment/examples-helloworld-v1
```

##### 6. monitor curl, all traffic should go to kubernetes-cluster-02

##### 7. change DNS record to kubernetes-cluster-02
```bash
while true
do date;curl https://helloworld.zufardhiyaulhaq.dev/hello --resolve helloworld.zufardhiyaulhaq.dev:443:88.198.50.164; echo; sleep 2;
done
```

### Reset
```bash
KUBECONFIG=~/.kube/config-server kubectl --context=kubernetes-cluster-01 -n default scale --replicas=1 deployment/examples-helloworld-v1
KUBECONFIG=~/.kube/config-server kubectl --context=kubernetes-cluster-02 -n default scale --replicas=1 deployment/examples-helloworld-v1
```
