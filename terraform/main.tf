provider "azurerm" {
  version = "=2.0.0"
  features {}
}

resource "azurerm_resource_group" "cards" {
  name     = terraform.workspace
  location = "uksouth"
}

resource "azurerm_kubernetes_cluster" "cards" {
  name                = "cards-aks1"
  location            = azurerm_resource_group.cards.location
  resource_group_name = azurerm_resource_group.cards.name
  dns_prefix          = "cardsaks1"

  default_node_pool {
    name       = "default"
    vm_size    = var.vm_size
    enable_auto_scaling = true
    min_count           = var.min_nodes
    max_count           = var.max_nodes
  }

  identity {
    type = "SystemAssigned"
  }

  service_principal {
    client_id     = var.client_id
    client_secret = var.client_secret
  }
}
