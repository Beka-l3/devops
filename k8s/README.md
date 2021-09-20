# Lab 9
## 1
```
minikube start

kubectl create deployment my_app  --image=beka13/python_app:latest
```
## 2
```
kubectl expose deployment my-app --type=LoadBalancer --port=80
```

## 3
```
Bekzhans-MBP k8s % kubectl get pods,svc
NAME                          READY   STATUS    RESTARTS   AGE
pod/my-app-7cff8957f8-kvhrf   1/1     Running   0          9m38s

NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP   PORT(S)        AGE
service/kubernetes   ClusterIP      10.96.0.1        <none>        443/TCP        10m
service/my-app       LoadBalancer   10.101.179.102   <pending>     80:31659/TCP   8m22s
```

## 4
```
kubectl delete deployment,svc my-app
```

## 5 Create Deployment and Service .yml then run them
```
Bekzhans-MBP k8s % kubectl get pods,svc     
NAME                                  READY   STATUS    RESTARTS   AGE
pod/app-deployment-5bf57b5b7d-bkscd   1/1     Running   0          3m37s
pod/app-deployment-5bf57b5b7d-p2mbm   1/1     Running   0          3m37s
pod/app-deployment-5bf57b5b7d-vknm5   1/1     Running   0          3m37s

NAME                 TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
service/kubernetes   ClusterIP      10.96.0.1      <none>        443/TCP        56m
service/my-app       LoadBalancer   10.109.56.76   <pending>     80:32407/TCP   3m31s
```
## 6 Clean up
```
kubectl delete svc my-app
kubectl delete deployment app-deployment
```

# Lab 10

## 1
```
helm create my-app
```

## 2
```
helm package my-app
helm install my-app ./my-app-0.1.0.tgz

minikube service my-app
```

## 3
```
Bekzhans-MBP k8s % kubectl get pods,svc   
NAME                          READY   STATUS    RESTARTS   AGE
pod/my-app-6c97ffc5f7-svztp   1/1     Running   0          23s

NAME                 TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
service/kubernetes   ClusterIP      10.96.0.1      <none>        443/TCP          103m
service/my-app       LoadBalancer   10.107.235.2   <pending>     8080:31914/TCP   23s
```

## 4 
```
minikube start
minikube dashboard
```
<img width="1440" alt="Screenshot 2021-09-20 at 21 49 30" src="https://user-images.githubusercontent.com/61314408/134058255-a5fa9f6e-67a6-4551-b2ab-df158888d041.png">


