test Latam
1. Arquitectura de la Solución
1.1 Infraestructura en la Nube
Se utilizó Google Cloud Platform (GCP) para desplegar dos instancias de Cloud Run. Este enfoque sigue las recomendaciones para mantener la simplicidad y funcionalidad. Las instancias utilizan imágenes separadas:

Servicio GET: Se encarga de obtener datos desde una base de datos MongoDB.
Servicio POST (Ingest): Se utiliza para alimentar la base de datos.
Se implementaron políticas de IAM para asegurar el acceso a través de HTTPS sin restricciones. La base de datos se aloja en MongoDB Atlas. Consulta el diagrama 2.4 para más detalles.

1.2 Despliegue con Terraform
Se utiliza Terraform para la creación de la infraestructura, que incluye el despliegue de imágenes de Docker mediante dos scripts: uno para el método GET y otro para el método POST (Ingest). Esto permite la inyección de datos en los topics correspondientes. Además, se implementan pruebas unitarias para el script de GET.

2. Implementación y Pruebas
2.1 Despliegue HTTP
El servicio se despliega a través de Docker utilizando Cloud Run e integrado con GitHub Actions. Puedes consultar un ejemplo de ejecución del job aquí: Ejecución del Job.

Endpoint para GET: https://data-service-360293459643.us-central1.run.app/data
2.2 Integración Continua
En el proceso de integración continua, se realiza un análisis de código estático utilizando SonarQube. Los pasos incluyen la generación de la imagen de Docker, el push y el despliegue utilizando el comando gcloud run deploy.

2.3 Servicio de Ingest
El servicio de Ingest utiliza el método POST para ingresar datos en la base de datos de MongoDB.

Endpoint para POST: https://data-ingest-q3al6muwza-uc.a.run.app/ingest
2.4![DIAGRAMA](https://github.com/user-attachments/assets/d0f618bf-d80a-4c4f-94db-be4bef825f00)


Lo demás está en progreso.
