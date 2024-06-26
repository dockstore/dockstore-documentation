+----------------------+-----------------------------+----------------------------------------+
| Differences          | Legacy Tool                 | GitHub App Tool                        |
+======================+=============================+========================================+
| Use case             | User owns the Docker image  | User doesn't need to own the image     |
|                      |                             |                                        |
|                      |                             | (or their tool does not use Docker)    |
+----------------------+-----------------------------+----------------------------------------+
| Dockerfile           | Dockerfile required         | Dockerfile not required                |
+----------------------+-----------------------------+----------------------------------------+
| Versioning           | Based on image's tags       | Based off of branches/tags from git    |
|                      |                             |                                        |
|                      |                             | repository                             |
+----------------------+-----------------------------+----------------------------------------+
| Path                 | Docker container location   | GitHub repository location             |
+----------------------+-----------------------------+----------------------------------------+
| Dockstore CLI        | Run in tool mode            | Run in workflow mode                   |
+----------------------+-----------------------------+----------------------------------------+

.. it might be worth making another version of this that includes workflows plus launch-with support, and putting it in tools-vs-workflows.rst