# pergent.sh

[pergent.sh](https://github.com/gopaytech/pergent.sh) reviews GitHub pull requests with an LLM, one Kubernetes Job per review.

## Where it lives

| Piece | Where |
|---|---|
| ArgoCD app (chart) | `clusters/home-lab-kubernetes-01/argocd/namespaces/argocd-system/applications.argoproj.io/pergent-sh.yaml` |
| Postgres (CNPG `pergent-pg`) and sealed Secrets | `clusters/home-lab-kubernetes-01/argocd/namespaces/pergent-sh/` |
| Public host `pergent.zufardhiyaulhaq.com` | `clusters/home-lab-kubernetes-01/argocd/namespaces/istio-system/ingress/pergent.zufardhiyaulhaq.com/` |
| Namespaces | `pergent-sh` (service, database), `pergent` (review and scan Jobs) |

## What is public

Only the GitHub App webhook, `POST /webhooks/github/<instance>`. Everything else stays private:

- The dashboard is reached with a port-forward: `kubectl -n pergent-sh port-forward svc/pergent-sh 8080:8080`, then `http://localhost:8080`.
- Review, scan and skill-fetch Jobs report back in-cluster through `callback_url` (`http://pergent-sh.pergent-sh.svc:8080`), so `/runs/`, `/readiness-scans/` and `/skill-fetches/` are not routed on the public host.

## How the webhook is protected

| Layer | What it does |
|---|---|
| VirtualService | Routes only the `/webhooks/github/` prefix to `pergent-sh:8080`. |
| AuthorizationPolicy | Allows only `POST` to `/webhooks/github/*` from GitHub's `hooks` ranges in `https://api.github.com/meta`. Anything else on the host gets 403. The source IP is the real client because frp sends PROXY protocol v2 to the gateway. |
| pergent.sh | Checks `X-Hub-Signature-256` (HMAC-SHA256 with the webhook secret) and answers 401 on a mismatch. The body is capped at 5 MiB. |
| TLS | TLS 1.3 only. HTTP redirects to HTTPS. |

If GitHub adds a new `hooks` range, its deliveries get 403 until the range is added to the AuthorizationPolicy.

## Upgrading

Bump `targetRevision` in the ArgoCD app. Read the release notes first: a release can add a database migration that runs at startup.
