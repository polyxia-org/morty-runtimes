FROM --platform=${TARGETPLATFORM:-linux/amd64} ghcr.io/polyxia-org/alpha:v0.2.2 as get-alpha
FROM --platform=${BUILDPLATFORM:-linux/amd64} golang:1.19-alpine as build

ARG TARGETPLATFORM

# Get Alpha and make it executable in the final build image
COPY --from=get-alpha /alpha /usr/bin/alpha
RUN chmod +x /usr/bin/alpha

RUN apk --no-cache add git

RUN mkdir -p /go/src/handler
WORKDIR /go/src/handler
COPY . .

ARG GO111MODULE="on"
ARG GOPROXY=""
ARG GOFLAGS=""
ARG CGO_ENABLED=0
ENV CGO_ENABLED=${CGO_ENABLED}

WORKDIR /go/src/handler/function

WORKDIR /go/src/handler
RUN GOOS=${TARGETOS} GOARCH=${TARGETARCH} \
    go build --ldflags "-s -w" -o handler .

FROM --platform=${TARGETPLATFORM:-linux/amd64} alpine:3.17.2

ARG ADDITIONAL_PACKAGE

RUN apk --no-cache add curl ca-certificates ${ADDITIONAL_PACKAGE} 

# Split instructions so that buildkit can run & cache
# the previous command ahead of time.
RUN mkdir -p /app 

WORKDIR /app

COPY --from=build /go/src/handler/handler .
COPY --from=build /usr/bin/alpha .

WORKDIR /
