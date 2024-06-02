### Bringing application into Kubernetes cluster

- By leveraging the Kubernetes's powers, you can deploy the application into Kubernetes cluster to get the high availability, scalability, and easy to rollout/rollback or implement many deployment strategy when deploying new application's version.

### Deployment

- To deploy the application into Kubernetes cluster, we need create 3 type of resources:
  - Deployment: that managed pod
  - Service: work as a load balancer for routing traffic to pod.
    - We can also use it to expose applications to external by using the service type `NodePort` or `LoadBalancer`, [here](https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer) for more details.
  - Ingress (Optional): expose service to external using ingress controller, i.e nginx ingress controller

- Following these steps:
  - Step 1: Create the deployment file.
  - Step 2: Create service file.
    - After create service, you can access to application by:
      - Forwarding service port to local
        ```
        kubectl port-forward svc/qac-screen-test-api 8080:8080
        ```
      - Accessing the application in browser with URL `localhost:8080`
  - Step 3: Create ingress file. (Optional)