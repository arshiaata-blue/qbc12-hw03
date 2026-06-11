# HW03 Docker Image Size Report

| Repository           | Tag       | Size   |
|:---------------------|:----------|:-------|
| qbc12-airbnb-serving | optimized | 1.29GB |
| qbc12-airbnb-serving | naive     | 3.14GB |

## Analysis
The naive image is significantly larger (3.14GB) because it uses the full `python:3.11` base image and leaves behind all intermediate build tools, caches, and compiler dependencies. In contrast, the optimized image (1.28GB) utilizes a multi-stage build with `python:3.11-slim`, isolating the compilation environment and copying only the finalized, compiled Python site-packages into the runtime layer. For production, the optimized image is the definitive choice as its smaller footprint significantly reduces network latency and significantly shrinks the container's security attack surface.
