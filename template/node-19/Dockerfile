FROM --platform=${TARGETPLATFORM:-linux/amd64} ghcr.io/polyxia-org/alpha:v0.2.2 as get-alpha
FROM --platform=${TARGETPLATFORM:-linux/amd64} node:19-alpine

ARG TARGETPLATFORM
ARG ADDITIONAL_PACKAGE

RUN apk --no-cache add curl ca-certificates ${ADDITIONAL_PACKAGE}

# Get Alpha and make it executable in the final build image
COPY --from=get-alpha /alpha /usr/bin/alpha
RUN chmod +x /usr/bin/alpha

RUN mkdir -p /app

# Install entrypoint dependencies
WORKDIR /app
COPY package.json .
RUN npm install

# Copy the function entrypoint
COPY index.js .

# Install function dependencies in a separate layer to allow caching
WORKDIR /app/function
COPY function/*.json ./
RUN npm install

# Copy the function
COPY function/ .

WORKDIR /
