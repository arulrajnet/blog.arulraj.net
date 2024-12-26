---
title: No More Basic Auth &#58; htpasswd with OAuth2 Proxy
date: 2024-12-15 20:44:14
author: arul
category: Security
tags: proxy,Traefik,APISix,nginx
slug: no-more-basic-auth-htpasswd-with-oauth2-proxy
disqus_identifier: no-more-basic-auth-htpasswd-with-oauth2-proxy
cover: /assets/images/basic-auth-oauth2-proxy-cover.png
color: gray
headline: Create cookie session store for htpasswd based authentication using oauth2-proxy. This will eliminate the insecure basic authentication.
status: published
---

In this blog post, we are going to see how we can enable authentication based on an htpasswd file using OAuth2 Proxy.

Before that, let's discuss the problems with htpasswd + Basic Authentication.
## The problem

### What is an htpasswd File?

An `htpasswd` file contains a finite number of usernames and passwords encrypted using the highly secure bcrypt algorithm. The file looks like the following:

```txt
admin@mycompany.com:$2y$05$Npda/wcHOGrBKYgr9sNJo./O8KZbXQqwTrF0BcRxiS5Vr.P37zDJC
user@mycompany.com:$2y$05$crIQ3pU/dJi2T6c8IM1UNOXV6KlgxjvFBvJH2ZfmmhgRSS8qObZVu
another-user@mycompany.com:$2y$05$tQrvnJQgeroRwi8FJgHsUufUZpU3lrmoMMXC9xYZ9XA9Kno0iwDWy
```

Most of the time, the htpasswd file is used in conjunction with Basic Authentication. Basic Authentication works by sending a Base64-encoded username and password as an `Authorization` header in every request. On the server side, these credentials are validated against the htpasswd file.

<!-- ### Proxies That Support This Authentication Method

The following proxies support this method of authentication:

* [NGinx](https://docs.nginx.com/nginx/admin-guide/security-controls/configuring-http-basic-authentication/)
* [HAProxy](https://www.haproxy.com/documentation/haproxy-configuration-tutorials/authentication/basic-authentication/)
* [Traefik](https://doc.traefik.io/traefik/middlewares/http/basicauth/)
* [APISix](https://apisix.apache.org/docs/apisix/plugins/basic-auth/)
* [Caddy](https://caddyserver.com/docs/caddyfile/directives/basic_auth)
* [Envoy](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/basic_auth_filter.html) -->
### Why Is This the Most Insecure Way to Handle Authentication?

Using htpasswd with Basic Authentication is considered highly insecure for the following reasons:

- **Plain Username and Password Are Sent in Every Request**
    - Although encoded in Base64, it is easily decodable.
- **Lack of Session Management**
    - There is no session handling; credentials are sent repeatedly with every request.
- **Password Stored in Client-Side Cache as Plain Text**
    - If the client device is compromised, cached credentials can be exploited.
- **Exposure in Logs**
    - Credentials can appear in browser history, server logs, and proxy logs, increasing the chances of leakage.
- **No Logout Mechanism**
    - There is no way to log out a user or invalidate credentials once they are compromised.

You might also have seen this method in use in legacy devices, such as older routers and network appliances.

![[basic-auth-popup.png]]

## The Objective

The **htpasswd** file is an excellent fit for applications with a finite number of users. If an application wants to leverage the flexibility of an htpasswd file but without relying on Basic Authentication, **OAuth2-Proxy** is the perfect solution for this use case.

OAuth2-Proxy creates a cookie-based session upon login and uses this cookie for subsequent authentication. The cookie has an expiration time and can be refreshed at regular intervals. It also includes built-in support for CSRF tokens, enhancing security.
## The challenges

While there are various ways to replace Basic Authentication, we’ve chosen to address it using the open-source software [OAuth2-Proxy](https://github.com/oauth2-proxy/oauth2-proxy). However, using OAuth2-Proxy comes with its own set of challenges:

- **Focus on OIDC/OAuth2-Based Authentication**
    - As the name suggests, OAuth2-Proxy primarily focuses on OpenID Connect (OIDC) and OAuth2 authentication methods.
    - By default, the application requires **at least one OIDC provider to be configured**.
    - There is no official support for disable provider [https://github.com/oauth2-proxy/oauth2-proxy/issues/1725#issuecomment-1195865190](https://github.com/oauth2-proxy/oauth2-proxy/issues/1725#issuecomment-1195865190)
    - The `htpasswd` file-based authentication is optional and secondary.
- **No Support for External Standalone Login Pages**
    - OAuth2-Proxy includes a built-in login page, which can be customized. However, it is pure HTML and lacks advanced design capabilities.
    - If your application uses a **ReactJS-based branded login page**, it won’t be supported by default.
## Solutions

There are two main approaches to address these challenges:

* Dummy OAuth2 Provider + Built-in Login Page.
* Dummy OAuth2 Provider + Standalone Login page.

The OAuth2-Proxy can be run as a http proxy to route traffic to the upstream. In this setup, the routing is handled by some well known proxy and OAuth2-Proxy act as a [forward-auth](https://doc.traefik.io/traefik/middlewares/http/forwardauth/).
### with built-in login page

I’m a big fan of **Traefik Proxy**! Its Docker label-based configuration is on another level🔥in CNCF ecosystem. For this setup, I’ve chosen Traefik as the reverse proxy in front of OAuth2-Proxy.

![[htpasswd-oauth2-proxy.drawio.png]]

The config of oauth2 proxy is look like

```bash
--client-id=dummy-client-id,
--client-secret=dummy-client-secret,
--cookie-expire=168h,
--cookie-name=_session,
--cookie-refresh=30m,
--cookie-secret=cbiGJkwts9Ye6XD2Pbt_L1jLcipIZBDMfMuqxDWRbeQ=,
--custom-sign-in-logo=https://avatars.githubusercontent.com/u/4029521?v=4,
--custom-templates-dir=/templates,
--cookie-secure=false,
--email-domain=*,
--footer=Powered by <a href='https://mycompany.com'>My Company</a>,
--htpasswd-file=/.htpasswd,
--http-address=0.0.0.0:4181,
--provider=google,
--proxy-prefix=/auth,
--reverse-proxy=true,
--set-authorization-header,
--set-xauthrequest,
--skip-provider-button=false,
--upstream=static://202
```

In this the client-id and client-secret are dummy values.

**The Login page**

![[oauth2-proxy-login-page.png]]

**The Cookie**

![[oauth2-proxy-cookie-page.png]]

The docker compose stack is in [GitHub Repo](https://github.com/arulrajnet/oauth2-proxy-without-provider/tree/main/built-in-login-page)
### with standalone login page

In some cases, the login page also serve from the application. This is for, how to handle it.

![[htpasswd-oauth2-proxy-standalone-login.drawio.png]]

**Traefik Config**

Remove the middleware for the `/login` and `/static` URL for app.

```
- traefik.http.routers.app-noauth.rule=PathPrefix(`/login`) || PathPrefix(`/static`)
- traefik.http.routers.app-noauth.entrypoints=web
- traefik.http.routers.app-noauth.priority=200
```

Added errors middleware to handle errors.

```
- traefik.http.middlewares.oauth2-proxy-error.errors.service=app@docker
- traefik.http.middlewares.oauth2-proxy-error.errors.status=401,403
- traefik.http.middlewares.oauth2-proxy-error.errors.query=/login
```

 This is not working. TODO.

**OAuth2 Config**

The Login page written in Your Preferrable language.

![[oauth2-proxy-standalone-login-screen.png]]

The form POST request to `/auth/sign_in`

**The Cookie**

There is no difference in the cookie.

## Final Thoughts

This solution eliminates Basic Authentication for your application using OAuth2 Proxy, making it ideal for newly developed software (Greenfield projects).

But what about the legacy devices and applications (Brownfield systems) in your network that have relied on Basic Authentication for decades? If you're still accessing them using Basic Authentication, your system is at significant risk.

How can these systems be protected? This is a critical topic with plenty to discuss, which we'll cover in detail in an upcoming [post](shielding-legacy-applications-eliminating-basic-authentication-without-code-changes)(coming soon).
