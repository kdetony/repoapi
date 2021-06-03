resource "digitalocean_kubernetes_cluster" "kubernetes_cluster" {
  name    = "k8s-ks"
  region  = "ams3"
  version = "1.20.2-do.0"

  node_pool {
    name       = "ks-pool"
    size       = "s-1vcpu-2gb" 
    auto_scale = false
    node_count = 2
  }

}
