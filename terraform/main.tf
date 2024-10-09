terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 6.6.0"  # O usa la última versión estable
    }
  }
}

provider "google" {
  project = "lat-test-437905"
  region  = "us-central1"
}

resource "google_cloud_run_service" "ingest_service" {
  name     = "data-ingest"
  location = "us-central1"

  template {
    spec {
      containers {
        image = "aandresbarreras/ingest:1"  

        ports {
          container_port = 8080 
        }
      }
    }
  }

  
}

resource "google_cloud_run_service" "data_service" {
  name     = "data-service"
  location = "us-central1"

  template {
    spec {
      containers {
        image = "aandresbarreras/data:latest"  

        ports {
          container_port = 8081  
        }
      }
    }
  }

  # Omite la sección de traffic hasta que tengas una revisión disponible
}

resource "google_cloud_run_service_iam_member" "ingest_invoker" {
  service  = google_cloud_run_service.ingest_service.name
  location = google_cloud_run_service.ingest_service.location
  role     = "roles/run.invoker"
  member   = "allUsers"  # Permitir acceso a todos los usuarios
}

resource "google_cloud_run_service_iam_member" "data_invoker" {
  service  = google_cloud_run_service.data_service.name
  location = google_cloud_run_service.data_service.location
  role     = "roles/run.invoker"
  member   = "allUsers"  # Permitir acceso a todos los usuarios
}

output "ingest_service_url" {
  value = "Ingest Service URL: ${google_cloud_run_service.ingest_service.status[0].url}/ingest"
}

output "data_service_url" {
  value = "Data Service URL: ${google_cloud_run_service.data_service.status[0].url}/data"
}