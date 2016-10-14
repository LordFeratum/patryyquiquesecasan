# https://hub.docker.com/r/zzrot/alpine-caddy/
FROM zzrot/alpine-caddy:v0.9.3

COPY Caddyfile /etc/Caddyfile

# disable http2 for proxy pass errors
# https://github.com/mholt/caddy/issues/1080
#CMD ["caddy", "--conf", "/etc/Caddyfile", "-http2=false"]
CMD ["caddy", "--conf", "/etc/Caddyfile"]
