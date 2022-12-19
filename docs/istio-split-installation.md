# Split IstioOperator Installation file (control plane & gateway)
1. in the current istioOperator file, add 
```
metadata:
  name: control-plane
  namespace: istio-system
```
if it's not done yet. it will not rollout restart any deployment

this will add labels into the deployment
```
install.operator.istio.io/owning-resource: control-plane
install.operator.istio.io/owning-resource-namespace: istio-system
```
from previously
```
install.operator.istio.io/owning-resource: unknown
```

always fucking confirm with --dry-run!
```
istioctl install -f control-plane.yaml --force --skip-confirmation --dry-run
istioctl install -f control-plane.yaml --force --skip-confirmation
````

2. create IstioOperator for each gateway, don't forget to change the metadata.name

execute in each gateway
```
istioctl install -f istio-public-gateway.yaml --force --skip-confirmation --dry-run
istioctl install -f istio-public-gateway.yaml --force --skip-confirmation
````

this will replace
```
install.operator.istio.io/owning-resource: control-plane
install.operator.istio.io/owning-resource-namespace: istio-system
```
with
```
install.operator.istio.io/owning-resource: <IstioOperator name>
install.operator.istio.io/owning-resource-namespace: istio-system
```

it will rollout restart gateway

3. remove all gateway object from control-plane IstioOperator and run istioctl again

```
istioctl install -f control-plane.yaml --force --skip-confirmation --dry-run
istioctl install -f control-plane.yaml --force --skip-confirmation
````

4. add profile: minimal in the control-plane file
```
spec:
  hub: ghcr.io/resf/istio
  profile: minimal
```

```
istioctl install -f control-plane.yaml --force --skip-confirmation --dry-run
istioctl install -f control-plane.yaml --force --skip-confirmation
````
