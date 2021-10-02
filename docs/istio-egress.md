k exec -it deploy/examples-helloworld-v1 -c examples-helloworld-v1 bash
k logs deploy/examples-helloworld-v1 -c istio-proxy -f --tail 1 | jq

wget https://github.com/grpc-ecosystem/grpc-health-probe/releases/download/v0.4.5/grpc_health_probe-linux-amd64
mv grpc_health_probe-linux-amd64 grpc_health_probe
chmod +x grpc_health_probe

http
curl http://helloworld.zufardhiyaulhaq.dev/api/v1/ -v

https
curl https://helloworld.zufardhiyaulhaq.dev/api/v1/ -v -k
curl http://helloworld.zufardhiyaulhaq.dev:8080/api/v1/ -v

mtls
curl https://helloworld.zufardhiyaulhaq.dev:8443/api/v1/ -v -k (expected fail because no certificate)
curl http://helloworld.zufardhiyaulhaq.dev:8008/api/v1/ -v

grpc
./grpc_health_probe -addr=helloworld.zufardhiyaulhaq.dev:80 -v 

grpc tls
./grpc_health_probe -addr=helloworld.zufardhiyaulhaq.dev:443 -tls -v 
./grpc_health_probe -addr=helloworld.zufardhiyaulhaq.dev:8080 -v 

grpc mtls
./grpc_health_probe -addr=helloworld.zufardhiyaulhaq.dev:8443 -tls -v (expected fail because no certificate)
./grpc_health_probe -addr=helloworld.zufardhiyaulhaq.dev:8008 -v 
