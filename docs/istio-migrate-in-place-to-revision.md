# Istio migrate In-Place upgrade to Revision upgrade

this scenario is when the current in-place upgrade doesn't have any `revision` tag.

1. make sure you already split istio control plane and gateway into different istioOperator.
2. install new revision of control plane
```
istioctl install -f control-plane.yaml --force --skip-confirmation --dry-run --revision 1-15-4
istioctl install -f control-plane.yaml --force --skip-confirmation --revision 1-15-4
```

3. upgrade in-place each gateway, also use --revision
```
istioctl install -f control-plane.yaml --force --skip-confirmation --dry-run --revision 1-15-4
istioctl install -f control-plane.yaml --force --skip-confirmation --revision 1-15-4
```
this will in-place upgrade the gateway rather than creating a new deployment

4. upgrade each namespace with the new labels
add label
```
istio.io/rev: 1-15-4
```
remove label
```
istio-injection: enabled
```

5. feel free to rollout restart deployment on the namespace, or you don't (as infra engineer)

6. after all workload migrated to the revision control plane, delete the non revision control-plane
```
istioctl uninstall -f control-plane.yaml --force --skip-confirmation --dry-run
istioctl uninstall -f control-plane.yaml --force --skip-confirmation
```

there is several clusterRole that get deleted, reapply the revision
```
istioctl install -f control-plane.yaml --force --skip-confirmation --dry-run --revision 1-15-4
istioctl install -f control-plane.yaml --force --skip-confirmation --revision 1-15-4
```
