# Stage 1: Build Vite & Vue static assets
FROM node:20-alpine AS build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Stage 2: Caddy web server and reverse proxy
FROM caddy:2.7-alpine AS production-stage

# Copy the built Vue app
COPY --from=build-stage /app/dist /srv

# Copy the custom Caddyfile
COPY Caddyfile /etc/caddy/Caddyfile

# Expose HTTP and HTTPS ports
EXPOSE 80 443

CMD ["caddy", "run", "--config", "/etc/caddy/Caddyfile", "--adapter", "caddyfile"]
